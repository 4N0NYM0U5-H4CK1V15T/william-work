# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 11:07:19 2018

@author: William
"""

import unittest
from maths.Add import Add            #Imports other classes
from maths.Subtract import Subtract
from maths.Multiply import Multiply
from parser.tokens import tokens


class TestMaths(unittest.TestCase):
    def test_Add(self):
        temp = Add(2,3)
        self.assertEqual(temp.evaluate(), 5)    #(this part is what is executed, this part is what it should be)
        
    def test_Subtract(self):
        temp = Subtract(3,2)
        self.assertEqual(temp.evaluate(), 1)
        
    def test_Multiply(self):
        temp = Multiply(3,2)
        self.assertEqual(temp.evaluate(), 6)
        
    def test_Divide(self):
        temp = Divide(3,2)
        self.assertEqual(temp.evaluate(), 1.5)
        
    def test_Strings(self):         #not accually needed
        temp = Add("2","3")
        self.assertEqual(temp.evaluate(), 5)
        self.assertEqual(Add("2",3).evaluate(), 5)
    
    def test_Expressions(self):
        temp = Add(2,Multiply(3,4))
        self.assertEqual(temp.evaluate(), 14)
        
    def test_Str(self):
        temp = Add(2,3)
        self.assertEqual(str(temp), "(2 + 3)")
        self.assertEqual(str(Subtract(5,6)), "(5 - 6)")
        self.assertEqual(str(Subtract(5,Multiply(7,9))), "(5 - (7 * 9))")
        self.assertEqual(str(Multiply(5,Subtract(7,9))), "(5 * (7 - 9))")
    
    def test_Tokens(self):
        temp = "123 + 45"
        self.assertEqual(tokens(temp), ["123","+","45"])
        
    
if __name__ == '__main__':
    unittest.main()