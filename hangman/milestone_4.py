import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list) # The word to be guessed, picked randomly from the word_list
        self.word_guessed = ['_']*len(self.word) # A list of the letters of the word, with _ for each letter not yet guessed.
        self.num_letters = len(set(self.word)) # The number of UNIQUE letters in the word that have not been guessed yet
        self.num_lives = num_lives # The number of lives the player has at the start of the game.
        self.word_list = word_list #  A list of words
        self.list_of_guesses = [] #A list of the guesses that have already been tried. Set this to an empty list initially

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word.lower():
            print(f'Good guess! {guess} is in the word')
            for index, character  in enumerate(self.word):
                if character == guess:
                    self.word_guessed[index] = character
            self.num_letters -= 1       
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')

    def ask_for_input(self):
        while 1 > 0: # Continous while loop to ensure that valid input is given
            guess = input("Enter a single letter: ")
            if len(guess) == 1 and guess.isalpha():
                print("Guess is valid")
                break
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")
    
        self.check_guess(guess)
# test    
test = Hangman(["apple"],2)
test.ask_for_input()
print(test.word_guessed)

