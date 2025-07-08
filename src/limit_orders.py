import logging
from binance.exceptions import BinanceAPIException

def place_limit_order(client, symbol, side, quantity, price):
    """
    Places a limit order on Binance Futures.

    Args:
        client: Authenticated Binance client
        symbol (str): Trading pair (e.g., 'BTCUSDT')
        side (str): 'BUY' or 'SELL'
        quantity (float): Order amount
        price (float): Limit price

    Returns:
        dict: Order response
    """
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type='LIMIT',
            quantity=quantity,
            price=str(price),
            timeInForce='GTC'
        )
        logging.info(f"Limit order placed: {order}")
        print("Limit order placed.")
        print(order)
        return order

    except BinanceAPIException as e:
        logging.error(f"API error: {e}")
        print(" Binance API Error:", e.message)
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(" Unexpected error:", e)
