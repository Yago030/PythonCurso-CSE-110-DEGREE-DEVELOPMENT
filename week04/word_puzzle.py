"""
Author: Santiago Bergerat

Task: Word Puzzle

Enhancement: 
- The secret word is now chosen randomly from a predefined list.
"""


import random

word_list = ["apple", "banana", "cherry", "grape", "mango", "orange", "peach", "melon"]

word_secret = random.choice(word_list)

length = len(word_secret)


print("Welcome to the word guessing game!\n")

print("\nYour word is:", "_ " * length, "\n")

attempts = 0

while True:
    
    guess = input("Enter your guess: ").lower()
    attempts += 1
    

    if len(guess) != len(word_secret):
        print("Sorry, the guess must have the same number of letters as the secret word. Try again.")
        continue
    
    
    hint = ""
    
    
    for i in range(length):
        if guess[i] == word_secret[i]:
            hint += guess[i].upper()
        elif guess[i] in word_secret:
            hint += guess[i].lower()
        else: 
            hint += "_"
    
    
    print("Your hint is:", " ".join(hint))
        
        
    if guess == word_secret:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break

