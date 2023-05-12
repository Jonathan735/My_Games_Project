import games
import random
def restart():
    print("(Y) YES || (N) NO")
    replay = input("Want to play again? ").strip().upper()

    if replay == "Y":
        play()
    elif replay == "N":
        print("See you!")
        games.play()
    else:
        print("Select a valid option!!")
        restart()

def initial_banner():
    print("#################################################")
    print("#################################################")
    print("##### WELCOME TO THE GUESS THE NUMBER GAME! #####")
    print("#################################################")
    print("#################################################")

def theme_banner():
    print("choose a difficulty level:")
    print("(1) easy (2) moderate (3) Hard")

def play():

    initial_banner()
    theme_banner()

    secret_number = random.randrange(1, 51)
    attempts = 0
    level = int(input("define difficulty: "))

    if(level == 1):
        attempts = 20
    elif(level == 2):
        attempts = 10
    else:
        attempts = 5

    for round in range (1, attempts + 1):
        print("round {} of {}".format(round, attempts))

        Guess_str = input("guess a number from 1 to 50: ")
        Guess = int(Guess_str)
        correct = secret_number == Guess
        higher = Guess > secret_number

        if (Guess > 50 or Guess < 1):
            print ("only numbers from 1 to 50!")
            continue
        if (correct):
            winner_message()
            break
        else:
            if (higher):
                print("Choose a lower number!")
            else:
                print("Choose a higher number!")

    print ("end game")
    restart()

def winner_message():
    print("CONGRATULATIONS, YOU WON!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

if(__name__ == "__main__"):
    play()