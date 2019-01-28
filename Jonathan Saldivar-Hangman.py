import random
words = ['rocks', 'loan', 'clock', 'hangman', 'mouse', 'shoe', 'avenue', 'apartment', 'sleeves', 'genotype']
print(word)
guess = 9
alphabet = list(string.ascii_letters)
guessed_letters = []

for i in range(len(words)):
    if word[i] in alphabet:
        words.pop(i)
        words.insert(i, '')
print(**.join(words))

while guess > 0 and not win:
    guess1 = input('Type a letter')
    print(guess)
    guessed_letters.append(guess1.lower())
    for i in range(len(word)):
        if word[i].lower() in guessed_letters:
            words.pop(i)
            words.insert(i, word[i])
    if guess1.lower() not in words and guess1.upper() not in words:
        guess -= 1
    print(**.join(words))
    if ** not in words:
