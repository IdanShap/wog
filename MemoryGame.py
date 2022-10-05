import random
import time
import misc
from os import system, name as sys_name

# can tweak these variables
RANGE_MIN = 1
RANGE_MAX = 100
DISPLAY_NUMS_TIME = 0.7  # seconds
DEBUG = False


class MemoryGame:

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.valid_answers = [] # array of all valid answers for user input verification
        for i in range(RANGE_MIN, RANGE_MAX + 1):
            self.valid_answers.append(str(i))

    def generate_sequence(self):
        sequence = []
        for i in range(self.difficulty):
            # already converts to strings, so no conversion should be done later
            sequence.append(str(random.randint(RANGE_MIN, RANGE_MAX)))

        if DEBUG: print(f"\nDEBUG: {sequence}\n")
        return sequence

    def get_list_from_user(self):
        print("It's your time to enter the numbers you memorized, in the correct order")
        user_list = []
        for i in range(1, self.difficulty + 1):
            user_list.append(misc.validate_input_given_list(prompt=f"Nuber {i} : ", options_list=self.valid_answers))

        return user_list

    def is_list_equal(self, sequence, user_list):
        # compares each number in sequence to user_list, if not the same, returns immediately - user lost the game
        for i in range(self.difficulty):
            if DEBUG: print(f"\nDEBUG: sequence[i]: {sequence[i]}, user_list[i]: {user_list[i]}\n")
            if sequence[i] != user_list[i]:
                return False

        return True

    def play(self):
        input("\n--------------------------------------------------------"
              "\nWelcome to the Memory Game"
              f"\nIn this game a sequence of numbers will be displayed to you for {DISPLAY_NUMS_TIME} seconds"
              "\nIn order to win the game you will need to enter all the correct numbers in the correct order."
              "\n--------------------------------------------------------"
              "\nPress Enter to begin the game: ")

        # generates and prints the sequence of numbers to memorize
        sequence = self.generate_sequence()
        for number in sequence:
            print(number, end=" ")
        print()

        # clears the display after set time
        time.sleep(DISPLAY_NUMS_TIME)
        system('cls' if sys_name == 'nt' else 'clear')

        # prompts the user to enter the numbers he memorized
        user_list = self.get_list_from_user()
        if DEBUG: print(f"DEBUG: user_list: {user_list}, sequence: {sequence}\n")

        # handling results
        if self.is_list_equal(sequence, user_list):
            return True
        else:
            print(f"The correct sequence was: {sequence}")
            return False

