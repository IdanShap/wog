import random
import requests
import utils

# can tweak these variables
URL = 'https://v6.exchangerate-api.com/v6/fd6de2ab3c500dfeabb006ac/latest/USD' # URL for API requests for USD rates
RANGE_MIN = 1
RANGE_MAX = 100
ACCURACY = 4 # number of digits after decimal point
DEBUG = utils.DEBUG


class CurrencyRouletteGame:

    def __init__(self, difficulty):
        self.difficulty = difficulty
        # query the exchange API. saves USD/ILS rate
        self.dollar_shekel_rate = requests.get(URL).json()["conversion_rates"]["ILS"]
        self.dollar_total = random.randint(RANGE_MIN, RANGE_MAX)  # random amount of USD
        # total ILS, rounded to the decimal points based on the variable ACCURACY
        self.total = round(self.dollar_shekel_rate * self.dollar_total, ACCURACY)

    def get_money_interval(self):
        # tuple range, the user guess will be correct in this range
        interval = (self.total - (5 - self.difficulty), self.total + (5 - self.difficulty))

        if DEBUG: print(f"\nDEBUG: dollar_shekel_rate: {self.dollar_shekel_rate}, total: {self.total},"
                        f"difficulty: {self.difficulty}, interval: {interval}, dollar_total: {self.dollar_total}\n")
        return interval

    def get_guess_from_user(self):
        # gets user input and sends it to input validation
        user_input = float(utils.validate_input_is_number(f"Guess how much {self.dollar_total} Dollars worth in Shekels: "))
        user_input = round(user_input, ACCURACY)  # rounded by ACCURACY

        if DEBUG: print(f"\nDEBUG: user_input: {user_input}\n")
        return user_input

    def play(self):
        interval = self.get_money_interval()
        user_input = self.get_guess_from_user()

        # checks if the user guess is in the tuple range
        if interval[0] <= user_input <= interval[1]:
            return True
        else:
            print(f"The amount of {self.dollar_total} Dollars in Shekels is {self.total}")
            return False





