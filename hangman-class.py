import random

class Hangman:
    def __init__(self, word_list):
        self.word_list = word_list
        self.chosen_word = list(random.choice(self.word_list))
        self.blank_list = ["_"] * len(self.chosen_word)
        self.update_display = 0
        self.max_tries = 6

    def making_a_guess(self, guess):
        correct_guess = False
        for x, letter in enumerate(self.chosen_word):
            if guess.lower() == letter:
                self.blank_list[x] = guess.lower()
                correct_guess = True
        if not correct_guess:
            print(f"There is no {guess}, sorry.")
        return correct_guess

    def display(self):
        print(f"\n{self.HANGMANPICS[self.update_display]}")
        print(''.join(self.blank_list))

    def play(self):
        self.display()

        while self.update_display < self.max_tries:
            guess = input("Make a guess: ")
            correct_guess = self.making_a_guess(guess)
            
            if correct_guess:
                print("Good guess!")
            else:
                self.update_display += 1
            
            self.display()

            if self.blank_list == self.chosen_word:
                print("YOU WIN!")
                break

            if self.update_display == self.max_tries:
                print("GAME OVER.")
                break

    HANGMANPICS = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
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
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']


word_list = ["aardvark", "baboon", "camel", "jazz", "grass", "follow", "castle", "cloud"]
game = Hangman(word_list)
game.play()
