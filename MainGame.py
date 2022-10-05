from Live import Live


def main():
    live = Live(input("Please enter your name: "))

    exit_program = False
    while not exit_program:
        print(live.welcome())
        live.load_game()

        if input("\nPress Enter to start again, or 'E/e' to exit: ").upper() == 'E':
            print("Good bye!")
            exit_program = True


if __name__ == "__main__":
    main()