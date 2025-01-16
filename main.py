import random

class BingGame:
    player_list = []
    def __init__(self):
        self.name = input("enter your name : ")
        self.__rand_number = random.randint(0,10)
        self.__guess_left = 3
        self.__win_state = False
        self.player_list.append(self)


    def check_answer(self, answer):
        if answer == self.__rand_number:
            self.__win_state = True
            return True
        elif answer > self.__rand_number:
            print("Too high")
            self.__guess_left -= 1
            return False
        else:
            print("Too low")
            self.__guess_left -= 1
            return False

if __name__ == "__main__":
    while True:
        user = BingGame()
        print(BingGame.player_list)
        print({user.name},{user.rand_number},{user.guess_left})
