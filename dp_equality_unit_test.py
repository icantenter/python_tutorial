from dp_equality import *
import sys
import unittest
arr = [3, 34, 4, 12, 5, 2]
arr2 = [2]

class Test(unittest.TestCase):
    def test_rec_subset(self):
        self.assertEqual(rec_subset(arr, len(arr) - 1, 9) ,True)
        self.assertEqual(rec_subset(arr, len(arr) - 1, 10), True)
        self.assertEqual(rec_subset(arr, len(arr) - 1, 11), True)
        self.assertEqual(rec_subset(arr, len(arr) - 1, 12), True)
        self.assertEqual(rec_subset(arr, len(arr) - 1, 13), False)

    def test_dp_subset(self):
        self.assertEqual(dp_subset(arr2, 2), True)
        self.assertEqual(dp_subset(arr, 9) ,True)
        self.assertEqual(dp_subset(arr, 10), True)
        self.assertEqual(dp_subset(arr, 11), True)
        self.assertEqual(dp_subset(arr, 12), True)
        self.assertEqual(dp_subset(arr, 13), False)

unittest.main()