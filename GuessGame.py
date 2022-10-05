import random
import utils

# can tweak these variables
MULTI_EXPONENT = 3
TRIES = 3
DEBUG = utils.DEBUG


class GuessGame:

    def __init__(self, difficulty):
        self.difficulty = difficulty * MULTI_EXPONENT # the range of numbers for guessing
        self.secret = self.generate_number() # the selected secret number
        self.valid_answers = [] # array of all possible valid user inputs
        for i in range(1, self.difficulty + 1):
            self.valid_answers.append(str(i))

    def generate_number(self):
        return random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        # function taken from utils.py for validating user inputs
        return utils.validate_input_given_list(prompt=f"Please enter your guess ({1}-{self.difficulty}) : ", options_list=self.valid_answers)

    def compare_results(self, user_input):
        if DEBUG: print(f"DEBUG: secret: {self.secret}, user_input: {user_input}\n")
        return self.secret == int(user_input)

    def play(self):
        print("\n--------------------------------------------------------"
              "\nWelcome to the guessing game game! "
              "\nIn this game, the computer will choose a random number, and you will 3 tries to guess it correctly."
              "\n--------------------------------------------------------")
        # loop exit parameters
        exit_game = False
        tries = TRIES
        # game loop
        while not exit_game and tries > 0:
            user_input = self.get_guess_from_user()
            if self.compare_results(user_input):
                print("You guessed it correctly! Great job!")
                exit_game = True
            else:
                tries -= 1
                print(f"You guessed it incorrectly. Try again. ({tries} tries left)")

        # won or lost
        if tries == 0:
            print(f"No tries left, the secret numer was {self.secret}")
            return False
        else:
            return True
