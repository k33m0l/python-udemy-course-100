from nutritionix import call_api, interpret
from sheety import add_workout

user_input = input("What sort of excercise did you do today?\n")

api_response = call_api(user_input)
interpreted_response = interpret(api_response)
add_workout(interpreted_response)