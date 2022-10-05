from Live import Live
from Scores import Scores


def main():
    username = input("Please enter your name: ")
    scores = Scores(username)
    live = Live(username, scores)

    exit_program = False
    while not exit_program:
        print(live.welcome())
        returned = live.load_game()

        if returned == 0:
            break

        if input("\nPress Enter to start again, or 'E/e' to exit: ").upper() == 'E':
            print("Good bye!")
            exit_program = True


if __name__ == "__main__":
    main()