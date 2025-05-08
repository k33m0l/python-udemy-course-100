import pandas
import matplotlib.pyplot as pyplot

colors = pandas.read_csv("data/colors.csv")
print(f"LEGO can produce {colors["name"].unique().size} unique colors!")
print(f"LEGO can produce {colors.is_trans.value_counts()["t"]} transparent colors!")

sets = pandas.read_csv("data/sets.csv").sort_values("year")
sorted_sets = sets.sort_values("year")
print(f"LEGO released {sorted_sets[sorted_sets["year"] == 1949]} sets in their first year")
print(f"LEGO sets with the most number of parts are: {sorted_sets.sort_values("num_parts", ascending=False).head()}")

sets_per_year = sets.groupby("year").count()
# pyplot.plot(sets_per_year.index[:-2], sets_per_year.set_num[:-2])
# pyplot.show()

themes_by_year = sets.groupby("year").agg({"theme_id": pandas.Series.nunique})
pyplot.plot(themes_by_year.index[:-2], themes_by_year.theme_id[:-2])
pyplot.show()
