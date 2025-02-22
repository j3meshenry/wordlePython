'''

File Name: wordle.py

Author(s): James Henry and Sophie Eichmann

Functionality: I made a wordle replica in python, using functions. While it's an old project, I did think it 
was a great way to showcase how to use text in different colors and functions. 

Note: This project was my first big coding project in college, and I do think it taught me the basics 
of python for programmers. It also taught me how to program in a team setting, so I hope you enjoy it. 

'''

import random

# ANSI escape codes for colors (reference: https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007 )
GREEN = "\033[0;32;48m"
YELLOW = "\033[0;33;48m"
LIGHT_GREEN = "\033[1;32;48m"  
RESET = "\033[0m"

# my list of words, can be modified to anything 
word_list = ["chick", "crime", "drive", "pains", "final"]

# Global variables to track wins and games
total_games = 0
total_wins = 0

#created check to check the user input and its length 
def check():
    user_input = input("Enter a 5-letter word: ").lower()
    if len(user_input) != 5:
        print("\033[0;31;48mLength of input is not 5 letters\033[0m")
        return check()
    return user_input

def eval(wordle, user_input):
    colored_output = ""

    for i, letter in enumerate(user_input):
        if letter == wordle[i]:  # Correct letter & position
            colored_output += GREEN + letter + RESET
        elif letter in wordle:  # Correct letter but wrong position
            colored_output += YELLOW + letter + RESET
        else:  # Incorrect letter
            colored_output += letter
    
    print(colored_output)

def play_game():
    global total_games, total_wins  # Use global variables to track games and wins
    wordle = random.choice(word_list)
    guesses = 5
    win = False
    total_games += 1
    
    while guesses > 0:
        user_input = check()
        eval(wordle, user_input)
        
        if user_input == wordle:
            print(LIGHT_GREEN + "Congratulations, you've guessed the word!" + RESET)
            win = True
            total_wins += 1
            break
        
        guesses -= 1
        if guesses == 0:
            print(f"Sorry, you've run out of guesses. The word was {wordle}.")
    
    # Win to game ratio
    if total_games > 0:
        win_percentage = (total_wins / total_games) * 100
    else:
        win_percentage = 0
    print(LIGHT_GREEN + f"Win to game ratio {win_percentage:.0f}%" + RESET)
    
    # Ask to play again
    play_again = input(LIGHT_GREEN + "Play again? (Y/N) " + RESET).lower()
    if play_again == 'y':
        return play_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
