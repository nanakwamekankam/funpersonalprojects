import functions
import turtle


def main():
    print_header()
    functions.draw_pole()
    print("Let's play Hangman")
    print("Guess the letters in the word I'm thinking of...")
    print()
    play_word = functions.word_generator()
    play_letters = functions.letters_of_word(play_word)
    run_event_loop(play_letters, play_word)


def print_header():
    print("---------------------------------------")
    print("               HANGMAN                 ")
    print("---------------------------------------")
    print()


def run_event_loop(letters, word):
    t = turtle.Turtle()
    turns = 6
    failed = 0
    passed = 0
    guesses = []
    word_completion = ["_" for letter in letters]

    while turns != 0 and passed != len(letters) and failed != 6:
        guess = input("Letter: ")
        guess = guess.lower().strip()

        if not guess or not guess.strip():
            print("Words are made up of letters")

        if guess in letters:
            if guess in guesses:
                print("Oops. Looks like you already guessed that.")
            else:
                for i in range(len(letters)):
                    if letters[i] == guess:
                        word_completion[i] = guess
                        passed += 1
                        print(word_completion)
        else:
            failed += 1
            turns -= 1
            print(f"Nope, you have {turns} turns left")
            functions.steps_hangman(t, turns+1)
        guesses.append(guess)

    print()
    if turns == 0 and failed == 6:
        print(f"Sorry. The word was {word.upper()}. You loose")
    if passed == len(letters):
        print(f"Yep, you guessed it. The word was {word.upper()}")


if __name__ == '__main__':
    main()
