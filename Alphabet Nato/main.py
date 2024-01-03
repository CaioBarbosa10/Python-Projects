import pandas


data = pandas.read_csv("./nato_phonetic_alphabet.csv")
# print(data)
df = pandas.DataFrame(data)
# print(df)

nato_dict = {row.letter: row.code for (index ,row ) in df.iterrows() }
#print(nato_dict)

def generate_phonetic():
    word = input("Enter with a word:").upper()
    try:
        output_list = [nato_dict[letter] for letter in word]

    except KeyError:
        print("Sorry only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
