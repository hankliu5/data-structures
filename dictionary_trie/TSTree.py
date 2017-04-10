from TSTNode import TSTNode


class TSTree:
    """The ternary tree stores characters for the trie.

    Attributes:
        __root: the root of the tree.
    """

    def __init__(self):
        self.__root = None

    def insert(self, string: str, freq: int) -> (bool):
        """Inserts the string into the tree.

        Returns:
            if the word hasn't existed in the tree, returns Tree; otherwise
            returns False.
        """

        # if root is None
        if self.__root is None:
            self.__root = TSTNode(string[0])
            curr = self.__root
            for c in string[1:]:
                curr.mid = TSTNode(c)
                curr = curr.mid
            curr.end_of_word = True
            curr.string = string
            curr.freq = freq
            return True
        else:
            curr = self.__root
            parent = self.__root
            for char in string:

                # when curr refers to None, means we found the place to insert.
                if curr is None:
                    parent.mid = TSTNode(char)
                    parent = parent.mid
                    continue

                # finds the place to insert.
                while curr is not None and curr.c != char:
                    if curr.c < char:
                        parent = curr
                        curr = curr.right
                    elif curr.c > char:
                        parent = curr
                        curr = curr.left

                # if curr becomes None, that means we found a place to insert.
                if curr is None:
                    curr = TSTNode(char)
                    if parent.c < char:
                        parent.right = curr
                    elif parent.c > char:
                        parent.left = curr
                    else:
                        parent.mid = curr
                parent = curr
                curr = curr.mid

            parent.string = string
            parent.freq = freq
            # if the flag has already been True, that mean we inserted the word
            # before.
            if parent.end_of_word is True:
                return False
            else:
                parent.end_of_word = True
                return True

    def find(self, string: str) -> (bool):
        """Finds the word in the tree.

        Returns:
            returns True if found in the tree; otherwise returns False.
        """

        # null check
        if self.__root is None:
            return False
        curr = self.__root
        parent = self.__root
        for char in string:
            while curr is not None and curr.c != char:
                parent = curr
                if char < curr.c:
                    curr = curr.left
                elif curr.c < char:
                    curr = curr.right
            if curr is None:
                return False
            else:
                parent = curr
                curr = curr.mid
        return parent.end_of_word

    def findNode(self, word: str, ht: dict) -> (TSTNode):
        # Null check
        if self.__root is None:
            return None

        curr = self.__root
        parent = self.__root
        for char in word:
            while curr is not None and curr.c != char:
                parent = curr
                if char < curr.c:
                    curr = curr.left
                elif curr.c < char:
                    curr = curr.right
            if curr is None:
                return None
            else:
                parent = curr
                curr = curr.mid

        if parent.end_of_word is True:
            ht[parent.string] = parent.freq

        return curr

    def dfs(self, node: TSTNode, ht: dict):
        if node is None:
            return
        if node.end_of_word is True:
            ht[node.string] = node.freq
            self.dfs(node.mid, ht)
            self.dfs(node.left, ht)
            self.dfs(node.right, ht)
