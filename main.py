student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()} #iterate through each of the rows

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_data = {row.letter:row.code for (index, row) in data.iterrows()}
#print(new_data)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    ask_name = input("Enter a name: ").upper()
    try:
        code_list = [new_data[letter] for letter in ask_name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(code_list)

generate_phonetic()
