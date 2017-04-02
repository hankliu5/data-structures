from Queue import Queue
from Stack import Stack


class Location:
    """Records the location

    Attributes:
        __row: the row location
        __col: the column location
    """

    def __init__(self, currRow, currCol):
        """Initializes the Location object with row and column"""
        self.__row = currRow
        self.__col = currCol

    def getRow(self):
        """Returns objects row location"""
        return self.__row

    def getCol(self):
        """Returns objects column location"""
        return self.__col

    def left(self):
        """Returns the left location of current object location"""
        return Location(self.__row, self.__col - 1)

    def right(self):
        """Returns the right location of current object location"""
        return Location(self.__row, self.__col + 1)

    def up(self):
        """Returns the up location of current object location"""
        return Location(self.__row - 1, self.__col)

    def down(self):
        """Returns the down location of current object location"""
        return Location(self.__row + 1, self.__col)


class DarkRoom:

    def __init__(self):
        """Initializes a DarkRoom object.

        A DarkRoom object contains a list that stores the details of the
        darkroom, and two integer variables stores the numbers of rows and
        columns.
        """
        self.__darkRoom = []
        self.__numCols = 0
        self.__numRows = 0

    def readFromFile(self, filename):
        """Reads the room from file.

        Reads the details of the room from the file, and records the details,
        such as the walls, the starting point, the escape door, the numbers of
        columns and rows into object's variables.

        Args:
            filename: the name of the file contains the room.
        """
        header = False
        inputfile = open(filename)

        for line in inputfile:
            if header is False:
                self.__numRows = int(line.split()[0])
                self.__numCols = int(line.split()[1])
                header = True
                continue
            else:
                self.__darkRoom.append(list(line.strip('\n')))

    def findStart(self):
        """finds out the start point from the room.

        Returns:
            A Location object contains the location of the start point.
        """
        for i in range(0, self.__numRows):
            for j in range(0, self.__numCols):
                if self.__darkRoom[i][j] == 'S':
                    return Location(i, j)

        return None

    def isDoor(self, loc):
        """Returns a Bool that the location is whether a door or not."""
        return self.__darkRoom[loc.getRow()][loc.getCol()] == 'D'

    def canMove(self, loc):
        """Returns a Bool that the location is whether available or not."""
        return self.__darkRoom[loc.getRow()][loc.getCol()] == ' '

    def markVisited(self, loc):
        """Marks a dot that indicates we've visited the location"""
        if self.__darkRoom[loc.getRow()][loc.getCol()] == ' ':
            self.__darkRoom[loc.getRow()][loc.getCol()] = '.'

    def countVisited(self):
        """Returns the count of visited marks in the room."""
        count = 0
        for line in self.__darkRoom:
            for char in line:
                if char == '.':
                    count += 1
        return count

    def clear(self):
        """Clears the marked location."""
        for i, line in enumerate(self.__darkRoom):
            for j, char in enumerate(line):
                if char is '.':
                    self.__darkRoom[i][j] = ' '

    def escapeDarkroom(self, choice):
        """Finds out the path to the door to escape the dark room.

        Uses depth-first search (stack) or breadth-first search (queue) to find
        out a path to the door. When the door is found, prints out the result.

        Args:
            choice: A string indicating which structure is going to be used.
        """
        self.storage = None
        if choice == 'queue':
            self.storage = Queue()
        elif choice == 'stack':
            self.storage = Stack()

        start = self.findStart()
        if start is None:
            print('Cannot find out the start.')
            return
        self.storage.add(start)
        while self.storage.size() != 0:
            current = self.storage.remove()
            self.markVisited(current)

            if self.__check(current.left(), choice) is True:
                return
            if self.__check(current.up(), choice) is True:
                return
            if self.__check(current.right(), choice) is True:
                return
            if self.__check(current.down(), choice) is True:
                return

    def printRoom(self):
        """Prints out what the room looks like"""
        for row in self.__darkRoom:
            print(''.join(row))

    def __check(self, loc, choice):
        """Checks the status of current location

        Checks the status of current location. If it is available for moving,
        it should be added to the storage. If it is a door, the program should
        print out the result.

        Args:
            loc: the Location object which is going to be checked.
            choice: A string indicating which structure is going to be used.

        Returns:
            Returns True if loc is the door; otherwise return false.
        """
        if self.canMove(loc) is True:
            self.storage.add(loc)
        elif self.isDoor(loc) is True:
            self.__printGoal(choice, self.countVisited(), self.storage.size())
            self.printRoom()
            return True
        return False

    def __printGoal(self, choice, stepsTaken, positionsLeft):
        """Prints out the format of the result.

        Args:
            choice: A string indicating which structure is going to be used.
            stepsTaken: How many marks in the room, counted by countVisited()
                function.
            positionsLeft: How many Locations objects are still in the storage.
        """
        print("Goal found (with " + choice + "): It took " +
              repr(stepsTaken) + " explored positions")
        print("There is (are) " + repr(positionsLeft) +
              " position(s) left to explore in " + choice)
