import random


def get_random_state():
    """Get a random state from states.txt"""
    num_words_processed = 0
    curr_word = None
    with open('states.txt', 'r') as f:
        for word in f:
            word = word.strip().lower()
            num_words_processed += 1
            if random.randint(1, num_words_processed) == 1:
                curr_word = word
    return curr_word


name = input("Enter your name --> ")

print("Good Luck!", name.title())
state = str(get_random_state())

print("Guess the state")
guesses = ''
turns = 7

while turns > 0:
    # counts the number of times a user fails
    failed = 0
    for char in state:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You Win")
        print("The state is:", state)
        break

    guess = input("guess a character:")
    guess = guess.lower()
    if len(guess) != 1:
        print("Invalid Input")
    elif not (guess.isalpha()):
        print("Invalid Input")
    else:
        # every input character will be stored in guesses
        guesses += guess
        if guess not in state:
            turns -= 1
            print("Wrong")
            if turns == 0:
                print("You ran out of guesses")
            else:
                print("You have", + turns, 'more guesses')
            if turns == 0:
                print("Game Over")
                print("The state is:", state)
