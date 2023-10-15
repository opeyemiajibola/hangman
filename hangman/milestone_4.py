import random

class Hangman:
    '''
    This class is used to represent the Hangman game.

    Attributes:
        word (string): the word to be guessed.
        word_guessed (list): A list of the letters of the word.
        num_letters (int): The number of UNIQUE letters in the word that have not been guessed yet.
        num_lives (int): The number of lives the player has at the start of the game.
        word_list (list): A list of words
        list_of_guesses (list): A list of the guesses that have already been tried
    '''
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list) # The word to be guessed, picked randomly from the word_list
        self.word_guessed = ['_']*len(self.word) # A list of the letters of the word, with _ for each letter not yet guessed.
        self.num_letters = len(set(self.word)) # The number of UNIQUE letters in the word that have not been guessed yet
        self.num_lives = num_lives # The number of lives the player has at the start of the game.
        self.word_list = word_list #  A list of words
        self.list_of_guesses = [] #A list of the guesses that have already been tried. Set this to an empty list initially

    def check_guess(self, guess):
        """
        This function validates the character guessed by a user

        The purpose of this function is to valiadate the character guessed by a user
        After a suceesful validation, the function updates the word_guessed list and the number of pending letters to be guessed to complete the word.
        Afer a failed validation, the function decrements user's number of lives
        
        """
        guess = guess.lower()
        if guess in self.word.lower():
            print(f'Good guess! {guess} is in the word')
            # check for index of guessed character in word and update word_guessed and num_letters to be guessed
            for index, character  in enumerate(self.word):
                if character == guess:
                    self.word_guessed[index] = character # update word_guessed
            self.num_letters -= 1 # decrement num_letters to be guessed      
        else:
            self.num_lives -= 1 # decrement user's num_lives
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')

    def ask_for_input(self):
        """
        This function ask users for an input character 

        The purpose of this function is to collect an input character from the user.
        The function continously request for an input character until the user enters a valid input.
        
        """

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

