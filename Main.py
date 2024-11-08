#hangman game
import random

from Words_list import animals,fruits,countries,technology,python

hangman_art = {0 : ("  +---+",
"      |",
"      |",
"      |",
"      |",
"      |",
"========="),
    1 : (
"  +---+",
"  |   |",
"      |",
"      |",
"      |",
"      |",
"========="),
             2:  (
"  +---+",
"  |   |",
"  O   |",
"      |",
"      |",
"      |",
"========="),
               3: (
"  +---+",
"  |   |",
"  O   |",
"  |   |",
"      |",
"      |",
"========="),
               4: (
"  +---+",
"  |   |",
"  O   |",
" /|   |",
"      |",
"      |",
"========="),
               5:(
"  +---+",
"  |   |",
"  O   |",
" /|\\  |",
"      |",
"      |",
"========="),
               6: (
"  +---+",
"  |   |",
"  O   |",
" /|\\  |",
" /    |",
"      |",
"========="),
               7:("  +---+",
"  |   |",
"  O   |",
" /|\\  |",
" / \\  |",
"      |",
"=========")}

Response = input("Choose a topic to generate a random word \n"
                 "A = Animals\n"
                 "F = Fruits \n"
                 "C = Countries \n"
                 "T = Technology \n"
                 "P = Python\n"
                 ": ")
if Response == "A" :
    Response_x = animals
elif Response == "F" :
    Response_x = fruits
elif Response == "C" :
    Response_x = countries
elif Response == "T" :
    Response_x = technology
elif Response == "P" :
    Response_x = python
else:
    print("Error : please choose a valid choice.")

def display_man(wrong_guesses) :
    print("******************")
    for line in hangman_art[wrong_guesses] :
        print(line)
    print("******************")
def display_hint(hint)  :
    print(" ".join(hint))
def display_answer(answer) :
    print(" ".join(answer))
def main () :
    answer = random.choice(Response_x)
    hint = ["_"] * len(answer)
    wrong_guess = 0
    guessed_alphabets = set()
    is_running = True
    while is_running :
        display_man(wrong_guess)
        display_hint(hint)
        guess = input("Please Guess A Alphabet From The Chosen Word : ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input")
            continue
        if guess in guessed_alphabets :
            print(f"{guess} is already guessed" )
            continue

        guessed_alphabets.add(guess)

        if guess in answer :
            for i in range(len(answer)) :
                if answer[i] == guess :
                    hint[i] = guess
        else:
            wrong_guess +=1

        if "_" not in hint :
            display_man(wrong_guess)
            display_answer(answer)
            print("You Won!")
            is_running = False
        elif wrong_guess >= len(hangman_art) - 1 :
            display_man(wrong_guess)
            display_answer(answer)
            print("You Lose!")
            is_running = False



if __name__ == "__main__" :
    main()