def readNumbers(file_name):
    numbers = []
    with open(file_name) as file1:
        for line in file1:
            numbers.append(line)
    return [int(n) for n in numbers]

file1_numbers = readNumbers("file1.txt")
file2_numbers = readNumbers("file2.txt")

result = [n for n in file1_numbers if n in file2_numbers]
print(result)