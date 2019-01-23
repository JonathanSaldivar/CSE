import random
words = ['Rocks', 'Loan', 'Clock', 'Hangman', 'Mouse', 'Shoe', 'Avenue', 'Apartment', 'Sleeves', 'Genotype']
print(words)
letters_guess = 9
letters_guess_right = []
guesses_made = []
random_words = random.choice(words)
playing = True
while playing and letters_guess > 0:
    guess = input('Choose a letter')
    input()
