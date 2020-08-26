import random


def display_welcome_message():
    print("Hello, welcome to the number guessing game!")


def display_highscore(highscore):
    print("Highscore (least guesses):",
          "is not set." if highscore is None else highscore)


def display_win_message(attempts):
    print("Your answer is correct!\nIt took you {} attempt(s)!".format(attempts))


def display_hint_for_lower():
    print("It's lower")


def display_hint_for_higher():
    print("It's higher")


def display_error(error):
    print(error)


def display_goodbye_message():
    print("Thank you for playing, goodbye.")


def prompt_for_guess_between(LOWERBOUND, UPPERBOUND):
    return int(input("Guess a number between {} and {}: ".format(LOWERBOUND, UPPERBOUND)))


def prompt_for_replay():
    return input("Would you like to play again? y/n ")


def wrap_and_initialize():
    highscore = None
    while True:
        display_highscore(highscore)
        score = play()
        if highscore is None or score < highscore:
            highscore = score
        if prompt_for_replay() == 'n':
            break


def play():
    LOWERBOUND = 1
    UPPERBOUND = 10
    ANSWER = random.randint(LOWERBOUND, UPPERBOUND)

    guess = 0
    attempts = 0

    while guess != ANSWER:
        try:
            guess = prompt_for_guess_between(LOWERBOUND, UPPERBOUND)
            if guess < LOWERBOUND or guess > UPPERBOUND:
                raise ValueError("your guess is out of bounds. Minimum = {}. Maximum = {}."
                                 .format(LOWERBOUND, UPPERBOUND))
        except ValueError as error:
            display_error("An error was found: {}".format(error))
        else:
            attempts += 1
            if guess == ANSWER:
                display_win_message(attempts)
            else:
                if guess < ANSWER:
                    display_hint_for_higher()
                else:
                    display_hint_for_lower()
    return attempts


def start_game():
    display_welcome_message()
    wrap_and_initialize()
    display_goodbye_message()


start_game()
