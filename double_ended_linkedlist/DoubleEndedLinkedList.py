class DoubleEndedLinkedList:

    def __init__(self):
        self.__nelems = 0
        self.__head = None
        self.__tail = None

    def isEmpty(self):
        return self.__nelems == 0

    def size(self):
        return self.__nelems

    def addFirst(self, element):
        if element is None:
            raise TypeError('The input element is NoneType')

        newNode = Node(element)
        if self.__nelems == 0:
            self.__head = self.__tail = newNode

        else:
            newNode.setNext(self.__head)
            self.__head = newNode

        self.__nelems += 1

    def addLast(self, element):
        if element is None:
            raise TypeError('The input element is NoneType')

        newNode = Node(element)
        if self.__nelems == 0:
            self.__head = self.__tail = newNode

        else:
            self.__tail.setNext(newNode)
            self.__tail = newNode

        self.__nelems += 1

    def removeFirst(self):
        if self.__nelems == 0:
            raise BaseException('Empty List')

        temp = self.__head
        if self.__nelems == 1:
            self.__head = self.__tail = None

        else:
            self.__head = temp.getNext()
            temp.setNext(None)

        self.__nelems -= 1

        return temp.getData()

    def removeLast(self):
        if self.__nelems == 0:
            raise BaseException('Empty List')

        temp = self.__tail

        if self.__nelems == 1:
            self.__head = self.__tail = None

        else:
            curr = self.__head
            while curr.getNext().getNext() is not None:
                curr = curr.getNext()

            curr.setNext(None)
            self.__tail = curr

        self.__nelems -= 1
        return temp.getData()


class Node:

    def __init__(self, element):
        self.__data = element
        self.__next = None

    def getNext(self):
        return self.__next

    def setNext(self, nextNode):
        self.__next = nextNode

    def getData(self):
        return self.__data
