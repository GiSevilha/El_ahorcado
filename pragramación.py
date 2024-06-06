#PC va a elegir una palabra y mostrar guiones al jugador que significa la cantidad de letras que hay en la palabra
from random import choice

def chooseWord():
    words = ["monkey", "tiger", "bear", "snake", "shark"]
    word_chosen = choice(words).capitalize()
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