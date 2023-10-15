# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

The user has limited attempt to guess the alphabetical characters of the word selected by the computer. 

If a user is unable to guess the selected word before permitted number of failures is reached, the user loses the game. Otherwise, the user wins the game.

## Usage instructions
To play the Hangman game, enter **"play_game(word_list)"** where ***word_list*** is a list of words from which a random word is selected for every play of the Hangman game.

Below are the usage instructions for each play of the Hangman game
- Step 1: User provides a guessed character to the application.
- Step 2: Application validate the entered character.
- Step 3: Application confirms if entered character is present in the selected word. If character is present, application decrements number of pending characters. Otherwise, user looses a live and is allowed another attempt if live limit has not been reached. 
- Step 4: Steps 1 to Step 3 is repeated until the user loses or wins. 