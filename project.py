import random
import os
import sys
import json
from art import *
from tabulate import tabulate



word = ""
score = 0
livesLeft = 6
guessedWord = ""
winCheck = []
correctGuess = 0
incorrectGuess = 0
difficultyCat = 0
words = ""

def main():
    global word
    global words
    global livesLeft
    global guessedWord
    global winCheck
    global correctGuess
    global incorrectGuess
    global difficultyCat

    win = False
    selection = start_screen()
    count = 0

    if selection == 2:
        view_leaderboard()
        sys.exit()


    elif selection == 1:
        word = generate_word()
        print(word)

    for x in range(len(word)):
        guessedWord = guessedWord + " "
    guessedWord = list(guessedWord)


    while livesLeft >= 0 and win == False:
        count = count + 1
        game_screen(livesLeft)
        print(word)
        print((word_formatting(word)).center(49))
        print(words.center(49))
        print()
        usr_input()

        if " " not in winCheck:
            win = True
            clear_screen()
            print(text2art("You win!", font='big'))
            print(("Mystery word:").center(48))
            print((word).center(48))
            print()
            score = calculate_score()
            print(("Final score: " + str(score)).center(48))
            print(("Correct attempts: " + str(correctGuess)).center(48))
            print(("Incorrect attempts: " + str(incorrectGuess)).center(48))
            print(("Total attempts until victory: " + str(count)).center(48))
            print()
            name = (input("Please enter your name: "))
            leaderboard(name, score, difficultyCat)
            break
    else:
        clear_screen()
        print(text2art("Game Over", font="big"))
        score = 0
        print(("Final score: " + str(score)).center(48))
        print(("Correct attempts: " + str(correctGuess)).center(48))
        print(("Incorrect attempts: " + str(incorrectGuess)).center(48))
        print()



def calculate_score():
    global correctGuess
    global incorrectGuess
    global word
    global livesLeft
    global difficultyCat

    score = (10 * int(correctGuess)) + (-5 * int(incorrectGuess)) + (5 * int(livesLeft)) + (-1 * (6 - int(livesLeft)))
    return score



def leaderboard(name, score, difficultyCat):
    file = open("leaderboard.json", "a")
    data = {"Difficulty": difficultyCat, "Name": name, "Score": score}
    json.dump(data, file)
    file.write("\n")
    file.close()

def usr_input():

    global word
    global livesLeft
    global guessedWord
    global words
    global winCheck
    global correctGuess
    global incorrectGuess


    charIndex = []
    count = -1

    inpt = input("Guess a character: ")

    if inpt in word:
        correctGuess = correctGuess + 1
        for char in word:
            count = count + 1
            if char == inpt:
                charIndex.append(count)
    else:
        incorrectGuess = incorrectGuess + 1
        livesLeft = livesLeft - 1

    guessedWord = list(guessedWord)

    for i in range(len(charIndex)):
        guessedWord[charIndex[i]] = inpt

    winCheck = guessedWord

    guessedWord = "".join(guessedWord)

    words = ""
    for char in guessedWord:
        words = words + char + " "
    return words


def hangman_img_file(livesLeft):

    file = open("life_pictures.txt", "r")
    pics = file.read()
    HANGMANPICS = pics.split(",")

    if livesLeft > 6 or livesLeft < 0:
        return(print("invalid lives"))
    else:
        return(HANGMANPICS[livesLeft])


def word_generator(difficulty):
    global difficultyCat

    #Open and read file with words
    file = open("words.txt", "r")
    words = file.read()

    listOfWords = words.split("\n")

    difficultyCat = difficulty

    if difficulty == 1:
        difficulty = (2, 3, 4, 5)

    elif difficulty == 2:
        difficulty = (6, 7, 8, 9)

    elif difficulty == 3:
        difficulty = (10, 11, 12, 13)

    elif difficulty == 4:
        difficulty = (14, 15, 16, 17)

    elif difficulty == 5:
        difficulty = (18, 19, 20, 21)

    #Find words with the length chosen
    chosenWords = []
    for word in listOfWords:
        if len(word) in difficulty :
            chosenWords.append(word)

    #Choose and return random word from list of words with chosen length
    randWord = random.choice(chosenWords)
    return randWord


def word_formatting(word):

    markers = ""
    for i in range(len(word)):
        markers = markers + "_ "

    return markers


def game_screen(livesLeft):

    clear_screen()
    print(word)
    title = text2art("HangMan", font='big')
    print(title)
    print(("LivesLeft: " + str(livesLeft) + "       " + "Score: " + str(calculate_score())).center(47))
    print(hangman_img_file(livesLeft))


def start_screen():
    clear_screen()
    title = text2art("HangMan", font='big')
    print(title)
    print(("1. Play game!").center(48))
    print(("2. View leaderboard").center(48))
    print()

    while True:
        try:
            selection = int(input("Please select a option: "))
            if selection > 2 or selection < 1:
                raise ValueError
            return selection
        except:
            print("Selected option invalid")
        else:
            break


def generate_word():
    while True:
        try:
            word = word_generator(int(input("Please choose a dificulty between 1 and 5: ")))
            return word
        except:
            print("Selected difficulty out of range")
        else:
            break


def view_leaderboard():
    clear_screen()
    print(text2art("Leaderboard", font='big'))

    data = []
    with open("leaderboard.json") as f:
        for line in f:
            data.append(json.loads(line))

    table = data

    print((tabulate(table, headers="keys", tablefmt="rounded_grid")))



    input("Press enter for main menu")
    main()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
