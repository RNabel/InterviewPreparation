import unittest
from Contacts import find, add
from Python.CTCI.TrackingRunningMedian import RunningMedian


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

    def testMeanSingle(self):
        med = RunningMedian()
        med.add(12)
        self.assertEqual(12, med.get_median())

    def testMeanEvenTwo(self):
        med = RunningMedian()
        med.add(12)
        med.add(13)
        self.assertEqual(12.5, med.get_median())

    def testOddThree(self):
        med = RunningMedian()
        med.add(10)
        med.add(11)
        med.add(14)
        self.assertEqual(11, med.get_median())

    def testEvenFour(self):
        med = RunningMedian()
        med.add(10)
        med.add(12)
        med.add(16)
        med.add(22)
        self.assertEqual(14, med.get_median())
