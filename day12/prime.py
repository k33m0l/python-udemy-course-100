def is_divisible(num, divisor):
    return num % divisor == 0

def is_prime(num):
    count = 0
    for divisor in range(1, num + 1):
        if is_divisible(num, divisor):
            count += 1
    return count <= 2