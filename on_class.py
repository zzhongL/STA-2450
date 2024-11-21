#import random library to generate a random number between 1~1000
from random import randint
#GuessNumberGame Class
class GuessNumberGame:
    #initialize GuessNumberGame Class
    def __init__(self, attempts=20):
        #initialization target number,generate from 0 ~ 1000 by randint function
        self.target_number = randint(0, 1000)
        #initialization number
        self.attempts = attempts
        #initialization guess number to 1
        self.current_attempt = 1
        #set a Bool variable to ture while the game is running
        self.game_active = True
    #start game function
    def start_game(self):
        print(f"Please guess an integer between 0 and 1000. You have {self.attempts} chances.")
        #keep running function while game_active is true and attempts to do not over 20
        while self.game_active and self.current_attempt <= self.attempts:
            self.play_round()
        #output fail information if attempts over 20 times
        if self.game_active:
            print(f"Game Over! The correct number was: {self.target_number}.")
    #play_round function
    def play_round(self):
        try:
            #set attempt times
            guess = int(input(f"Attempt {self.current_attempt}: Please give a guess: "))
            #output error message if user guess > 1000 or < 0
            if guess < 0 or guess > 1000:
                print("Please input a number between 0 and 1000.")
            #otherwise, if user input < random generate number, output the guess is too small
            elif guess < self.target_number:
                print("Number too small,You used",self.current_attempt,"attempts")
            # otherwise, if user input > random generate number, output the guess is too big
            elif guess > self.target_number:
                print("Number too large,You used",self.current_attempt,".")
            else:
                #print the answer and attempts used
                print(f"Correct! The number is {self.target_number}!")
                print(f"You found it in {self.current_attempt} attempts.")
                #set game_active to false to kill the program
                self.game_active = False
            #loop if guess is not equal to random generate number, accumulate the counter
            self.current_attempt += 1
        #output error message if input is invalid
        except ValueError:
            print("Invalid input! Please enter an integer.")
#run the program
game = GuessNumberGame()
game.start_game()
