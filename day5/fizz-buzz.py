algorithm = {
    3: "Fizz",
    5: "Buzz"
}

def fizz_buzz(number):
    answer = ""
    for key in algorithm:
        if number % key == 0:
            answer += algorithm[key]
    return answer

for number in range(1, 101):
    result = fizz_buzz(number)
    if result == "":
        print(number)
    else:
        print(result)