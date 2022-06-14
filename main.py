
import pandas
data=pandas.read_csv('nato_phonetic_alphabet.csv')
# print(data)
result={row.letter:row.code for (index,row) in data.iterrows()}
# print(result)
inp=input("Enter a world \n").upper()
output=[result[letter] for letter in inp]
print(output)