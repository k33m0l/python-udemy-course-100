WORD_SPACE = 3
CHAR_SPACE = 1


morse_code = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}

def is_not_end(index, length):
    return not index == (length - 1)

def find_by_value(value):
    for key, val in morse_code.items():
        if val == value:
            return key
    raise KeyError()

def decode(input):
    words = input.split(" " * WORD_SPACE)
    result = ""
    for i in range(len(words)):
        chars = words[i].split(" " * CHAR_SPACE)
        for char in chars:
            decoded_char = find_by_value(char)
            result += decoded_char
        if is_not_end(i, len(words)):
            result += " "
    return result

def encode(input):
    words = input.split(" ")
    result = ""
    for i in range(len(words)):
        for char_index in range(len(words[i])):
            try:
                result += morse_code[words[i][char_index]]
                if is_not_end(char_index, len(words[i])): 
                    result += " " * CHAR_SPACE
            except KeyError:
                pass
        if is_not_end(i, len(words)):
            result += " " * WORD_SPACE
    return result

working = True
while working:
    user_mode = input("Select mode: (encode, decode, quit)\n")
    if user_mode == "encode":
        text = input("Type your text to be encoded: ")
        print(encode(text.upper()))
    elif user_mode == "decode":
        text = input("Type your morse code: ")
        try:
            print(decode(text))
        except KeyError:
            print("Incorrect morse code detected")
    elif user_mode == "quit":
        working = False
        print("Quiting")
    else:
        print(f"{user_mode} operation mode not available.")

