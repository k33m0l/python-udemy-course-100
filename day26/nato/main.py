import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato = {row.letter:row.code for (_, row) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def getUserInput():
    return input("Provide a word: ").upper()

def getNatoWord():
    try:
        return [nato[c] for c in getUserInput()]
    except KeyError:
        print("Sorry only letters in the ABC please.")
        return getNatoWord()

print(getNatoWord())
