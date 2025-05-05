import pandas
data = pandas.read_csv("salaries_by_college_major.csv")
clean_data = data.dropna()

start_med_salary_row = clean_data["Starting Median Salary"].idxmax()
start_med_salary_major = clean_data["Undergraduate Major"].loc[start_med_salary_row]
print(f"Best startin major: {start_med_salary_major}")

mid_car_salary_row = clean_data["Mid-Career Median Salary"].idxmax()
mid_car_salary_major = clean_data["Undergraduate Major"][mid_car_salary_row]
print(f"Best Mid-Career major {mid_car_salary_major}")
print(f"Median salary expectations: {clean_data["Mid-Career Median Salary"][mid_car_salary_row]}")

start_lowest_salary_row = clean_data["Starting Median Salary"].idxmin()
start_lowest_salary_major = clean_data["Undergraduate Major"][start_lowest_salary_row]
print(f"Worst starting major {start_lowest_salary_major}")
print(f"Salary expectations: {clean_data["Starting Median Salary"][start_lowest_salary_row]}")

mid_lowest_salary_row = clean_data["Mid-Career Median Salary"].idxmin()
mid_lowest_salary_major = clean_data["Undergraduate Major"][mid_lowest_salary_row]
print(f"Worst Mid-Career major: {mid_lowest_salary_major}")
print(f"Salary expectations: {clean_data["Mid-Career Median Salary"][mid_lowest_salary_row]}")




risk_spread = clean_data["Mid-Career 90th Percentile Salary"] - clean_data["Mid-Career 10th Percentile Salary"]
clean_data.insert(1, "Spread", risk_spread)

highest_potential = clean_data.sort_values("Mid-Career 90th Percentile Salary", ascending=False)
print(highest_potential[["Undergraduate Major", "Mid-Career 90th Percentile Salary"]].head())

decreasing_risk = clean_data.sort_values("Spread", ascending=False)
print(decreasing_risk[["Undergraduate Major", "Spread"]].head())

