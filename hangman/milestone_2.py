# %%
import random # import python random module
# creat list of favorite fruits
word_list = ["Apple", "Banana", "Orange", "Grapes", "Pear"]
print(word_list)
# select random fruit from list
word = random.choice(word_list)
print(word) # print random choice

# %%
# Ask user to enter a single character
user_guess = input('Enter a single letter')
print(user_guess) # print user's input

# validate user input
if len(user_guess) == 1 and user_guess.isalpha():
    print("Good guess")
else:
    print("Oops! That is not a valid input")
# %%
