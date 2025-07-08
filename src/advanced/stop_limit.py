import logging
from binance.exceptions import BinanceAPIException

def place_stop_limit_order(client, symbol, side, quantity, stop_price, limit_price):
    """
    Places a Stop-Limit order on Binance Futures.

    Args:
        client: Authenticated Binance client
        symbol (str): Trading pair
        side (str): 'BUY' or 'SELL'
        quantity (float): Order quantity
        stop_price (float): Trigger price
        limit_price (float): Price for limit order

    Returns:
        dict: Order response from Binance
    """
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type='STOP_MARKET',
            stopPrice=str(stop_price),
            price=str(limit_price),
            quantity=quantity,
            timeInForce='GTC',
            workingType='MARK_PRICE'
        )
        logging.info(f"Stop-Limit order placed: {order}")
        print(" Stop-Limit order placed.")
        print(order)
        return order

    except BinanceAPIException as e:
        logging.error(f"API error: {e}")
        print(" Binance API Error:", e.message)
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(" Unexpected error:", e)
