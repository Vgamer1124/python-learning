import random
list=["Rock","Paper","Scissors"]
computer_choice=random.choice(list)
cpu_score=0
player_score=0
while True:
    player_choice=input("enter the choice").capitalize()
    if player_choice==computer_choice:
        print("tie")
        player_score+=1
        cpu_score+=1
    elif player_choice=="Rock":
        if computer_choice=="Paper":
            print("computer wins")
            cpu_score+=1
        if computer_choice=="Scissors":
            print("Player wins")
            player_score+=1
    elif player_choice=="Paper":
        if computer_choice=="Scissors":
            print("Computer wins")
            cpu_score+=1
        if computer_choice=="Rock":
            print("Player wins")
            player_score+=1
    elif player_choice=="Scissors":
        if computer_choice=="Rock":
            print("Computer wins")
            cpu_score+=1
        if computer_choice=="Paper":
            print("Player wins")
            player_score+=1
    else:
        print("cpu score:",cpu_score)
        print("player score:",player_score)
        break




