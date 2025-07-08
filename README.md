# Binance Futures Trading Bot

A command-line crypto trading bot for Binance USDT-M Futures Testnet.

---

## ✅ Features

- Market Orders (Buy/Sell)
- Limit Orders (Buy/Sell)
- Stop-Limit Orders (Bonus)
- Logging of orders and errors
- Input validation
- CLI interface

---

## 📁 Folder Structure

```
binance_bot_project/
│
├── .env                # API keys (not committed)
├── bot.log             # Log file (generated during usage)
├── README.md
└── src/
    ├── main.py
    ├── utils.py
    ├── market_orders.py
    ├── limit_orders.py
    └── advanced/
        └── stop_limit.py
```

---

## ⚙️ Setup

### 1. Install Requirements

```bash
pip install python-binance python-dotenv
```

### 2. Create .env

```
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_api_secret
```

> Note: Due to Binance Futures Testnet limitations in mid-2025, obtaining valid testnet API keys may not be possible currently.

---

## 🚀 Usage

```bash
python src/main.py --symbol BTCUSDT --side BUY --type market --quantity 0.01
```

Other examples:
- Limit Order:
```bash
python src/main.py --symbol BTCUSDT --side SELL --type limit --quantity 0.01 --price 108000
```

- Stop-Limit Order:
```bash
python src/main.py --symbol BTCUSDT --side SELL --type stop-limit --quantity 0.01 --stop_price 107000 --price 106800
```

---

## 📓 Notes

Due to current issues with Binance Futures Testnet API access (deprecation of GitHub login and key restrictions), live trading via API may return:

```
Binance API Error: Server is busy, please try to request a moment later
```

This log has been simulated to demonstrate the bot’s structure and execution path.