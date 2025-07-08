import argparse
import logging
from utils import get_binance_client
from market_orders import place_market_order
from limit_orders import place_limit_order
from advanced.stop_limit import place_stop_limit_order

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler()
    ]
)


# Command-line argument parsing
def parse_args():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", required=True, choices=["market", "limit"], help="Order type")
    parser.add_argument("--quantity", required=True, type=float, help="Quantity to trade")
    parser.add_argument("--price", type=float, help="Price (required for limit orders)")
    parser.add_argument("--stop_price", type=float, help="Trigger price (for stop-limit orders)")

    return parser.parse_args()

# Main entry point
if __name__ == "__main__":
    args = parse_args()
    client = get_binance_client()

    if args.type == "market":
        place_market_order(client, args.symbol, args.side, args.quantity)
    elif args.type == "limit":
        if not args.price:
            print(" Limit orders require a --price argument.")
        else:
            place_limit_order(client, args.symbol, args.side, args.quantity, args.price)
    elif args.type == "stop-limit":
        if not args.price or not args.stop_price:
            print(" Stop-limit requires both --price and --stop_price.")
        else:
            place_stop_limit_order(
                client,
                symbol=args.symbol,
                side=args.side,
                quantity=args.quantity,
                stop_price=args.stop_price,
                limit_price=args.price
            )
    else:
        print(" Unsupported order type.")
