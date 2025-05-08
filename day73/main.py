import pandas
import matplotlib.pyplot as pyplot

data = pandas.read_csv("QueryResults.csv", names=["DATE", "TAG", "POSTS"], header=0)
posts_per_lang = data.groupby("TAG").sum()
months_per_lang = data.groupby("TAG").count()

# Convert to datetime
data.DATE = pandas.to_datetime(data.DATE)

pivoted_data = data.pivot(index="DATE", columns="TAG", values="POSTS")
pivoted_data.fillna(0, inplace=True)
rolling_data = pivoted_data.rolling(window=6).mean()

pyplot.xlabel("Date", fontsize=14)
pyplot.ylabel("Number of Posts", fontsize=14)
pyplot.ylim(0, 35000)
for lang in pivoted_data.columns:
    pyplot.plot(pivoted_data.index, pivoted_data[lang], linewidth=3, label=pivoted_data[lang].name)

pyplot.legend(fontsize=16)
pyplot.show()
