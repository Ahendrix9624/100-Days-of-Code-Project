# # FileNotFound
# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "Value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message}does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error i made up")

###################################################

# #Raising your own exception
# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Human height should not be over 3 meters")

# bmi = weight / height ** 260
# print(bmi)

###################################################

fruits = ["Apple", "Pear", "Orange"]

# # #TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#         print(fruit + " pie")
#     except IndexError:
#         print(fruits[0] + " pie")
#     else:
#         print(fruit + " pie")


# make_pie(9)

################################################### 

# Key Error handling 
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2}, 
#     {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
#     {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
#     {'Comments': 4, 'Shares': 2}, 
#     {'Comments': 1, 'Shares': 1}, 
#     {'Likes': 19, 'Comments': 3}
# ]

# total_likes = 0

# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         pass

# print(total_likes)

################################################### 

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only a letters in the alphabet.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()