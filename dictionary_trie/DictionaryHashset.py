class DictionaryHashset:
    """Implemented by using set.

    Attributes:
        __s: set data structure
    """

    def __init__(self):
        self.__s = set()

    def insert(self, word: str) -> (bool):
        """inserts a word into a set and return a bool if it's successful."""
        if word in self.__s:
            return False
        else:
            self.__s.add(word)
            return True

    def find(self, word) -> (bool):
        """finds a word and return a bool if found in the set."""
        return word in self.__s
