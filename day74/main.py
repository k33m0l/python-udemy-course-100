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
themes_by_year = sets.groupby("year").agg({"theme_id": pandas.Series.nunique})
parts_per_set = sets.groupby("year").agg({"num_parts": pandas.Series.mean})

axis1 = pyplot.gca()
axis2 = axis1.twinx()

axis1.plot(sets_per_year.index[:-2], sets_per_year.set_num[:-2], color="g")
axis2.plot(themes_by_year.index[:-2], themes_by_year.theme_id[:-2], color="b")

axis1.set_xlabel("Year")
axis1.set_ylabel("Number of Sets", color="green")
axis2.set_ylabel("Number of Themes", color="blue")

pyplot.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])

pyplot.show()

