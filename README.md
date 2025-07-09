# Binance Futures Trading Bot 

A Python-based command-line trading bot that interfaces with the Binance **USDT-M Futures Testnet**.

---

## ✅ Features

- Place Market & Limit orders via CLI
- Bonus: Stop-Limit order support
- Environment-variable based API key handling
- Binance Testnet support
- Order logging (`bot.log`)

---

## 🛠 Installation

```bash
git clone https://github.com/your-username/binance-futures-trading-bot.git
cd binance-futures-trading-bot
pip install -r requirements.txt
```

---

## 📁 Project Structure

```
binance-futures-trading-bot/
│
├── .env.example            # Example for storing API credentials
├── bot.log                 # Generated log file (real or simulated)
├── README.md               # You're reading it
├── requirements.txt        # Required Python packages
├── .gitignore              # Files excluded from Git
└── src/
    ├── main.py             # CLI entry point
    ├── utils.py            # Binance client logic
    ├── market_orders.py    # Market orders
    ├── limit_orders.py     # Limit orders
    └── advanced/
        └── stop_limit.py   # (Bonus) Stop-limit orders
```

---

## 🔐 Setup API Keys

1. Copy `.env.example` → `.env`
2. Paste your Binance Futures **Testnet** API credentials:

```
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
```

⚠️ **Note:** Testnet API creation is currently unstable or restricted as of 2025. 

---

## 🚀 Usage

```bash
# Market Order
python src/main.py --symbol BTCUSDT --side BUY --type market --quantity 0.01

# Limit Order
python src/main.py --symbol BTCUSDT --side SELL --type limit --quantity 0.01 --price 108000

# Stop-Limit Order (Bonus)
python src/main.py --symbol BTCUSDT --side SELL --type stop-limit --quantity 0.01 --stop_price 107000 --price 106800
```

---

## 📝 Sample Log Output

```
2025-07-08 22:45:51,321 - INFO - Starting bot...
2025-07-08 22:45:51,876 - INFO - Attempting to place MARKET order...
```
---

## 📘 License

This project is for educational purposes only.

---

⭐ If this was helpful, give it a star on GitHub!
