import random
from art import rock, paper, scissors, logo

print(logo)
print("\033[4m" + "\033[1;35m" + "WELCOME TO THE VIRTUAL ROCK, PAPER, SCISSOR GAME\n" + "\033[0m")
print("\033[3m" + '''rules;
  1.rock wins against scissors.
  2.scissors wins against paper.
  3.paper wins against rock.\n \n ''' + "\033[0m")

game_list_img = [rock, paper, scissors]
game_list_name = ['rock', 'paper', 'scissors']

game_continue = True
while game_continue:
    human_choice = int(input("what do you want to choose? Type 0 for 'rock', 1 for 'paper', 2 for 'scissor' : "))

    if human_choice == 0 or human_choice == 1 or human_choice == 2:

        print(f"\nyour choice is {human_choice} ({game_list_name[human_choice]}) \n{game_list_img[human_choice]}")

        computer_choice = random.randint(0, 2)
        print(f"Computer's choice is {computer_choice} ({game_list_name[computer_choice]}) \n{game_list_img[computer_choice]}")

        if human_choice == computer_choice:
            print("match draw.")
        elif human_choice == 0 and computer_choice == 2:
            print("you win.")
        elif human_choice == 1 and computer_choice == 0:
            print("you win")
        elif human_choice == 2 and computer_choice == 1:
            print("you win")
        else:
            print("\033[0;36m" + "you lost." + "\033[0m")
        if input("do you want to play again? yes/no: ").lower() == "no":
            break
    else:
        print("\nyour choice is wrong. select from given choice." + "\033[0;36m" + "\n\nGAME OVER" + "\033[0m")
        if input("do you want to play again? yes/no: ").lower() == "no":
            break
