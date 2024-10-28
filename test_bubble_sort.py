import unittest
import bubble_sort


class TestBubbleSort(unittest.TestCase):

    def test_bubble_sort(self):
        result = [2, 1, 69, 3, 8, 4]
        bubble_sort.bubble_sort(result)
        self.assertEqual(result, [1, 2, 3, 4, 8, 69])


if __name__ == '__main__':
    unittest.main()
