import unittest
import multiplication

class TestTable(unittest.TestCase):

    def test_kakezan(self):
        value1 = 3
        value2 = 5
        expected = [[1, 2, 3], [2, 4, 6,], [3, 6, 9], [4, 8, 12], [5, 10, 15]] 
        actual = multiplication.kakezan(value1, value2) #run kakezan()
        self.assertEqual(expected, actual) #compare expected with actual result
        
    def test_tashizan(self):
        value1 = 3
        value2 = 5
        expected = [[2, 3, 4],[3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8]]
        actual = multiplication.tashizan(value1, value2) #run kakezan()
        self.assertEqual(expected, actual) #compare expected with actual result
            

if __name__ == "__main__":
    unittest.main()
    