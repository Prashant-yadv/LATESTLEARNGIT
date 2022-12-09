import random
mygame= input("Enter a choice (rock, paper, scissors): ")
gamer=["rock","paper","scissor"]
choose=random.choice(gamer)

if mygame==choose:
    print("Both players slected", mygame,". It`s tie")
    
elif mygame =="rock" and choose == "scissor":
    print("Rock shames scisors! You win")

elif mygame=="paper" and choose == "scissor":
        print("paper covers rock! You lose")
        
elif mygame=="scissor" and choose == "paper":
    print("scissor cuts paper! You win")

elif mygame=="scissor" and choose == "rock":
    print("rock destroys scissor! You lose")

elif mygame=="rock" and choose == "paper":
    print("paper covers rock! You lose")

else:
    print("paper covers rock! You win")

