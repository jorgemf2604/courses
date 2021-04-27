import random
import os


class Hangman():
    def __init__(self):
        self.word_list = ["dog", "cat", "camel", "aardvark", "baboon", "hawk"]
        self.chosen_word = random.choice(self.word_list)
        self.user_guess = None
        self.placeholder = []
        self.stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

        self.lives = len(self.stages)-1

    def print_stage(self, index):
        print(self.stages[index])

    def print_initial_msg(self):
        print(
            "==============================================================================")
        print(
            f"Welcome to the Hangman game! I am thinking of an animal with {len(self.chosen_word)} charaters.")
        print(
            "==============================================================================")

    def ask_user(self):
        self.user_guess = input("Guess a letter: ").lower()

    def create_placeholder(self):
        for char in self.chosen_word:
            self.placeholder.append("*")

    def print_placeholder(self):
        print(self.placeholder)

    def populate_placeholder(self, guess):
        for index in range(len(self.chosen_word)):
            if guess == self.chosen_word[index]:
                self.placeholder[index] = guess

    def print_info(self):
        print(f"You have {self.lives} lives left...")
        self.print_placeholder()
        print(self.stages[self.lives])

    def check_guess(self, char):
        if char in self.chosen_word:
            print(f"\nYes, {char} is in the word.")
            self.populate_placeholder(char)
        else:
            print(f"\nSorry, {char} is not in the word. You lose a life.")
            self.lives -= 1
        self.print_info()

    def start_game(self):
        self.print_initial_msg()
        self.create_placeholder()
        keep_asking = True
        while keep_asking:
            self.ask_user()
            self.check_guess(self.user_guess)
            if self.lives == 0:
                keep_asking = False
                print("You have run out of lives, you lose.")
            if self.chosen_word == "".join(self.placeholder):
                keep_asking = False
                print("You have guessed the word! You win!")


def main():
    play_again = "yes"
    while (play_again == "yes"):
        new_game = Hangman()
        new_game.start_game()
        play_again = input("Do you want to play again? yes/no: ").lower()
        os.system("clear")


main()
