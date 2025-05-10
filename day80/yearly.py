import pandas
import matplotlib.pyplot as plt
import plotly.express as px

df_yearly = pandas.read_csv("annual_deaths_by_clinic.csv")
df_mothly = pandas.read_csv("monthly_deaths.csv")

prob = df_yearly.deaths.sum() / df_yearly.births.sum() * 100
print(prob)

df_yearly["pct_deaths"] = df_yearly.deaths / df_yearly.births
clinic1 = df_yearly[df_yearly.clinic == "clinic 1"]
avg_c1 = clinic1.deaths.sum() / clinic1.births.sum() * 100
clinic2 = df_yearly[df_yearly.clinic == "clinic 2"]
avg_c2 = clinic2.deaths.sum() / clinic2.births.sum() * 100

#line = px.line(
#    df_yearly,
#    x="year",
#    y="pct_deaths",
#    color="clinic",
#    title="Yearly deaths by clinic",
#)
#line.show()
handwashing_start = "1846"
df_mothly["pct_deaths"] = df_mothly.deaths/df_mothly.births
before_washing = df_mothly[df_mothly.date <handwashing_start]
after_washing = df_mothly[df_mothly.date >= handwashing_start]

bw_rate = before_washing.deaths.sum() / before_washing.births.sum() * 100
aw_rate = after_washing.deaths.sum() / after_washing.births.sum() * 100

roll_df = before_washing.set_index("date")
roll_df = roll_df.rolling(window=6).mean()

plt.figure(figsize=(14,8), dpi=200)
plt.title("Percentage of Monthly Deaths over Time", fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
plt.ylabel("Percentage of Deaths", color="crimson", fontsize=18)

axis = plt.gca()
axis.set_xlim([df_mothly.date.min(), df_mothly.date.max()])

av_line = plt.plot(
    roll_df.index,
    roll_df.pct_deaths,
    color="crimson",
    linewidth=3,
    linestyle="--",
    label="6m Moving Average",
)
bw_line = plt.plot(
    before_washing.date,
    before_washing.pct_deaths,
    color="skyblue",
    linewidth=3,
    marker="o",
    label="Before handwashing",
)
aw_line = plt.plot(
    after_washing.date,
    after_washing.pct_deaths,
    color="skyblue",
    linewidth=3,
    marker="o",
    label="After handwashing",
)

plt.show()

