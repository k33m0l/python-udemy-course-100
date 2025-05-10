import pandas
import matplotlib.pyplot as pyplot
import matplotlib.dates as mdates

df_testa = pandas.read_csv("tesla_search_vs_price.csv")
df_unemployment = pandas.read_csv("ue-2004-19.csv")
df_bitcoin_price = pandas.read_csv("daily_bitcoin_price.csv")
df_bitcoin_search = pandas.read_csv("bitcoin_search_trend.csv")

df_testa = df_testa.dropna()
df_unemployment = df_unemployment.dropna()
df_bitcoin_price = df_bitcoin_price.dropna()
df_bitcoin_search = df_bitcoin_search.dropna()

df_testa.MONTH = pandas.to_datetime(df_testa.MONTH)
df_unemployment.MONTH = pandas.to_datetime(df_unemployment.MONTH)
df_bitcoin_price.DATE = pandas.to_datetime(df_bitcoin_price.DATE)
df_bitcoin_search.MONTH = pandas.to_datetime(df_bitcoin_search.MONTH)
df_bitcoin_monthly = df_bitcoin_price.resample("ME", on="DATE").last()

pyplot.figure(figsize=(14,8), dpi=120)
pyplot.title("Tesla Search vs Price", fontsize=18)

axis1 = pyplot.gca()
axis2 = axis1.twinx()
axis1.set_ylabel("TSLA Stock Price", color="#E6232E", fontsize=14)
axis2.set_ylabel("Search Trend", color="skyblue", fontsize=14)
axis1.plot(df_testa.MONTH, df_testa.TSLA_USD_CLOSE, color="#E6232E", linewidth=3)
axis2.plot(df_testa.MONTH, df_testa.TSLA_WEB_SEARCH, color="skyblue", linewidth=3)

years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter("%Y")
axis1.xaxis.set_major_locator(years)
axis1.xaxis.set_major_formatter(years_fmt)
axis1.xaxis.set_minor_locator(months)

pyplot.show()

