def calculate_score(name, scoring_letters):
    score = 0
    for letter in scoring_letters:
        score += name.count(letter)
    return score

scoring_letters_1 = ['t', 'r', 'u', 'e']
scoring_letters_2 = ['l', 'o', 'v', 'e']

def calculate_love_score(name1, name2):
    first_score = calculate_score(name1, scoring_letters_1) + calculate_score(name2, scoring_letters_1)
    second_score = calculate_score(name1, scoring_letters_2) + calculate_score(name2, scoring_letters_2)
    return int(str(first_score) + str(second_score))
