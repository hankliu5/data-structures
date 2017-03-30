from Queue import Queue
from Stack import Stack


class Location:

    def __init__(self, currRow, currCol):
        self.__row = currRow
        self.__col = currCol

    def getRow(self):
        return self.__row

    def getCol(self):
        return self.__col

    def left(self):
        return Location(self.__row, self.__col - 1)

    def right(self):
        return Location(self.__row, self.__col + 1)

    def up(self):
        return Location(self.__row - 1, self.__col)

    def down(self):
        return Location(self.__row + 1, self.__col)


class DarkRoom:

    def __init__(self):
        self.__darkRoom = []
        self.__numCols = 0
        self.__numRows = 0

    def readFromFile(self, filename):
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
        for i in range(0, self.__numRows):
            for j in range(0, self.__numCols):
                if self.__darkRoom[i][j] == 'S':
                    return Location(i, j)

        return None

    def isDoor(self, loc):
        return self.__darkRoom[loc.getRow()][loc.getCol()] == 'D'

    def canMove(self, loc):
        return self.__darkRoom[loc.getRow()][loc.getCol()] == ' '

    def markVisited(self, loc):
        if self.__darkRoom[loc.getRow()][loc.getCol()] == ' ':
            self.__darkRoom[loc.getRow()][loc.getCol()] = '.'

    def countVisited(self):
        count = 0
        for line in self.__darkRoom:
            for char in line:
                if char == '.':
                    count += 1
        return count

    def clear(self):
        for i, line in enumerate(self.__darkRoom):
            for j, char in enumerate(line):
                if char is '.':
                    self.__darkRoom[i][j] = ' '

    def escapeDarkroom(self, choice):
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
        for row in self.__darkRoom:
            print(''.join(row))

    def __check(self, loc, choice):
        if self.canMove(loc) is True:
            self.storage.add(loc)
        elif self.isDoor(loc) is True:
            self.__printGoal(choice, self.countVisited(), self.storage.size())
            self.printRoom()
            return True
        return False

    def __printGoal(self, choice, stepsTaken, positionsLeft):
        print("Goal found (with " + choice + "): It took " +
              repr(stepsTaken) + " explored positions")
        print("There is (are) " + repr(positionsLeft) +
              " position(s) left to explore in " + choice)
