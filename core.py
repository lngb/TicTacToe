from modules import funcs

# Run a new match
def singleMatch():

    marks = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    # Running the main loop
    while True:

        # 1 - Refresh the console
        funcs.refresh(marks)

        # 2 - Request User Input
        while True:
            # Check the user input
            user_response = funcs.userInput(marks)

            # If user inserted a correct value
            if user_response != 0:                    
                marks[user_response - 1] = "X"
                break

        # 3 - Refresh the console
        funcs.refresh(marks)

        # 4 - Generate Random Numbers from available for the CPU
        while True:
            # Check the CPU pick
            cpu_response = funcs.cpuInput(marks)
                
            # If cpu picked a correct value
            if cpu_response is not None:
                marks[cpu_response] = "O"
                break

        # 5 - Refresh the console
        funcs.refresh(marks)

        # 6 - Check for a Winner, if the function return False, the game will end
        if not funcs.checkWinner(marks):
            return

# Manage the main loop
def main():
    while True:
        # Check if user starts a new game
        run = funcs.menu()

        # If user start a new match, run is True
        if run:
            singleMatch()  

# Entry Point
if __name__ == "__main__":
    # Run the main function
    main()