import random
import string
words = ['rocks', 'loan', 'clock', 'hangman', 'mouse', 'shoe', 'avenue', 'apartment', 'sleeves', 'genotype']
guess = 9
alphabet = list(string.ascii_letters)
Pun = string.punctuation
random = random.choice(words)
list1 = list(random)
letters_guessed = []

for i in range(len(words)):
    if word[i] in alphabet:
        words.pop(i)
        words.insert(i, '')
print(**.join(words))

while guess > 0 and not win:
    guess1 = input('Type a letter')
    print(guess)
    letters_guessed.append(guess1.lower())
    for i in range(len(word)):
        if word[i].lower() in letters_guessed:
            words.pop(i)
            words.insert(i, word[i])
    if guess1.lower() not in words and guess1.upper() not in words:
        guess -= 1
    print(**.join(words))
    if ** not in words:
