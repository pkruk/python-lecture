import unittest

from sorting import *

class TestSort(unittest.TestCase):

    def test_empty_insert(self):
        tmp = []
        InsertionSort()(tmp)
        return self.assertEqual(tmp, [])

    def test_empty_selection(self):
        tmp = []
        SelectionSort()(tmp)
        return self.assertEqual(tmp, [])

    def test_singleton_insert(self):
        tmp = [1]
        InsertionSort()(tmp)
        return self.assertEqual(tmp, [1])

    def test_singleton_select(self):
        tmp = [1]
        SelectionSort()(tmp)
        return self.assertEqual(tmp, [1])

unittest.main()
