# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 11:07:19 2018

@author: William
"""

import unittest
from maths.Add import Add
from maths.Subtract import Subtract

class TestMaths(unittest.TestCase):
    def test_Add(self):
        temp = Add(2,3)
        self.assertEqual(temp.evaluate(), 5)
        
    def test_Subtract(self):
        temp = Subtract(3,2)
        self.assertEqual(temp.evaluate(), 1)
        
    
if __name__ == '__main__':
    unittest.main()