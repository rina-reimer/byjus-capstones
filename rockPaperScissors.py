## Rock Paper Scissors
# In the algorithm, the computer should keep a count of player moves (i.e., the counts for 0, 1 and 2) in three separate variables - 
# count_rock, count_paper and count_scissors. The algorithm should decide the computer's move based on the following possibilities:
# If the value of the count_rock variable > count_paper and count_scissors variables, then the computer's move should be ROCK.
# If the value of the count_paper variable > count_rock and count_scissors variables, then the computer's move should be PAPER.
# If the value of the count_scissors variable > count_rock and count_paper variables, then the computer's move should be SCISSORS.
#In all other cases, the computer should play ROCK, PAPER and SCISSORS randoml
import random
count_rock = 0
count_paper = 0
count_scissors = 0
player_score = 0
comp_score = 0
valid_entries = ["0", "1", "2"]

# Create the update_counts() function.
def update_counts(user_input):
  global count_rock, count_paper, count_scissors
  if user_input == 0:
    count_rock += 1
  elif user_input == 1:
    count_paper +=1
  elif user_input == 2: 
    count_scissors +=1

# Create the predict() function.
def predict():
  pred = None
  if count_rock > count_paper and count_rock > count_scissors:
    pred = 1
  elif count_paper > count_rock and count_paper > count_scissors:
    pred = 2
  elif count_scissors > count_paper and count_scissors > count_rock:
    pred = 0
  return pred

# Create the update_scores() function.
def update_scores(user_input):
  global player_score, comp_score
  predicted = predict()
  if user_input == 0:
    if predicted == 0:
      print("\nYou played ROCK, computer played ROCK.")
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    elif predicted == 1:
      print("\nYou played ROCK, computer played PAPER.")
      comp_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    elif predicted == 2:
      print("\nYou played ROCK, computer played SCISSORS.")
      player_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
  if user_input == 1:
    if predicted == 0:
      print("\nYou played PAPER, computer played ROCK.")
      player_score +=1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    elif predicted == 1:
      print("\nYou played PAPER, computer played PAPER.")
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    elif predicted ==2:
      print("\nYou played PAPER, computer played SCISSORS.")
      comp_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
  if user_input == 2:
    if predicted == 0:
      print("\nYou played SCISSORS, computer played ROCK.")
      comp_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    elif predicted == 1:
      print("\nYou played SCISSORS, computer played PAPER.")
      player_score += 1
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)
    elif predicted ==2:
      print("\nYou played SCISSORS, computer played SCISSORS.")
      print("\nComputer Score: ", comp_score, "\nYour Score: ", player_score)

# Gameplay
while True:
    user_input = input("Enter 0 for ROCK, 1 for PAPER and 2 for SCISSORS: ")
    while user_input not in valid_entries:
        print("Invalid Entry")
        user_input = input("Enter 0 for ROCK, 1 for PAPER and 2 for SCISSORS: ")
    user_input = int(user_input)
    update_scores(user_input)
    update_counts(user_input)
    if comp_score ==10:
        print("Computer Won!")
        break
    elif player_score == 10:
        print("You Won!")
        break