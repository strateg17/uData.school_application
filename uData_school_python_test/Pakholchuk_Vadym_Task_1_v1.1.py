# Завдання №1.1 Пахольчук Вадим Володимрович

from random import shuffle

print("Hello!, ")
sentence = input("Please, print your sentence: ")

def scramble(sentence):
    split = sentence.split()  # Split the string into a list of words
    shuffle(split)  # This shuffles the list in-place.
    return ' '.join(split)  # Turn the list back into a string

print(scramble(sentence))