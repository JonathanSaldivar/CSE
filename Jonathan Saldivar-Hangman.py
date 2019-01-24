import random
words = ['rocks', 'loan', 'clock', 'hangman', 'mouse', 'shoe', 'avenue', 'apartment', 'sleeves', 'genotype']
print(words)
letters_guess = 9
letters_guess_right = []
guesses_made = []
input('Choose a letter')
random_words = random.choice(words)
playing = True
while guess > 0:
    guess = input('Choose a letter')
    input()
else guess < 0:
    output.end
letters_used = input('You have lost')
