import unittest
from datetime import datetime

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.test_string = "Python Testing"
    
    def test_upper(self):
        """Test string upper method"""
        self.assertEqual(self.test_string.upper(), "PYTHON TESTING")
    
    def test_split(self):
        """Test string split method"""
        self.assertEqual(self.test_string.split(), ["Python", "Testing"])
    
    def test_strip(self):
        """Test string strip method"""
        padded_string = "  python  "
        self.assertEqual(padded_string.strip(), "python")

class TestDateTimeMethods(unittest.TestCase):
    def test_date_comparison(self):
        """Test datetime comparison"""
        date1 = datetime(2024, 1, 1)
        date2 = datetime(2024, 1, 2)
        self.assertLess(date1, date2)
    
    def test_date_attributes(self):
        """Test datetime attributes"""
        date = datetime(2024, 12, 31, 23, 59, 59)
        self.assertEqual(date.year, 2024)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.day, 31)

if __name__ == '__main__':
    unittest.main()
