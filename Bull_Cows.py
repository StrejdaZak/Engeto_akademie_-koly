"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Michal Krhut
email: michal.k.ppc@gmail.com
discord: Michal K.#3398
"""
import random

number = []
attempts = 0
rating = ""
pause = "-" * 45
playing_again = False

def NumberMaker():
    """
    Tato funkce slouží pro vytvoření náhodného čísla
    Opakuje se tak dlouho, dokud nevytvoří 4 unikátní čísla v řadě, přičemž první nesmí být 0.
    """
    for i in range(4):
        num = random.randrange(0, 9)
        number.append(num)
    if len(number) > len(set(number)) or number[0] == 0:
        number.clear()
        NumberMaker()

def performance():
    """
    Tato funkce slouží k vyhodnocení úspěšnosti hráče po dokončení hry.

    """
    global attempts, rating
    if attempts > 25:
        rating = "pretty bad!"
    elif attempts > 20:
        rating = "not good."
    elif attempts > 15:
        rating = "quite average!" 
    elif attempts > 10:
        rating = "really good!"
    elif attempts > 1:
        rating = "Amazing!"
    else:
        rating = "unbelievable! Your wits are unmatched. All heil the king of Bulls and Cows!"
    return rating

def quess_check(quess):
    """
    Tato funkce kontroluje správnost hádaného čísla.
    Tip musí být číslo o 4 znacích. 
    Žádné číslo se nesmí opakovat.
    První číslo nesmí být 0.
    """
    check = False
    while check is False:
        if not str.isdigit(quess):
            print("Nezadali jste číslo.")
            quess = input("Enter a number: ")
        elif len(quess) != 4:
            print("Nezadali jste 4 čísla")
            quess = input("Enter a number: ")
        elif quess[0] == "0":
            print("První číslo nesmí být 0. Zkuste jiné číslo.")
            quess = input("Enter a number: ")
        else:
            check = True
            break
    same_num = False
    for i in range(4):
        for j in range(4):
            if quess[i] == quess[j] and i != j:
                same_num = True
                break
        if same_num:
            break
    if same_num:
        print("Čísla se nesmí opakovat.")
        quess = input("Enter a number: ")
        quess_check(quess)
    else:
        return quess

def Playing():
    """
    Tato funkce obsahuje samotnou hru:
    a) Načte hádané číslo a tip hráče
    b) Zkontroluje správnost zadaného tipu hráče
    c) Vyhodnotí výsledek
    d) Pokud hráč dokončí hru, vyhodnotí ji
    e) Nabídne pokračování, případně se ukončí
    """
    global attempts, playing_again
    attempts += 1
    cows = 0
    bulls = 0
    print(attempts)
    while attempts == 1:
        quess = input("Enter a number: ")
        quess = quess_check(quess)
        break
    else:
        quess = input(">>> ")
        quess = quess_check(quess)
    result = [int(quess[i]) for i in range(4)]
    for i in range(4):
        for j in range(4):
            if result[i] == number[j]:
                cows += 1
    for k in range(4):
        if result[k] == number[k]:
            bulls += 1
    if bulls == 4:
        print(f"Correct, you've guessed the right number in {attempts} guesses!")
        print(pause)
        performance()
        print(f"That´s {rating}")
        print(pause)
        playing_again = (input("Do you want to play again? Y/N: "))
        if playing_again == "Y":
            NumberMaker()
            attempts = 0
            Playing()
        else:
            print("Thank you for playing Bulls and Cows. Have a great day!")
            quit()
    else:
        print(f"{bulls} bulls, {cows - bulls} cows\n" + pause)
        Playing()


NumberMaker() #vytvoříme hádané číslo

welcome_message = f"""
Hi there!
{pause}
I've generated a random 4-digit number for you.
Let's play a bulls and cows game.
{pause}
"""

print(welcome_message)

Playing() #spouštíme hru
