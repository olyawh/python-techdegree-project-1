"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """
    """
    # write your code inside this function.
print('''
Welcome to the Number Guessing Game!
Have fun!
''')

  
number_of_tries = 0
true_number = random.randint(1, 10)
 
while True: 
   
    try:
        player_answer = int(input('Please choose a number between 1 and 10: '))
        if player_answer > 10 or player_answer < 0:
            raise ValueError("Please pick a number between 1 and 10")
    except ValueError as err:
        print("Please try again.")
        print("({})".format(err))  
    else:
        number_of_tries += 1
        if player_answer > true_number: 
            print('The number is too high, try again')
        elif player_answer < true_number: 
            print('The number is too low, try again') 
        else: 
            print('You win! It took you ', number_of_tries, ' attempt(s) to guess the number') 
            highest_score = 9
            if highest_score < number_of_tries:
                print('Highest score is ', highest_score)
            else:
                print('Highest score is ' , number_of_tries)    
            play_more = input('Would you like to play again? Type "yes" if so: ')
            if play_more.lower() == "yes":
                number_of_tries = number_of_tries - number_of_tries
                continue
            else:
                break    


print('Bye for now. Come back again')

if __name__ == '__main__':
   
    start_game()
