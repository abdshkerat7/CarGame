



class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """

    def __init__(self):
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # implement your code and erase the "pass"
        self._num_cars = 0
        self._cur_board = self._helper_get_board()
        self._length = 7
        self.dec_car = {} # car_name : [car, orientation]
        self._cell_list = self.cell_list()


    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.
        # implement your code and erase the "pass"
        string_board = ""
        i = 0
        while i < self._length:
            x = "".join(self._cur_board[i])
            string_board += x
            string_board += '\n'
            i += 1
        return string_board

    def _helper_get_board(self):
        board = [["_ " for i in range(7)] for j in range(7)]
        return board


    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        # implement your code and erase the "pass"
        cells = [(i, j) for i in range(7) for j in range(7)]
        cells.append(self.target_location())
        return cells



    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,move_key,description)
                 representing legal moves
        """
        # From the provided example car_config.json file, the return value could be
        # [('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]
        # implement your code and erase the "pass"
        lst = []
        for car_name, car in self.dec_car.items():
            lst_possible_move = []
            for move_key in car.possible_moves().keys():
                for target in car.movement_requirements(move_key):
                    if target in self._cell_list:
                        if self.cell_content(target) is None:
                            car_name = car.get_name()
                            desc = car.possible_moves()[move_key]
                            lst_possible_move.append((car_name,
                                                      move_key, desc))
            for pos in lst_possible_move:
                lst.append(pos)
        return lst


    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        # In this board, returns (3,7)
        # implement your code and erase the "pass"
        target = (3, 7)
        return target

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        # implement your code and erase the "pass"
        counter = 0
        for car_name, car in self.dec_car.items():
            if not self.check_coordinate(coordinate, car):
                counter += 1
            else:
                return car_name
        return None

    def check_coordinate(self, coordinate, car):
        if coordinate in car.car_coordinates():
            return True
        return False

    def add_new_car(self, car):
        for cor in self._cell_list:
            if cor != (3, 7):
                i, j = cor
                if self._cur_board[i][j] == car.get_name():
                    self._cur_board[i][j] = "_ "
                if cor in car.car_coordinates():
                    car_name = car.get_name()
                    self._cur_board[i][j] = car_name + " "

    def check_add_car_helper(self, car):
        if car.get_name() in self.dec_car:
            return False
        lst = car.car_coordinates()
        for cell in lst:
            if self.cell_content(cell):
                return False
            elif cell not in self._cell_list:
                return False
        return True

    def add_done(self, car):
        self.dec_car[car.get_name()] = car
        self.add_new_car(car)
        self._num_cars += 1

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # Remember to consider all the reasons adding a car can fail.
        # You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"
        if not self.check_add_car_helper(car):
            return False
        else:
            self.add_done(car)
            return True


    def check_if_car_move(self, name, move_key):
        if name not in self.dec_car:
            return False
        car = self.dec_car[name]
        if move_key not in car.possible_moves():
            return False
        lst = self.dec_car[name].movement_requirements(move_key)
        for i in range(len(lst)):
            if self.cell_content(lst[i]):
                return False
            elif lst[i] not in self._cell_list:
                return False
        return True


    def check_move_car(self, car, move_key):
        if not car.move(move_key):
            return False
        self.add_new_car(car)
        return True


    def move_car(self, name, move_key):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param move_key: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        if not self.check_if_car_move(name, move_key):
            return False
        car = self.dec_car[name]
        cur_coord = car.car_coordinates()
        if not self.check_move_car(car, move_key):
            return False
        for cell in cur_coord:
            if cell not in car.car_coordinates():
                if cell != (3, 7):
                    i, j = cell
                    self._cur_board[i][j] = "_ "
        return True





