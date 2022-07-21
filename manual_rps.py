

import random

'''
Our Rock, Paper, Scissors class
'''
class rps:
    #List of valid options for game
    choices = ['rock','paper','scissors']

    '''
    Method to randomly select computer choice
    '''
    def get_computer_choice(self):
        return random.choice(self.choices)


    '''
    Method to accept user choice, with error checking
    '''
    def get_user_choice(self):
        while True:
            selection = input ("select rock, paper or scissors: ")
            if selection.lower() in self.choices:
                return selection.lower()
            else:
                print("Invalid choice ")


    '''
    Method to determine winner of game
    '''
    def determine_winner(self, computer_choice, user_choice):

        if computer_choice == user_choice:
            return "Draw"
        if computer_choice == 'rock' and user_choice =='paper':
            return "User won"
        elif computer_choice == 'paper' and user_choice == 'scissors':
            return "User won"
        elif computer_choice == 'scissors' and user_choice == 'rock':
            return "User won"
        else:
            return "Computer won"


game = rps()

computer_choice = game.get_computer_choice()
user_choice = game.get_user_choice()

print(f"Computer choice : {computer_choice}   User choice : {user_choice}")
print (game.determine_winner(computer_choice,user_choice))
