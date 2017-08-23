from random import random

is_game_ended=False
comp_choice=""
possible_choices=['rock', 'paper', 'scissors']

while (is_game_ended==False) :
  prompt="Pick one: rock, paper, scissors>"

  user_choice=input(prompt)
  if user_choice not in possible_choices :
    print("Invalid choice.")
    continue

  rand_num = random() * 3

# make comp_choice by bucketing 
#  < 1 rock
#  < 2 paper
#  else scissors

  if (rand_num < 1) :
    comp_choice = "rock"
  elif (rand_num < 2) :
    comp_choice = "paper"
  else: comp_choice = "scissors"


  print("\nUser chose: " + user_choice + ", AI chose: " + comp_choice + "\n\n")

  if(user_choice==comp_choice) : 
    print("tie\n")
  #user wins: (rock, scissors), (paper, rock), (scissors, paper)
  elif ((user_choice=="rock" and comp_choice=="scissors") or (user_choice=="paper" and comp_choice=="rock") or (user_choice=="scissors" and comp_choice=="paper")) : 
    print("user wins")
    is_game_ended=True
  else: 
    print("AI wins")
    is_game_ended=True
    
print("\nGame ended.")
