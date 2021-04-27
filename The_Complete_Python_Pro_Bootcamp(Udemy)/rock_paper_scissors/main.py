import random
import time
import os


class Game():
    def __init__(self):
        self.user_wins = 0
        self.computer_wins = 0
        self.computer_choice = None
        self.user_choice = None
        self.rock_img = "🪨"
        self.paper_img = "📜"
        self.scissors_img = "💇"
        self.num_rounds = 3
        self.is_game_over = False

    def ask_user(self):
        self.user_choice = int(
            input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))

    def computer_random_choice(self):
        self.computer_choice = random.randint(0, 2)

    def print_emoji(self, number):
        if number == 0:
            print(self.rock_img)
        elif number == 1:
            print(self.paper_img)
        elif number == 2:
            print(self.scissors_img)
        else:
            print("Enter a valid code...")

    def compare_choices(self):
        if self.user_choice == self.computer_choice:
            print("It is a tie")
        elif (self.user_choice == 0):
            if (self.computer_choice == 1):
                print("Computer wins!")
                self.computer_wins += 1
            elif (self.computer_choice == 2):
                print("User wins!")
                self.user_wins += 1
        elif (self.user_choice == 1):
            if (self.computer_choice == 0):
                print("User wins!")
                self.user_wins += 1
            elif (self.computer_choice == 2):
                print("Computer wins!")
                self.computer_wins += 1
        elif (self.user_choice == 2):
            if (self.computer_choice == 1):
                print("User wins!")
                self.user_wins += 1
            elif (self.computer_choice == 0):
                print("Computer wins!")
                self.computer_wins += 1
        else:
            print("Impossible comparison")

    def print_scores(self):
        print(f"Computer score: {self.computer_wins}/3")
        print(f"User score: {self.user_wins}/3")
        time.sleep(3)
        os.system("clear")

    def start_game(self):
        self.ask_user()
        self.computer_random_choice()
        print("You have choosen: ")
        self.print_emoji(self.user_choice)
        print("Computer chose: ")
        self.print_emoji(self.computer_choice)
        self.compare_choices()
        self.print_scores()

    def play(self):
        while not self.is_game_over:
            self.start_game()
            if self.computer_wins == self.num_rounds:
                print("The computer has won 3 rounds. It is the final winner")
                self.is_game_over = True
            if self.user_wins == self.num_rounds:
                print("The user has won 3 rounds. You are the final winner!")
                self.is_game_over = True


def main():
    play_again = "yes"
    while (play_again == "yes"):
        new_game = Game()
        new_game.play()
        play_again = input("Do you want to play again? yes/no: ").lower()
        os.system("clear")


main()
