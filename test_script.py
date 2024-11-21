# test_your_script.py
import unittest
from app import add, subtract

class test(unittest.TestCase):
    
    def test_add():
        assert add(2, 3) == 5

    def test_subtract():
        assert subtract(5, 3) == 2
if __name__=="__main__":
    unittest.main()
