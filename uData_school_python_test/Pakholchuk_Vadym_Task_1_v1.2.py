# Завдання №1/2 Пахольчук Вадим Володимрович

"""Sentence input block"""

print("Hello!, ")
sentence = input("Please, print your sentence: ")

"""Program block"""
split = sentence.split()         # Split the string into a list of words
sentence = split[1:]             # Delete first element
sentence.append(split[0])        # Append the list with the first element from the end
sentence = ' '.join(sentence)    # Create a sting from the list (join the elements)

"""Output block"""
print(sentence)