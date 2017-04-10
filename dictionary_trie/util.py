from DictionaryTrie import DictionaryTrie
import sys


def load_dict(d: DictionaryTrie):
    f = open('freq_dict.txt', 'r')
    for line in f:
        ls = line.split()
        d.insert(ls[1], int(ls[0]))


def main():
    trie = DictionaryTrie()
    load_dict(trie)
    trie.predictCompletions(sys.argv[1], int(sys.argv[2]))


if __name__ == '__main__':
    main()
