import logging
from binance.exceptions import BinanceAPIException

def place_market_order(client, symbol, side, quantity):
    """
    Places a market order on Binance Futures.

    Args:
        client: Authenticated Binance client
        symbol (str): Trading pair (e.g., 'BTCUSDT')
        side (str): 'BUY' or 'SELL'
        quantity (float): Amount to trade

    Returns:
        dict: Order response from Binance
    """
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type='MARKET',
            quantity=quantity
        )
        logging.info(f"Market order placed: {order}")
        print(" Order successful!")
        print(order)
        return order

    except BinanceAPIException as e:
        logging.error(f"API error: {e}")
        print(" Binance API Error:", e.message)
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(" Unexpected error:", e)
