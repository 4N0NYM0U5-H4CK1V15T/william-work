# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:42:30 2018

@author: William
"""

from maths.Expression import Expression
# Represents a constant numerical value
class Constant(Expression): 
    # Can be initialized with a number or string
    def __init__(self,value):
        if isinstance(value, float):
            self.numValue = value
        else:
            self.numValue = float(value)
        
    def evaluate(self):
        return self.numValue
        
    def __str__(self):  #called by python when it tries to convert the object to a string
        return str(self.numValue)
            
    def __eq__(self, other):    #called by python when two objects == each other
        return isinstance(other, Constant) and self.numValue == other.numValue
