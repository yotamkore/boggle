import boggle_board_randomizer as bbr
from tkinter import *
from screen import ScreenUI
from screen import ScreenLogic

BOARD_SIZE = 4


class Game:

    SCORE = 0

    def __init__(self, parent):
        self.parent = parent

        # words_from_given_text
        self.__words = self.__get_words_from_txt()

        # Screen Logic Object
        self.screen_logic = ScreenLogic(self.__words)

        # Screen UI Object
        self.screen_ui = ScreenUI(self.parent, self.screen_logic)

        # letters and cords from given letters list
        # self.__letters_and_places_dict = self.__make_lst_to_dict()

        # pressed buttons
        self.__pressed_buttons_places = []

        # current word
        self.__current_word = ''

        # words found
        self.__words_found = []

    @ staticmethod
    def __get_words_from_txt():
        with open("boggle_dict.txt") as file:
            words = list(line.rstrip() for line in file)
        return words

    def submit_word(self):
        if self.__current_word in self.__words:
            if self.__current_word not in self.__words_found:
                self.__words_found.append(self.__current_word)
                self.__current_word = ''
                self.__pressed_buttons_places = []


if __name__ == '__main__':
    parent = Tk()
    game = Game(parent)
    parent.mainloop()



