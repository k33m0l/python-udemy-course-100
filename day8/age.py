max_age = 90
weeks_in_year = 52

def life_in_weeks(age):
    remaining_years = max_age - age
    remaining_weeks = remaining_years * weeks_in_year
    print(f"You have {remaining_weeks} weeks left.")
