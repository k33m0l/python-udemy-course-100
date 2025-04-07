import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato = {row.letter:row.code for (_, row) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
print([nato[c] for c in input("Provide a word: ").upper()])
