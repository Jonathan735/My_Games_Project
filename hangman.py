import games
import random
def theme_analyzis(theme_index):
    choice_dictionary = {
        1: "fruits",
        2: "objects",
        3: "countries",
    }


    return choice_dictionary[theme_index]
def choose_cathegory():
    Theme = (1, 2, 3)
    theme_number = input("Select a theme: ")
    while True:
        if theme_number.isnumeric() and int(theme_number) in Theme:
             return int(theme_number)
        else:
            theme_number = input("select a valid theme: ")
            theme_index = theme_number
            return theme_index
def Categories_banner():
    print("[1]fruits [2]objects [3] countries")
def play():
    initial_banner()
    Categories_banner()
    theme_index = choose_cathegory()
    theme = theme_analyzis(theme_index)
    secret_word = Load_Secret_Word(theme)
    
    
    
    guessed_letters = ["_" for letter in secret_word]
    wrong_letters = []
    print("Tip: {}".format(theme))
    print (guessed_letters)

    hanged = False
    Guessed = False
    mistakes = 0
    
    while(not hanged and not Guessed):

        guess = ask_guess()
        
        if (guess in secret_word):                                                                     
           score_correct_guess(guess, secret_word, guessed_letters)
        
        else:
            wrong_letters.append(guess)
            print("wrong letters: {}".format(wrong_letters))
            mistakes += 1
            hanged_drawing(mistakes)
        
        hanged = mistakes == 7
        Guessed = "_" not in guessed_letters
        print (guessed_letters)

    if Guessed:
        winner_message()
        restart()
    else:
        Loser_message(secret_word)
        restart()
def initial_banner():
    print("########################################")
    print("########################################")
    print("##### WELCOME TO THE HANGMAN GAME! #####")
    print("########################################")
    print("########################################")
def Load_Secret_Word(cathegory):
    file = open(cathegory + ".txt", "r")
    fruits = [line.strip() for line in file]
    file.close()
    number = random.randrange(0,len(fruits))
    secret_word = fruits[number].upper()
    return secret_word

def score_correct_guess(guess, secret_word, guessed_letters):
    index = 0
    for letter in secret_word:
        if (guess == letter):
            guessed_letters [index] = letter
        index += 1

def ask_guess():
    guess = input("Guess the letter: ")
    guess = guess.strip().upper()
    return guess

def winner_message():
    print("congratulations, you guessed right!")
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

def Loser_message(secret_word):
    print("Well it looks like you got hanged!")
    print("the word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def hanged_drawing(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    if(mistakes == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(mistakes == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (mistakes == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

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

if(__name__ == "__main__"):
    play()