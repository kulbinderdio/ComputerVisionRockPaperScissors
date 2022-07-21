

import random
import time
import cv2
from keras.models import load_model
import numpy as np



'''
Our Rock, Paper, Scissors class
'''
class rps:
    #List of valid options for game
    choices = ['rock','paper','scissors']

    computer_wins = 0
    user_wins = 0

    '''
    load model in constructor
    '''
    def __init__(self):
        self.model = load_model('keras_model.h5')



    '''
    Method to randomly select computer choice
    '''
    def get_computer_choice(self):
        return random.choice(self.choices)


    def test(self):
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = self.model.predict(data)
            cv2.imshow('frame', frame)
            # Press q to close the window
            print(prediction)




    def get_prediction(self, delay):


        start = time.time()
        current = time.time()

        while current - start < delay:
            print(round(abs(current-start-delay)))
            current = time.time()
            # ret, frame = cap.read()
            # resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            # image_np = np.array(resized_frame)
            # normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            # data[0] = normalized_image
            # cv2.imshow('frame', frame)

        prediction = self.model.predict(data)
        print(prediction)
        print(self.choices[np.argmax(prediction)])
        return self.choices[np.argmax(prediction)]

        

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
    def get_winner(self, computer_choice, user_choice):

        if computer_choice == user_choice:
            return "Draw"
        if computer_choice == 'rock' and user_choice =='paper':
            self.user_wins += 1
            return "User won"
        elif computer_choice == 'paper' and user_choice == 'scissors':
            self.user_wins += 1
            return "User won"
        elif computer_choice == 'scissors' and user_choice == 'rock':
            self.user_wins += 1
            return "User won"
        else:
            self.computer_wins += 1
            return "Computer won"

    def play(self):
        while self.computer_wins <3 and self.user_wins <3:
            computer_choice = game.get_computer_choice()
            user_choice = game.test()


            print(f"Computer choice : {computer_choice}   User choice : {user_choice}")
            print (game.get_winner(computer_choice,user_choice))
            print (f"Scores : Computer - {self.computer_wins}    User - {self.user_wins}")

game = rps()
game.test()

