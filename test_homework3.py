import unittest
import os 
from homework3 import create_dataframe
from homework3 import checkColumnName
from homework3 import checkRowSize
from homework3 import checkKey

class create_dataframe_test(unittest.TestCase):
    """Tests for `Creation of dataframe`."""

    def test_checkColumnName(self):
        """Check if column Name is same """
        self.assertTrue(checkColumnName(create_dataframe("class.db")))  
    
    def test_checkRowSize(self):
        """Check Row Size """
        self.assertTrue(checkRowSize(create_dataframe("class.db"))) 
    
    def test_checkKey(self):
        """Check Key """
        self.assertTrue(checkKey(create_dataframe("class.db")))   

    def test_path(self):
        """Check Path """
        self.assertTrue(os.path.exists('./class.db')) 

if __name__ == '__main__':
    unittest.main()

