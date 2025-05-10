import pandas
import matplotlib.pyplot as pyplot
import plotly.express as px

df_apps = pandas.read_csv("apps.csv")
df_apps.drop(["Last_Updated", "Android_Ver"], axis=1, inplace=True)
df_apps.dropna(inplace=True)
df_apps.drop_duplicates(inplace=True)

ratings = df_apps.Content_Rating.value_counts()
df_apps.Installs = df_apps.Installs.astype(str).str.replace(",", "")
df_apps.Installs = pandas.to_numeric(df_apps.Installs)
df_apps.Price = df_apps.Price.astype(str).str.replace("$", "")
df_apps.Price = pandas.to_numeric(df_apps.Price)
df_apps = df_apps[df_apps["Price"] < 250]

df_apps["Revenue_Estimate"] = df_apps.Installs.mul(df_apps.Price)
top10_cat = df_apps.Category.value_counts()[:10]
cat_installs = df_apps.groupby("Category").agg({"Installs":pandas.Series.sum})
cat_installs.sort_values("Installs", ascending=True, inplace=True)

bar = px.bar(
    x=cat_installs.Installs,
    y=cat_installs.index,
    orientation="h",
    title="Category Popularity",
)
bar.update_layout(
    xaxis_title="Number of Downloads",
    yaxis_title="Category",
)

bar.show()

