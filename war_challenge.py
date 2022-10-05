import random

def hangman(word):                          # create hangman function, accepts parameter called word
    wrong = 0                               # We start with 0 mistakes, this variable will keep tack of incorrect guesses
    stages = ["",                           # list filled with strings used to draw the hangman
              "_______        ",
              "|              ",
              "|      |       ",
              "|      0       ",
              "|     /|\      ",
              "|     / \      ",
              "|              "
              ]
    rletters = list(word)                   # rletters is a list containing each character in the variable word
    board = ["_"] * len(word)               # board is a list of strings used to keep track of the hints you display
    win = False                             # win variable used to keep track of whether player 2 has won the game
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:          # While loop that keeps the game going, compensate stages starts at 0 and wrong at 1
        print("\n")                         # print a blank space to make the game look nice
        msg = "Guess a letter"              # Input request message
        char = input(msg)                   # Request input and save is as variable char
        if char in rletters:                # Begin if statement
            cind = rletters.index(char)     # Use index method to get the first index
            board[cind] = char              # Update board list, replace underscore with character
            rletters[cind] = '$'            # Index only return the first index, modify rletters by replacing char with $
        else:
            wrong += 1                      # Increment wrong by 1
        print((" ".join(board)))            # print board
        e = wrong + 1                       # Wrong + 1 because stages has an empty line
        print("\n".join(stages[0:e]))       # Print hangman
        if "_" not in board:                # If _ not in board, you win!
            print("You win!")
            print(" ".join(board))          # Print complete board
            win = True                      # Change win to True to end while loop
            break                           # break if statement
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was {}.".format(word))


word_list = ["Hello", "Julie", "Diego", "dbt", "analytics"]

hangman(random.choice(word_list))