import random, os, sys

# ••••••••• Generic Functions ••••••••• #

# Get system info
def getOs():
    os_Name = os.name
    return os_Name

# Get System info and clean console
def consoleClean():
    if getOs() == 'posix':
        os.system("clear") 
    else:
        os.system("cls")

# ••••••••• Game Design Functions ••••••••• #

# Print Old Grid - Not used anymore
def printGrid(marks):
    print("")
    print("     |     |    ")
    print("  " + marks[0] + "  |  " + marks[1] + "  |  " + marks[2] + "  ")
    print("_____|_____|_____")
    print("     |     |    ")
    print("  " + marks[3] + "  |  " + marks[4] + "  |  " + marks[5] + "  ")
    print("_____|_____|_____")
    print("     |     |    ")
    print("  " + marks[6] + "  |  " + marks[7] + "  |  " + marks[8] + "  ")
    print("     |     |    ")
    print("")

# Print New Fashionable Grid - in use
def newGrid(marks):
    print("\n")
    print("        ██     ██     ")
    print("     " + marks[0] + "  ██  " + marks[1] + "  ██  " + marks[2] + "  ")
    print("        ██     ██     ")
    print("   ███████████████████")
    print("        ██     ██     ")
    print("     " + marks[3] + "  ██  " + marks[4] + "  ██  " + marks[5] + "  ")
    print("        ██     ██     ")
    print("   ███████████████████")
    print("        ██     ██     ")
    print("     " + marks[6] + "  ██  " + marks[7] + "  ██  " + marks[8] + "  ")
    print("        ██     ██     ")
    print("\n")

# Refresh Page
def refresh(marks):
    consoleClean()
    #printGrid(marks) -> Not used anymore due to newGrid()
    newGrid(marks)

# ••••••••• Game Logical Functions ••••••••• #

# Request User Input
def userInput(marks):

    # Get the raw user input
    raw_input = input(">> Insert box number where insert your mark (from 1 to 9): ")

    # Try to convert the input string in an Integer
    try:
        # Convert the raw_input in an integer
        int_input = int(raw_input)
        
        # Check if the value is included between 1 and 9
        if (int_input >= 1 and int_input <= 9):

            # Check if mark place choosen is free
            if marks[int_input - 1] != " ":
                print("Select a free space for your mark !")
                return 0

            # Exit the loop if the range is valid
            return int_input
        
        # Don't exit the loop
        return 0
    
    # If the conversion got wrong
    except ValueError:
        print("Insert a correct value: A number between 1 and 9.")
        return 0
    
# Pick an available place to mark
def cpuInput(marks):

    # Available index that can be picked up from CPU
    availableMarks = []

    # From 0 to 9 check if index is empty or already picked
    for i in range(0, 9, 1):
        if marks[i] == " ":
            availableMarks.append(i)  
        
    return random.choice(availableMarks)

# Check marks in the Grid for a Winner
def valueMarks(marks):
    
    # If the User has 3 marks in line, He wins

    match marks:
        
        # Row check
        case [a, b, c, *_] if "X" == a == b == c:
            return "Win"
        case [a, b, c, *_] if "O" == a == b == c:
            return "Lose"
        case [_, _, _, d, e, f, *_] if "X" == d == e == f:
            return "Win"
        case [_, _, _, d, e, f, *_] if "O" == d == e == f:
            return "Lose"
        case[_, _, _, _, _, _, g, h, i] if "X" == g == h == i:
            return "Win"
        case[_, _, _, _, _, _, g, h, i] if "O" == g == h == i:
            return "Lose"
        
        # Coloumns check
        case [a, _, _, d, _, _, g, *_] if "X" == a == d == g:
            return "Win"
        case [a, _, _, d, _, _, g, *_] if "O" == a == d == g:
            return "Lose"
        case [_ , b, _, _, e, _, _, h, *_] if "X" == b == e == h:
            return "Win"
        case [_ , b, _, _, e, _, _, h, *_] if "O" == b == e == h:
            return "Lose"
        case [_ , _, c, _, _, f, _, _, i] if "X" == c == f == i:
            return "Win"
        case [_ , _, c, _, _, f, _, _, i] if "O" == c == f == i:
            return "Lose"
        
        # Diagonals check
        case [a , _, _, _, e, _, _, _, i] if "X" == a == e == i:
            return "Win"
        case [a , _, _, _, e, _, _, _, i] if "O" == a == e == i:
            return "Lose"   
        case [_, _, c, _, e, _, g, *_] if "X" == c == e == g:
            return "Win"
        case [_, _, c, _, e, _, g, *_] if "O" == c == e == g:
            return "Lose"        
        
        # check for a draw
        case _:

            # Count the numer of marks
            markscounter = 0

            # If the number of empty space = 1, it's a draw, no winner
            for i in range(0, 9, 1):
                if marks[i] != " ":
                    markscounter += 1

            if markscounter >= 8:
                return "Draw"

# Run in case of Draw
def draw():
    input("It's a draw")

# Run in case of Win
def win():
    input("You Win !")

# Run in case of Lose
def lose():
    input("You Lose")

# Value if there is a Winner
def checkWinner(marks):

    # Obtain the state of the match, if the user Win/Lose/Draw
    state = valueMarks(marks)

    # Check if user Wìn/lose/Draw and manage the match
    if state == "Win":
            win()
            return False
    elif state == "Lose":
            lose()
            return False
    elif state == "Draw":
            draw()
            return False
    else:
        return True

# ••••••••• Menu functions ••••••••• #

# Print the menu and gain user input
def menu():

    menuSplash()

    # Get the raw user input
    raw_input = input(">> ")

    # Try to convert the input string in an Integer
    try:
        # Convert the raw_input in an integer
        int_input = int(raw_input)
        
        # Check if the value is included between 1 and 3
        if (int_input >= 1 and int_input <= 3):
            match int_input:
                case 1:
                    return True
                case 2:
                    pass
                case 3:
                    sys.exit()
        else:
            raise ValueError
        
    # If the conversion got wrong
    except ValueError:
        input("Insert a correct value: A number between 1 and 3 ! ")

# The splash art and menu structure
def menuSplash():
    consoleClean()
    print("\n")
    print("   ████████ ██  ██████ ████████  █████   ██████ ████████  ██████  ███████ ")
    print("      ██    ██ ██         ██    ██   ██ ██         ██    ██    ██ ██      ")
    print("      ██    ██ ██         ██    ███████ ██         ██    ██    ██ █████   ")
    print("      ██    ██ ██         ██    ██   ██ ██         ██    ██    ██ ██      ")
    print("      ██    ██  ██████    ██    ██   ██  ██████    ██     ██████  ███████ ")
    print("\n                                                              Version 0.1")
    print("\n")
    print(" 1. Start the Game ")
    print(" 2. Settings ")
    print(" 3. Exit ")
    print("\n")

# To improve with some settings
def menuSettings():
    pass