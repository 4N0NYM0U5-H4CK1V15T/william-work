# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 12:01:17 2018

@author: William
"""

from maths.Expression import Expression

class Subtract(Expression):
    def __init__(self,leftNumb,rightNumb):
        Expression.__init__(self,leftNumb,rightNumb)    #imported to from the main expression where it has been checked
    def evaluate(self):
        sum = self.left() - self.right()        #these functions are imported from expression master function
        return sum
    
