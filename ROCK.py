import random

# assigning variables to count the score 
userScore,compScore=0,0

# running loop until user wants to play the game 
while(1):
    game=['rock','scissor','paper']
    # taking user input 
    userChoice=input("Enter rock/paper/scissor : ").lower()

    # checking user choice 
    if userChoice not in game :
        print("please enter valid input (rock/paper/scissor) ")
        continue

    # taking random value for computer choice 
    compChoice=random.choice(game)

    # printing user and computer choices 
    print("Your choice : ",userChoice,"\nComputer choice : " ,compChoice)

    # checking user choice and computer choice to increase score 
    if userChoice=='rock' and compChoice =='scissor' :
        userScore+=1
    elif userChoice=='scissor' and compChoice =='paper' :
        userScore+=1
    elif userChoice=='paper' and compChoice =='rock' :
        userScore+=1
    elif userChoice == compChoice :
        continue
    else:
        compScore+=1   
    
    # checking whether user wants to play the game or not 
    play=input("play again ? (yes/no) : ").lower()
    if play == "no" :
        break 
# printing score after completion of game 
print("Your Score  : ",userScore,"\nComp Score : ",compScore)

# overall output
if(userScore>compScore):
    print("Congo..... You won ")
elif userScore == compScore : 
    print("tie")
else:
    print("You lost!")
    
