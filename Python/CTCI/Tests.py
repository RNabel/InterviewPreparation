import unittest
from Contacts import find, add

class Tests(unittest.TestCase):
    def testContactsSingle(self):
        trie = [0, {}]
        self.assertEqual(0, find("h", trie))
        add("hi", trie)
        self.assertEqual(1, find("h", trie))
        self.assertEqual(1, find("hi", trie))

    def testContactsMultiple(self):
        trie = [0, {}]
        add("hi", trie)
        self.assertEqual(1, find("h", trie))
        add("ha", trie)
        self.assertEqual(2, find("h", trie))
        self.assertEqual(1, find("hi", trie))
        self.assertEqual(1, find("ha", trie))

    def testEmpty(self):
        trie = [0, {}]
        add("hi", trie)
        res = find("bla", trie)
        self.assertEqual(0, res)
