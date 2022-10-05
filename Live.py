import misc
from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrecyRouletteGame import CurrencyRouletteGame

# can tweak these variables
DEBUG = False


class Live:

    def __init__(self, name):
        self.name = name

    def welcome(self):
        """Greats the user at the start of the program"""
        return (f"\n--------------------------------------------------------"
                f"\nHello {self.name} and welcome to the World of Games (WoG). "
                f"\nHere you can find many cool games to play."
                f"\n--------------------------------------------------------")

    def load_game(self):
        # menu
        print("Please choose a game to play: "
              "\n\t0. Exit"
              "\n\t1. Guess Game - guess a number and see if you chose like the computer"
              "\n\t2. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back "
              "\n\t3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")

        # user input for the menu selection (sent to validation)
        game = int(misc.validate_input_given_list(prompt="Enter your selection: ", options_list=['0', '1', '2', '3']))

        # handling the user choice
        if game == 0:
            print("Good bye.")
            return
        else:
            difficulty = int(misc.validate_input_given_list(prompt="Select difficulty level between 1-5: ",
                                                            options_list=['1', '2', '3', '4', '5']))

        if DEBUG: print(f"\nDEBUG: game: {game}, difficulty: {difficulty}\n")

        if game == 1:
            guess_game = GuessGame(difficulty)
            if guess_game.play():
                print('\nYou won the game!')
            else:
                print('\nYou lost the game, I wish you better luck next time.')
        elif game == 2:
            memory_game = MemoryGame(difficulty)
            if memory_game.play():
                print("\nYou won the game!")
            else:
                print('\nYou lost the game, I wish you better luck next time.')
        elif game == 3:
            currency_roulette_game = CurrencyRouletteGame(difficulty)
            if currency_roulette_game.play():
                print("\nYou won the game!")
            else:
                print('\nYou lost the game, I wish you better luck next time.')
            pass

