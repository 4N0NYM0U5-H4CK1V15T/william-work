# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:42:30 2018

@author: William
"""

from maths.Expression import Expression

class Constant(Expression):       #This class a several sub classes that it runs to 
    def __init__(self,val):
        self.val = val
        
    def val(self):
        return self.valueOf(self.val)    
    
    def evaluate(self):
        return self.val()
        
    def __str__(self):  #called by python when it tries to convert the object to a string
        return str(self.val)
            
    def __eq__(self, other):    #called by python when two objects == each other
        return isinstance(other, Constant) and self.val == other.val