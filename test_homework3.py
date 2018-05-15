import unittest
import os
from homework3 import create_dataframe
#from homework3 import checkColumnName
#from homework3 import checkRowSize
#from homework3 import checkKey

df = create_dataframe("class.db")

class create_dataframe_test(unittest.TestCase):
    """Tests for `Creation of dataframe`."""

    def test_checkColumnName(self):
        """Check if column Name is same """
        self.assertTrue(set(['video_id', 'language', 'category_id']).issubset(set(list(df))))

    def test_checkRowSize(self):
        """Check Row Size """
        self.assertTrue(df.shape[0]>=10)

    def test_checkKey(self):
        """Check Key """
        self.assertTrue(df.shape[0] == len(set(df['video_id'].map(str) + df["language"].map(str))))
        #df.shape[0] = len(set(df['video_id'].map(str) + df["language"].map(str)))

    def test_path(self):
        """Check Path """
        self.assertRaises(ValueError,create_dataframe,"Please Provide correct path")



if __name__ == '__main__':
    unittest.main()
