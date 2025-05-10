import pandas
import matplotlib.pyplot as plt

df_yearly = pandas.read_csv("annual_deaths_by_clinic.csv")
df_mothly = pandas.read_csv("monthly_deaths.csv")

prob = df_yearly.deaths.sum() / df_yearly.births.sum() * 100
print(prob)

plt.figure(figsize=(14,8), dpi=200)
plt.title("Total number of Monthly Birts and Deaths", fontsize=18)

axis1 = plt.gca()
axis2 = axis1.twinx()

axis1.grid(color="grey", linestyle="--")

axis1.plot(
    df_mothly.date,
    df_mothly.births,
    color="skyblue",
    linewidth=3,
)
axis2.plot(
    df_mothly.date,
    df_mothly.deaths,
    color="crimson",
    linewidth=2,
    linestyle="--",
)

plt.show()

