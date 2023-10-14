# %%
word = "Apple"


# %%

# %%
def check_guess(guess):
    if guess.lower() in word.lower():
        print(f'Good guess! {guess} is in the word')
    else:
        print(f'Sorry, {guess} is not in the word. Try again')  


def ask_for_input():
    while 1 > 0: # Continous while loop to ensure that valid input is given
        guess = input("Enter a single letter: ")
        if len(guess) == 1 and guess.isalpha():
            print("Guess is valid")
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()

