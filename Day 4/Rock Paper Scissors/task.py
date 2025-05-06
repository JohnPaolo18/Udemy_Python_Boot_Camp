import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

players_choice = input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors\n")

hands_list = ["0", "1", "2"]
random_choice = random.choice(hands_list)

if players_choice == "0" and random_choice == "1":
    print(rock)
    print("Computer Choose:")
    print(paper)
    print("You lose")

elif players_choice == "0" and random_choice == "2":
    print(rock)
    print("Computer Choose:")
    print(scissors)
    print("You Win")
elif players_choice == "0" and random_choice == "0":
    print(rock)
    print("Computer Choose:")
    print(rock)
    print("It's a tie")
elif players_choice == "1" and random_choice == "1":
    print(paper)
    print("Computer Choose:")
    print(paper)
    print("It's a Tie")
elif players_choice == "1" and random_choice == "2":
    print(paper)
    print("Computer Choose:")
    print(scissors)
    print("You lose")
elif players_choice == "1" and random_choice == "0":
    print(paper)
    print("Computer Choose:")
    print(rock)
    print("You Win")
elif players_choice == "2" and random_choice == "2":
    print(scissors)
    print("Computer Choose:")
    print(scissors)
    print("It's a Tie!")
elif players_choice == "2" and random_choice == "1":
    print(scissors)
    print("Computer Choose:")
    print(paper)
    print("You Win")
elif players_choice == "2" and random_choice == "0":
    print(scissors)
    print("Computer Choose:")
    print(rock)
    print("You lose")
else:
    print("Your choice was incorrect")
