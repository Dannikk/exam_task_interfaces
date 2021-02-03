import unittest

from src import directory_reader as dr

class Test(unittest.TestCase):
    def test_main(self):
        with dr.DirReader("data") as file_names:
            for file_name in file_names:
                self.assertTrue(len(file_name) < 11)
