import yfinance as yf
stock = input("Enter stock symbol: ")
data = yf.Ticker(stock)
print("Current Price:", data.history(period="1d")["Close"].iloc[-1])
