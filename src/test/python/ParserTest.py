# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 11:07:19 2018

@author: William
"""

import unittest
from maths.Add import Add            #Imports other classes
from maths.Subtract import Subtract
from maths.Multiply import Multiply
from maths.Divide import Divide
from maths.Parser import Parser
from maths.Constant import Constant

class ParserTest(unittest.TestCase):

    
    def test_Tokens(self):
        temp = "123 + 45"
        self.assertEqual(Parser.tokens(temp), [123, "+", 45 ])
        
    def test_Tokens2(self):
        temp = "12.3 + 45"
        self.assertEqual(Parser.tokens(temp), [12.3 ,"+",45 ])
        
    def test_Tokens3(self):
        temp = "(123 + 45)/2"
        self.assertEqual(Parser.tokens(temp), ["(", 123 ,"+", 45 ,")","/", 2 ])
        
    def test_Tokens4(self):
        with self.assertRaises(ValueError):
            Parser.tokens("12.3.3 + 45")
            
    def test_Parse(self):
        self.assertIsNone(Parser.parse(""))
        self.assertEqual(Parser.parse("12"), Constant(12))
        self.assertEqual(Parser.parse("12.3 + 4.5"), Add(12.3, 4.5))
        self.assertEqual(Parser.parse("12.3 - 4.5"), Subtract(12.3, 4.5))
        self.assertEqual(Parser.parse("12.3 * 4.5"), Multiply(12.3, 4.5))
        self.assertEqual(Parser.parse("12.3 / 4.5"), Divide(12.3, 4.5))
        self.assertEqual(Parser.parse("12.3 + 4.5 + 6.7"), Add(Add(12.3, 4.5), 6.7))
        
    def test_signs(self):
        self.assertEqual(Parser.parse("-2"), Constant(-2))
        self.assertEqual(Parser.parse("+3.5"), Constant(3.5))
        self.assertEqual(Parser.parse(" -2"), Constant(-2))
        self.assertEqual(Parser.parse("-12.3 + 4.5"),Add(-12.3, 4.5))
        self.assertEqual(Parser.parse("-12.3 + -4.5"),Add(-12.3, -4.5))
        self.assertEqual(Parser.parse("12.3 +4.5"), Add(12.3, 4.5))
        self.assertEqual(Parser.parse("12.3-4.5"), Subtract(12.3, 4.5))
        self.assertEqual(Parser.parse("12.3-+4.5"), Subtract(12.3, 4.5))
        self.assertEqual(Parser.parse("12.3+-4.5"), Add(12.3, -4.5))

        
if __name__ == '__main__':
    unittest.main()