# this file contains functions that are re-used many times in different other files
from os import system, name as sys_name

# Global Parameters
DEBUG = False
SCORES_FILE_NAME = 'Scores.csv'
BAD_RETURN_CODE = -1


# Functions
def clear_screen():
    system('cls' if sys_name == 'nt' else 'clear')


def validate_input_given_list(prompt, options_list):
    """If the user input is in the list of options, the function returns the input, else ask again for input"""
    validated = False
    while not validated:
        user_input = input(prompt).strip()
        if user_input in options_list:
            validated = True
        else:
            print("Invalid input")

    return user_input


def validate_input_is_number(prompt):
    digits = []
    validated = False
    while not validated:
        user_input = input(prompt).strip()

        if "." in user_input:
            digits = user_input.split(".")
        else:
            digits.append(user_input)

        matches = 0
        for i in digits:
            if i.isdigit():
                matches +=1

        if matches == len(digits):
            validated = True
        else:
            print("Invalid input.")

    return user_input

