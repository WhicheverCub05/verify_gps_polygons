import unittest
import main


class TestPolygons(unittest.TestCase):
    
    def test_if_correct(self):
        # works 
        self.assertEqual(main.provideSolutions([[7, 8], [5, 15], [3, 15], [2, 4]]), [[7, 8], [5, 15], [3, 15], [2, 4]])
        # doesn't work 
        self.assertEqual(main.provideSolutions([[7, 8], [5, 15], [2, 4], [3, 15]]), [[7, 8], [5, 15], [3, 15], [2, 4]])


if __name__ == '__main__':
    unittest.main()