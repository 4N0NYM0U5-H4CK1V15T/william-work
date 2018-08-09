# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 12:01:17 2018

@author: William
"""

from maths.BinaryExpression import BinaryExpression

class Subtract(BinaryExpression):
    def __init__(self,l,r):
        BinaryExpression.__init__(self,l,r,"-")    #imported to from the main expression where it has been checked
    def value(self):
        sum = self.leftValue() - self.rightValue()        #these functions are imported from expression master function
        return sum
    
