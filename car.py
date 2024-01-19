


class Car:
    """
    Add class description here
    """
    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        # Note that this function is required in your Car implementation.
        # implement your code and erase the "pass"
        self._name = name           # the car name
        self._length = length       # poss 2-4
        self._location = location   #( car head (row, col))
        self._orientation = orientation   #(0 or 1)

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        # implement your code and erase the "pass"
        lst_car_cor = []
        x = self._location[0]
        y = self._location[1]
        for i in range(self._length):
            cell = (x, y)
            if self._orientation == 1:
                lst_car_cor.append(cell)
                y += 1
            else:
                lst_car_cor.append(cell)
                x += 1
        return lst_car_cor


    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        # For this car type, keys are from 'udrl'
        # The keys for vertical cars are 'u' and 'd'.
        # The keys for horizontal cars are 'l' and 'r'.
        # You may choose appropriate strings.
        # implement your code and erase the "pass"
        # The dictionary returned should look something like this:
        # result = {'f': "cause the car to fly and reach the Moon",
        #          'd': "cause the car to dig and reach the core of Earth",
        #          'a': "another unknown action"}
        # A car returning this dictionary supports the commands 'f','d','a'.
        # implement your code and erase the "pass"
        if self._orientation == 0:
            return {
                'u': 'go up',
                'd': 'go down'
            }
        else:
            return {
                'r': 'go right',
                'l': 'go left'
            }


    def movement_requirements(self, move_key):
        """ 
        :param move_key: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        # For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        # be empty in order to move down (with a key 'd').
        # implement your code and erase the "pass"
        lst_requires_cor = []
        x = self._location[0]
        y = self._location[1]
        if self._orientation == 0:
            if move_key == 'u':
                cell = (x - 1, y)
                lst_requires_cor.append(cell)
            else:
                x = self.car_coordinates()[-1][0]
                y = self.car_coordinates()[-1][1]
                cell = (x + 1, y)
                lst_requires_cor.append(cell)
        else:
            if move_key == 'r':
                x = self.car_coordinates()[-1][0]
                y = self.car_coordinates()[-1][1]
                cell = (x, y + 1)
                lst_requires_cor.append(cell)
            else:
                cell = (x, y - 1)
                lst_requires_cor.append(cell)
        return lst_requires_cor


    # هان يمكن بدهمش نفحص اذا في عالبورد سيارة أو لا وبكفي نفحص انه أعطى حرف مناسب للاتجاه
    def move_helper(self, move_key):
        if move_key == 'u':
            x = self._location[0] - 1
            self._location = x, self._location[1]
        elif move_key == 'd':
            x = self._location[0] + 1
            self._location = x, self._location[1]
        elif move_key == 'r':
            x = self._location[1] + 1
            self._location = self._location[0], x
        else:
            x = self._location[1] - 1
            self._location = self._location[0], x
        return True

    def move(self, move_key):
        """ 
        :param move_key: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        if move_key not in self.possible_moves():
            return False
        else:
            return self.move_helper(move_key)


    def get_name(self):
        """
        :return: The name of this car.
        """
        # implement your code and erase the "pass"
        name = str(self._name)
        return name

    def get_orientation(self):
        return self._orientation

    def get_length(self):
        return self._length