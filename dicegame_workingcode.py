import random

def diceroll(sides):  
    dice = random.randrange(sides)
    return dice       
def nameprompt():
    p1 = input("Enter players name: ")
    return p1
def gameplay():
    rollone = diceroll(10) 
    print(rollone)
    return rollone
def gameresult(rollone, rolltwo):
    if rollone > rolltwo:
        print ("Player One Wins!")
    elif rolltwo > rollone:
        print ("Player Two Wins!")
    else:
        print ("you tied")
def main():
    playagain = input("play again? y/n: ")
    if playagain.lower() == "n":
        print ("Goodbye.")
    elif playagain.lower() == "y":  
        print ("No you don't, this game is stupid.  Bye Felicia")       
    else: 
        print("try again... ")
        
    
player1 = nameprompt()
player2 = nameprompt()
player1roll = gameplay()
player2roll = gameplay()
gameresult(player1roll,player2roll)

main()
    