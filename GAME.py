import random

# Ask the user how many rounds they want to play
rounds = int(input("How many rounds do you want to play? "))

for _ in range(rounds):
    mygame = input("Enter a choice (rock, paper, scissors): ").lower()
    gamer = ["rock", "paper", "scissors"]
    choose = random.choice(gamer)

    print(f"Computer chose {choose}.")

    if mygame == choose:
        print(f"Both players selected {mygame}. It's a tie!")
        
    elif mygame == "rock" and choose == "scissors":
        print("Rock crushes scissors! You win!")
        
    elif mygame == "paper" and choose == "rock":
        print("Paper covers rock! You win!")
        
    elif mygame == "scissors" and choose == "paper":
        print("Scissors cuts paper! You win!")
        
    elif mygame == "rock" and choose == "paper":
        print("Paper covers rock! You lose!")
        
    elif mygame == "scissors" and choose == "rock":
        print("Rock crushes scissors! You lose!")
        
    elif mygame == "paper" and choose == "scissors":
        print("Scissors cuts paper! You lose!")
    
    else:
        print("Invalid input, please enter rock, paper, or scissors.")


print("Thanks for playing!")
