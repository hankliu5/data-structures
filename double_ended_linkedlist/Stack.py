from DoubleEndedLinkedList import DoubleEndedLinkedList


class Stack:
    """Implemented stack with DoubleEndedLinkedList"""

    def __init__(self):
        self.ls = DoubleEndedLinkedList()

    def isEmpty(self):
        return self.ls.isEmpty()

    def add(self, element):
        self.ls.addFirst(element)

    def remove(self):
        return self.ls.removeFirst()

    def size(self):
        return self.ls.size()
