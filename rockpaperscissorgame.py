<<<<<<< HEAD
import random
options=("rock","paper","scissor")

running=True
while running:
    player=None
    computer=random.choice(options)
    while player not in options:

        player=input("enter your guess from options: ")
    print(f"player: {player}")
    print(f"computer: {computer}")

    if player=="paper" and computer=="rock":
        print("you win____-------whohhhhh")
    elif player=="rock" and computer=="scissor":
        print("you win ------------ woahhhh")
    elif player=="scissor" and computer=="paper":
        print("you win----------- woahhhhh")
    else:
        print("-------------computer wins---  -- ----------")
    
    repetation=input(" you wanted to play again: ").lower()
    if repetation!="yes":
        running=False
        print("thanks for playing! bye")


=======
import random
options=("rock","paper","scissor")

running=True
while running:
    player=None
    computer=random.choice(options)
    while player not in options:

        player=input("enter your guess from options: ")
    print(f"player: {player}")
    print(f"computer: {computer}")

    if player=="paper" and computer=="rock":
        print("you win____-------whohhhhh")
    elif player=="rock" and computer=="scissor":
        print("you win ------------ woahhhh")
    elif player=="scissor" and computer=="paper":
        print("you win----------- woahhhhh")
    else:
        print("-------------computer wins---  -- ----------")
    
    repetation=input(" you wanted to play again: ").lower()
    if repetation!="yes":
        running=False
        print("thanks for playing! bye")


>>>>>>> 45d1a8f1206a7d905c9d7dd8fdd717f467ff784e
