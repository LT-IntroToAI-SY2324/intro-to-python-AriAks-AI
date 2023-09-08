# We will write a rock paper scissors game in class - Complete it in this file
import random

available_choices = ["rock", "paper", "scissors"]
def rand():
    random.choice(available_choices)


Player_choice = input("rock paper or scissors")
computer_choice = rand()

choices = {"Player": Player_choice, "Computer": computer_choice}

def play_game(P, C):
    if(P == C):
        print("Thats a tie!")
    elif(P == "paper" & C == "rock"):
        print("You win!")

    

play_game(choices["Player"], choices["Computer"])