"""
Textovy_analyzator.py: první projekt do Engeto Online Python Akademie

author: Michal Krhut
email: michal.k.ppc@gmail.com
discord: PMichal K.#3398
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

registered_users = {
        "bob": "123",
        "ann": "pass123",
        "mike": "password123",
        "liz": "pass123"
    }

#Ověření přihlašovacích údajů
username = input("Zadejte přihlašovací jméno: ")
password = input("Zadejte heslo: ")

if username not in registered_users:
    print(f"""
    username: {username}
    password: {password}
    unregistered user, terminating the program..
    """)
    quit()
elif registered_users[username] not in password:
    print(f"""
    username: {username}
    password: {password}
    unregistered user, terminating the program..
    """)
    quit()  
else:
    print("Vítejte, {}!".format(username))
    pass


#Výběr textu, který budeme analyzovat
text_choise = input("Který z textů chcete analyzovat? Zadejte číslo 1 až 3: ")
if not str.isdigit(text_choise):
    print("Nezadali jste číslo.")
    quit()
if int(text_choise) not in range(1,4):
    print("Nezadali jste číslo v rozmezí 1-3")
    quit()
else:
    print(f"Budeme analyzovat tento text:\n\n{TEXTS[int(text_choise)-1]}")
    pass

#Převedení vybraného textu na seznam slov
choosen_text = TEXTS[int(text_choise)-1]
words_list = choosen_text.split()

#Počet slov
words_count = len(words_list)

#Počet slov s velkým prvním písmenem
first_capital_letter_words = len([word for word in words_list if word.istitle()])

#Počet slov, napsaných kapitálkami
uppercase_words_count = len([word for word in words_list if word.isupper()])

#Počet slov, napsaných malými písmeny
lowercase_words_count = len([word for word in words_list if word.islower()])

#Počet čísel
numeric_strings_count = len([word for word in words_list if word.isnumeric()])

#Suma všech čísel v textu
numbers_sum = sum([int(word) for word in words_list if word.isnumeric()])


# Frekvence různých délek slov
word_lengths = [len(word) for word in words_list]
length_frequency = {}
for length in word_lengths:
    length_frequency[length] = length_frequency.get(length, 0) + 1

# Zobrazení výsledků 
print("----------------------------------------")
print("There are", words_count, "words in the selected text.")
print("There are", first_capital_letter_words, "titlecase words.")
print("There are", uppercase_words_count, "uppercase words.")
print("There are", lowercase_words_count, "lowercase words.")
print("There are", numeric_strings_count, "numeric strings.")
print("The sum of all the numbers is", numbers_sum)
print("----------------------------------------")
print("LEN|  OCCURRENCES  |NR.")
print("----------------------------------------")
for length, count in length_frequency.items():
    print(f"{length:3}|{'*' * count:16}|{count:3}")