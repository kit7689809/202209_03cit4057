import matplotlib.pyplot as plt
import yfinance as yf

start = "2015-01-01"
end = "2022-12-15"
stock_name = "Tecent"
stock_ticker = "0700.HK"

stock = yf.download(stock_ticker, start, end)
stock["MA50"] = stock["Open"].rolling(50).mean()
stock["MA250"] = stock["Open"].rolling(250).mean()
stock["Open"].plot(
    figsize = (15,7),
    title=stock_name,
    ylabel="Price"
    )
stock["MA50"].plot(legend=True)
stock["MA250"].plot(legend=True)
plt.savefig("graph.pdf")
stock.to_csv("graph.csv")
stock.to_json("graph.json")  