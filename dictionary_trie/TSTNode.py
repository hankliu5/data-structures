class TSTNode:
    """Node class for the Ternary Search Tree (Trie).

    Attributes:
        __char: stores a character in the node
        __left: left child node
        __right: right child node
        __mid: middle child node
        __end_of_word: indicates the node is whether the end of word or not.
        __freq: the frequency of the word.
        __string: the string stored in the node.
    """

    def __init__(self, c):
        if len(c) != 1:
            raise AttributeError('more than 1 character')
        else:
            self.__char = c
            self.__left = None
            self.__right = None
            self.__mid = None
            self.__end_of_word = False
            self.__freq = 0
            self.__string = None

    # getters and setters
    @property
    def c(self):
        return self.__char

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, node):
        self.__left = node

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, node):
        self.__right = node

    @property
    def mid(self):
        return self.__mid

    @mid.setter
    def mid(self, node):
        self.__mid = node

    @property
    def end_of_word(self):
        return self.__end_of_word

    @end_of_word.setter
    def end_of_word(self, flag):
        self.__end_of_word = flag

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, string):
        self.__string = string

    @property
    def freq(self):
        return self.__freq

    @freq.setter
    def freq(self, freq):
        self.__freq = freq
