# Hangman game vs Computer:
# A random word is supplied from a dictionary to both the computer and the player.
# The computer uses weighted choices based on english letter usage percentages to decide what letter to use.
# A high score is kept in json format to load and update after each game; it saves all scores with datetime, however
# it will only display the top 10. If the high score file is not found, it will create one.


from dataclasses import dataclass
from english_words import word
from random import choice, choices, randint
from json import dump, load
from operator import itemgetter
from datetime import datetime


@dataclass()
class Hangman:
    name = "Player"
    select_difficulty = "Easy"
    lives = 10
    score = 0
    diff_multi = 1
    win_bonus = 100
    secret_word = ""
    letter = ""
    guesses1 = []
    guesses2 = []
    completed = False
    my_turn = False
    comp_alphabet = ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'l', 'q', 'w', 'e', 'r',
                     't', 'y', 'u', 'i', 'o', 'p']

    def hangman_menu(self):
        hangman_text = "HANGMAN vs Computer"
        hangman_text_centered = hangman_text.center(120, "-")
        print(hangman_text_centered)
        print(f"Welcome to Hangman vs Computer!")
        while True:
            try:
                print(f"currently playing as: {self.name}.\nthe difficulty is: {self.select_difficulty}.\n"
                      f"use integers to make your selection."
                      )
                start_game = int(input("\nchoose an option:\n1.start game\n2.change player name\n"
                                       "3.choose difficulty\n4.high scores\n5.quit\n"
                                       )
                                 )
                if start_game == 1:
                    self.hangman_game(computer1)
                elif start_game == 2:
                    self.name = input("write your name:\n")
                elif start_game == 3:
                    self.choose_difficulty()
                elif start_game == 4:
                    self.display_high_score()
                elif start_game == 5:
                    quit()

            except ValueError:
                print("please use integers.")

    def hangman_game(self, computer):
        print(f"{self.name} vs {computer.name}!")
        print("new game begins!\n")

        # refresh the player values from previous run

        self.set_player_values()
        computer.set_player_values()

        # create the secret word

        self.create_secret_word(computer1)

        # deciding turn order

        turn_order = randint(1, 2)
        if turn_order == 1:
            self.my_turn = True
            print(f"{self.name} goes first!")
        elif turn_order == 2:
            computer.my_turn = True
            print(f"{computer.name} goes first!")

            # -----------hangman game-----------

            # this next while loop is essentially the entire game, as it will keep looping until a end game condition
            # has been satisfied. It contains both the hangman text display as well as the guess inputs of both players.

            # display the secret word

        while not self.completed or not computer.completed:

            print(f"{computer.name}'s word: ", end="")
            computer_check_complete = ""
            for computer.letter in computer.secret_word:
                if computer.letter.lower() in computer.guesses2:
                    print(f"{computer.letter.upper()}", end=" ")
                    computer_check_complete += computer.letter
                else:
                    print(f"_", end=" ")

            print()

            print(f"{self.name}'s word: ", end="")
            player_check_complete = ""
            for self.letter in self.secret_word:
                if self.letter.lower() in self.guesses1:
                    print(f"{self.letter.upper()}", end=" ")
                    player_check_complete += self.letter
                else:
                    print(f"_", end=" ")

            print()

            if player_check_complete == self.secret_word:
                break
            if computer_check_complete == computer.secret_word:
                break

            # -------------play turns-------------

            # player turn

            if self.my_turn is True:
                guess_input = None
                acceptable_answer = False
                while acceptable_answer is False:
                    guess_input = input(
                        f"type 'letters' to see what letters were attempted so far.\n"
                        f"type 'quit' to quit game. attempts left: {self.lives}.\n"
                        f"guess a letter:\n"
                        ).lower()

                    if guess_input.isalpha():
                        acceptable_answer = True

                if guess_input not in self.guesses1 and guess_input != "letters":
                    print(f"{self.name} guessed the letter: {guess_input[0]}")
                    self.guesses1.append(guess_input[0])
                    self.my_turn = False
                    computer.my_turn = True
                if guess_input == "letters":
                    print(f"letters used so far: {self.guesses1}")
                if guess_input == "quit":
                    exit()
                elif guess_input[0] not in self.secret_word and guess_input != "letters":
                    self.lives -= 1
                    if self.lives == 0:
                        break
                    else:
                        self.my_turn = False
                        computer.my_turn = True

            # computer turn

            if computer.my_turn is True:

                comp_guess = computer.computer_makes_choice()
                while comp_guess in computer.guesses2:
                    comp_guess = computer.computer_makes_choice()
                print(f"{computer.name} guesses the letter: {comp_guess}")
                if comp_guess not in computer.guesses2:
                    computer.guesses2.append(comp_guess)
                    self.my_turn = True
                    computer.my_turn = False
                elif comp_guess not in computer.secret_word:
                    self.my_turn = True
                    computer.my_turn = False

            self.completed = True
            for letter in self.secret_word:
                self.score += 5
                if letter.lower() not in self.guesses1:
                    self.score -= 5
                    self.completed = False
            computer.completed = True
            for letter in computer.secret_word:
                computer.score += 5
                if letter.lower() not in computer.guesses2:
                    computer.score -= 5
                    computer.completed = False

        print()

        self.calculate_score(computer1)

        # calculate score and end message

    def create_secret_word(self, other):

        if self.select_difficulty == "Easy":
            self.secret_word = choice(word).lower()
            other.secret_word = choice(word).lower()
            while len(self.secret_word) >= 5:
                self.secret_word = choice(word).lower()
                other.secret_word = choice(word).lower()
        if self.select_difficulty == "Normal":
            self.secret_word = choice(word).lower()
            other.secret_word = choice(word).lower()
            while len(self.secret_word) < 5:
                self.secret_word = choice(word).lower()
                other.secret_word = choice(word).lower()
        if self.select_difficulty == "Hard":
            self.secret_word = choice(word).lower()
            other.secret_word = choice(word).lower()
            while len(self.secret_word) < 7:
                self.secret_word = choice(word).lower()
                other.secret_word = choice(word).lower()
        if self.select_difficulty == "Test":
            self.secret_word = choice(word).lower()
            other.secret_word = choice(word).lower()
            while len(self.secret_word) < 7:
                self.secret_word = choice(word).lower()
                other.secret_word = choice(word).lower()

    def calculate_score(self, other):

        if self.completed is False and other.completed is True:
            self.score = (self.lives * 10 + self.score) * self.diff_multi
            print(f"Game Over, {self.name}! the word was '{self.secret_word.upper()}'!\n"
                  f"total score: {self.score}\non difficulty: {self.select_difficulty}"
                  )

        if self.completed is True and other.completed is False:
            self.score = (self.lives * 10 + self.score) * self.diff_multi + self.win_bonus
            print(f"Congratulations, {self.name}, you completed the word '{self.secret_word.upper()}'!\n"
                  f"total score: {self.score}\non difficulty: {self.select_difficulty}"
                  )

        if self.completed is False and other.completed is False:
            self.score = (self.lives * 10 + self.score) * self.diff_multi + self.win_bonus
            print(f"Game ends! {self.name}, your word was '{self.secret_word.upper()}'!\n"
                  f"total score: {self.score}\non difficulty: {self.select_difficulty}"
                  )

        if other.completed is False:
            other.score = (other.lives * 10 + other.score) * self.diff_multi

        if other.completed is True:
            other.score = (other.lives * 10 + other.score) * self.diff_multi + self.win_bonus

        print(f"{self.name} : {self.score}\n"
              f"{other.name} : {other.score}\n"
              )

        if self.score > other.score:
            print(f"{self.name} wins!")
        if self.score < other.score:
            print(f"{other.name} wins!")
        if self.score == other.score:
            print("it's a tie!")

        self.update_high_scores()

    def computer_makes_choice(self):

        comp_pick = choices(self.comp_alphabet, weights=(0.27, 0.29, 1.00, 4.53, 1.00, 2.07, 6.65, 3.01, 8.49,
                                                         5.73, 1.81, 2.47, 3.00, 0.19, 5.48, 0.19, 1.28,
                                                         11.16, 7.58, 6.95, 1.77, 3.63, 7.54, 7.16, 3.16), k=1)
        comp_pick = "".join(comp_pick)
        return comp_pick

    def update_high_scores(self):
        """
        Attempts to load the highscore.txt and append the new score, datetime included.
        :return:
        """

        try:
            with open('highscore.txt', 'r') as f:
                highscores = load(f)
                now = datetime.now()
                now_string = now.strftime("%d/%m/%Y %H:%M:%S")

                highscores.append((self.name, self.score, self.select_difficulty, now_string))
                highscores = sorted(highscores, key=itemgetter(1), reverse=True)[:10]

                with open('highscore.txt', 'w') as f1:
                    dump(highscores, f1)

        except FileNotFoundError:
            print("\ncreating high score...")
            highscores = [["Bubbleboy", 500], ["Salami", 600], ["Riskitforabiscuit", 700],
                          ["Champ", 800], ["MasterNitroBlaster", 900], ["Omegasimp", 1000]]

            now = datetime.now()
            now_string = now.strftime("%d/%m/%Y %H:%M:%S")

            highscores.append((self.name, self.score, self.select_difficulty, now_string))
            highscores = sorted(highscores, key=itemgetter(1), reverse=True)[:10]

            with open('highscore.txt', 'w') as f:
                dump(highscores, f)

        input("\npress Enter to continue...\n")

    def choose_difficulty(self):

        while True:
            try:
                self.select_difficulty = int(input("choose difficulty:\n1.Easy (10 lives, small words)"
                                                   "\n2.Normal (7 lives, average size words)"
                                                   "\n3.Hard (5 lives, large size words only)\n"))
                if self.select_difficulty == 1:
                    self.select_difficulty = "Easy"
                elif self.select_difficulty == 2:
                    self.select_difficulty = "Normal"
                elif self.select_difficulty == 3:
                    self.select_difficulty = "Hard"
                elif self.select_difficulty == 9:
                    self.select_difficulty = "Test"

            except ValueError:
                print("please use an integer.")

            break

        self.set_player_values()

    def set_player_values(self):
        if self.select_difficulty == "Easy":
            self.lives = 10
            self.score = 0
            self.diff_multi = 0.5
            self.win_bonus = 100

        elif self.select_difficulty == "Normal":
            self.lives = 7
            self.score = 0
            self.diff_multi = 1
            self.win_bonus = 200

        elif self.select_difficulty == "Hard":
            self.lives = 5
            self.score = 0
            self.diff_multi = 2
            self.win_bonus = 300

        elif self.select_difficulty == "Test":
            self.lives = 99999
            self.score = -99999
            self.diff_multi = -99999
            self.win_bonus = -99999

        self.guesses1 = []
        self.guesses2 = []
        self.completed = False
        self.my_turn = False

    def display_high_score(self):
        """
        Attempts to read the highscore.txt file for printing.
        If unable to find, triggers create_high_score() method.
        :return:
        """
        high_score_title = "HIGH SCORE:"
        print(f"{high_score_title:>50}\n")
        try:
            with open('highscore.txt', 'r') as readf:
                highscores = load(readf)
                for index, sco in enumerate(highscores):
                    string_sco = f"{index + 1}.{str(sco[0])} : {str(sco[1]).zfill(4)}"
                    print(f"{string_sco:>50}")
                    if index == 10:
                        break

            input("\nPress Enter to continue...")

        except FileNotFoundError:
            print("file not found. creating...\n")
            self.create_high_score()

    @staticmethod
    def create_high_score():
        """
        Upon not finding a highscore.txt file, this method will create it.
        :return:
        """

        try:
            highscores = [["Bubbleboy", 500], ["Salami", 600], ["Riskitforabiscuit", 700],
                          ["ghostwiththemost", 800], ["MasterNitroBlaster", 900], ["OmegaSimp", 1000]]
            highscores = sorted(highscores, key=itemgetter(1), reverse=True)[:10]
            with open('highscore.txt', 'w') as writef:
                dump(highscores, writef)

            with open('highscore.txt', 'r') as readf:
                highscores = load(readf)
                for index, sco in enumerate(highscores):
                    string_sco = f"{index + 1}.{str(sco[0])} : {str(sco[1]).zfill(4)}"
                    print(f"{string_sco:>50}")
                    if index == 10:
                        break
        except PermissionError:
            print("you don't have permission to create this file!")
        except FileExistsError:
            print("file already exists.\n")

        print("created new high score file!")


player1 = Hangman()
computer1 = Hangman()
computer1.name = "Computer"

if __name__ == "__main__":
    while True:
        player1.hangman_menu()
