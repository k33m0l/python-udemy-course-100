import pandas
import matplotlib.pyplot as pyplot
import plotly.express as px

df_apps = pandas.read_csv("apps.csv")
df_apps.drop(["Last_Updated", "Android_Ver"], axis=1, inplace=True)
df_apps.dropna(inplace=True)
df_apps.drop_duplicates(inplace=True)

ratings = df_apps.Content_Rating.value_counts()

fig = px.pie(
    labels=ratings.index,
    values=ratings.values,
    title="Content Rating",
    names=ratings.index,
    hole=0.6,
)
fig.update_traces(textposition="outside", textfont_size=15, textinfo="percent")
fig.show()

