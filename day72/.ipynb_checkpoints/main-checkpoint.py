import pandas
data = pandas.read_csv("salaries_by_college_major.csv")
clean_data = data.dropna()
resp = clean_data.tail()
print(resp)
