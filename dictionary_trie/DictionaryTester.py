import unittest
from DictionaryHashset import DictionaryHashset
from DictionaryTrie import DictionaryTrie


class DictionaryTester(unittest.TestCase):

    def setUp(self):
        self.ls = ['basketball', 'asterisk', 'basket', 'application', 'a',
                   'app', 'gugglebee', 'waldos', 'are you not entertained',
                   'never gonna give you up']
        self.hs = DictionaryHashset()
        self.trie = DictionaryTrie()

    def testInsert(self):
        for word in self.ls:
            self.assertTrue(self.hs.insert(word))
            self.assertTrue(self.trie.insert(word))
        for word in self.ls:
            self.assertTrue(not self.hs.insert(word))
            self.assertTrue(not self.trie.insert(word))

    def testFind(self):
        for word in self.ls:
            self.hs.insert(word)
            self.trie.insert(word)
        for word in self.ls:
            self.assertTrue(self.hs.find(word))
            self.assertTrue(self.trie.find(word))


if __name__ == '__main__':
    unittest.main()
