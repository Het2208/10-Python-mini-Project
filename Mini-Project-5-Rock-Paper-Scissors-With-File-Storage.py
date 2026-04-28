import random

def chooseWinner(userInput , RPS):

    computerInput = random.choice(RPS)

    print(f"User Choice : {userInput}")
    print(f"Computer Choice : {computerInput}")

    Result = ""

    print("-" * 30)
    if userInput == computerInput:
        print("Draw !!")
        Result = "Draw"
    elif (userInput=="paper" and computerInput=="rock") or (userInput=="scissors" and computerInput=="paper")\
            or (userInput=="rock" and computerInput=="scissors"):
        print("You Win!!")
        Result = "You Win"
    else:
        print("You Lose!!")
        Result = "You Lose"
    print("*" * 30)
    with open("History.txt" , "a") as file:
        file.write(f"User : {userInput:<10}  Computer : {computerInput:<10}  Result : {Result:<10}")
        file.write("\n")


def gameHistory():
    print("-" * 45)
    try:
        with open("History.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No game history found!")
    print("-" * 45)

def main():
    print("*" * 42)
    print("Welcome to the Rock Paper Scissors Game!")
    print("*" * 42)
    is_running = True
    RPS = ["rock", "paper", "scissors"]
    while is_running:
        try:
            ch = int(input("Enter 1. Play , 2. Game History , 3. Exit : "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        match(ch):
            case 1:
                userInput = input("\nChoose your option: 'rock', 'paper' or 'scissors'.' : ").lower()
                while userInput not in RPS:
                    userInput = input("Invalid choice -> Choose your option: 'rock', 'paper' or 'scissors'.' : ").lower()
                chooseWinner(userInput , RPS)
            case 2:
                gameHistory()
            case 3:
                is_running = False
            case _:
                print("Invalid choice!")

main()

