import sys
from board import *
from car import *
from helper import *

NAMES = ["B", "O", "G", "W", "Y", "R"]


class Game:
    """
    Add class description here
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        # You may assume board follows the API
        # implement your code and erase the "pass"
        self._board = board
        self._num_of_games = 0


    def check_if_stop_game(self, user_input):
        if user_input == '!':
            return False
        return True

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        # implement your code and erase the "pass"
        user_input = input("please enter correct input")
        if not self.check_if_stop_game(user_input):
            return False
        lst_input = user_input.split(',')
        length = len(lst_input)
        if length != 2:
            print("incorrect input")
            return True
        else:
            car, dir = lst_input[0], lst_input[1]
            move = self._board.move_car(car, dir)
            if not move:
                print("invalid move, check your board")
                return True
            else:
                print("the car moved")
                return True


    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        # implement your code and erase the "pass"
        while True:
            if self._board.cell_content(self._board.target_location()) is not None:
                break
            else:
                print(self._board)
                if not self.__single_turn():
                    end_game = "you finished"
                    print(end_game)
                    return
        win_game = "you win"
        string_win = "yes!"
        print(string_win)
        print(self._board)
        print(win_game)

def add_car_to_board(board, all_data):
    for data in all_data:
        if data in NAMES:
            if 2 <= all_data[data][0] <= 4:
                if all_data[data][2] == 0 or all_data[data][2] == 1:
                    car_name = data
                    car_length = all_data[data][0]
                    car_location = (all_data[data][1][0], all_data[data][1][1])
                    car_orientation = all_data[data][2]
                    car = Car(car_name, car_length, car_location, car_orientation)
                    board.add_car(car)


if __name__== "__main__":
    # Your code here
    # All access to files, non API constructors, and such must be in this
    # section, or in functions called from this section.
    # implement your code and erase the "pass"
    ask_json = "please add just a jason file"
    if len(sys.argv) != 2:
        print(ask_json)
    else:
        board = Board()
        json_file = sys.argv[1]
        all_data = load_json(json_file)
        add_car_to_board(board, all_data)
        game = Game(board)
        game.play()

