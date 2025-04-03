import random

data = {
    "Budapest Hotel": 110000,
    "AFL": 1500000,
    "Six Nations": 135000,
    "The Wire": 450000,
    "Santorini": 1000000,
    "Brazil": 673000
}

def find_unique_random(comparable):
    result = random.choice(list(data))
    if result == comparable:
        return find_unique_random(comparable)
    return result

def get_user_answer(comparable_a, comparable_b):
    user_answer = input(f"Do you think A: '{comparable_a}' or B: '{comparable_b}' is more popular?").upper()
    if (user_answer != "A" and user_answer != "B"):
        return get_user_answer(comparable_a, comparable_b)
    return user_answer

def get_solution(comparable_a, comparable_b):
    popularity_a = data[comparable_a]
    popularity_b = data[comparable_b]
    if popularity_a > popularity_b:
        return "A"
    elif popularity_b > popularity_a:
        return "B"
    else:
        raise Exception("The popularity of A and B was the same, ensure data integrity!")

game_on = True
while game_on:
    comparable_a = find_unique_random("")
    comparable_b = find_unique_random(comparable_a)
    
    user_answer = get_user_answer(comparable_a, comparable_b)
    answer = get_solution(comparable_a, comparable_b)

    if user_answer == answer:
        print("Congraulations!")
    else:
        print("Wrong answer!")
        game_on = False