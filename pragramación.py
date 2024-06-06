#PC va a elegir una palabra y mostrar guiones al jugador que significa la cantidad de letras que hay en la palabra
from random import choice

def chooseWord():
    words = ["monkey", "tiger", "bear", "snake", "shark"]
    word_chosen = choice(words)
    return word_chosen

def totalLetters(word_chosen):
    letters = list()
    for i in word_chosen:
        letters.append(i)
    return len(letters)

def showWord(total):
    return "_" * total


selected_word = chooseWord()
total = totalLetters(selected_word)
print(showWord(total))

chances = 6
while chances > 0:
    chances -= 1
    selected_letter = str(input("Choose a letter: ")).lower()
    #comparar a letra com a palabra
    for i in selected_word:
        if i == selected_letter:
            print(i, end='')
        else:
            print("_", end='')