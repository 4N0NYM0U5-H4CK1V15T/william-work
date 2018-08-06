# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:42:30 2018

@author: William
"""

from maths.Expression import Expression

class BinaryExpression(Expression):       #This class a several sub classes that it runs to 
    def __init__(self,leftVal,rightVal,symbol):
        self.leftVal = leftVal
        self.rightVal = rightVal
        self.symbol = symbol
        
    def left(self):
        return self.valueOf(self.leftVal)    #valueOf is the expression used to check that it is a int
    def right(self):
        return self.valueOf(self.rightVal)
        
    def __str__(self):  #called by python when it tries to convert the object to a string
        return "(" + str(self.leftVal) + " " + self.symbol + " " + str(self.rightVal) + ")"
            
    def __eq__(self, other):    #called by python when two objects == each other
        return isinstance(other, BinaryExpression) and self.leftVal == other.leftVal and self.rightVal == other.rightVal and self.symbol == other.symbol