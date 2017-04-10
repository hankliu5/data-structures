from TSTree import TSTree
import operator


class DictionaryTrie:
    """Implemented by using Ternary Search Tree.

    Attributes:
        __trie: tstree data structure.
    """

    def __init__(self):
        self.__trie = TSTree()

    def insert(self, word: str, freq=0) -> (bool):
        """inserts a word into trie and return a bool if it's successful."""
        return self.__trie.insert(word, freq)

    def find(self, word: str) -> (bool):
        """finds a word and return a bool if found in the trie."""
        return self.__trie.find(word)

    def predictCompletions(self, prefix: str, num_completions=10) -> (list):
        if len(prefix) == 0:
            raise AttributeError('the length of prefix shouldn\'t be zero')
        ht = dict()
        ls = list()

        self.__trie.dfs(self.__trie.findNode(prefix, ht), ht)
        sorted_ht = sorted(ht.items(), key=operator.itemgetter(1))
        sorted_ht.reverse()
        for i in range(0, min(num_completions, len(sorted_ht))):
            ls.append(sorted_ht[i][0])
        print(ls)
