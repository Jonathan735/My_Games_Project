import GuessGame
import hangman

def play():
    print("########################################")
    print("########################################")
    print("##### WELCOME TO MY GAMES PROJECT! #####")
    print("####### FIRST JUST CHOOSE A GAME. ######")
    print("########################################")
    print("########################################")

    print("(1) HANGMAN! (2) GUESS THE NUMBER!")

    game = int(input("Wich one? "))
    if(game == 1):
        print("Running hangman")
        hangman.play()
    elif(game == 2):
        print("Running guessgame")
        GuessGame.play()

if(__name__ == "__main__"):
    play()