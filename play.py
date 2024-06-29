print("Welcome to MasterMind Game")
player1_name = str(input("Enter name for player 1: "))
player2_name = str(input("Enter name for player 2: "))

game_result = {player1_name: {"wins": 0, "lose": 0}, player2_name: {"wins": 0, "lose": 0}}

guessing_number = None
turn = 2

def enter_number():
    global guessing_number
    global turn
    if turn > 0:
        g_number = int(input(f"{player1_name}, enter a 4 digit number: "))
        if len(str(g_number)) != 4:
            g_number = int(input(f"{player1_name}, Please enter a 4 digit number. Eg: 1234: "))
        
        guessing_number = g_number
        turn -= 1
        guess_the_number()
    else:
        print("Game ended",game_result)

def get_hint(p2_guess):
    hint_string = ""
    for i in range(len(str(guessing_number))):
        if str(guessing_number)[i] == p2_guess[i]:
            hint_string = f"{hint_string}{p2_guess[i]}"
        else:
            hint_string = f"{hint_string}__"
    
    return hint_string

def guess_the_number(tries=3):
    global guessing_number
    global player1_name
    global player2_name

    if tries > 0:
        p2_guess = str(input(f"{player2_name}, enter a 4 digit number and make a guess: "))
        
        if len(p2_guess) != 4:
            print("Please enter a valid 4 digit number")
            guess_the_number(tries)
            return
        
        result = None
        if guessing_number == int(p2_guess):
            result = True
        else:
            result = False

        if result:
            print(f"{player2_name} Wins.\n You guessed the correct number!! :D")
            game_result[player2_name]["wins"] += 1
            if turn > 0:
                print(f"Now we are switching sides. {player2_name}, Now you have to enter a 4 digit number: ")
            player1_name, player2_name = player2_name, player1_name
            enter_number()
            return
        else:
            print(f"{player2_name}, you made a correct guess")
            hint = get_hint(p2_guess)
            if turn > 0:
                print(f"Hint: {hint}")
                print("Try another number with the hint: ")
                guess_the_number(tries=tries-1)
            return

    print(f"{player2_name}, You lost!! :( Your 3 tries are up.")
    game_result[player2_name]["lose"] += 1
    print(f"Now we are switching sides. {player2_name}, Now you have to enter a 4 digit number: ")
    player1_name, player2_name = player2_name, player1_name
    enter_number()

enter_number()
