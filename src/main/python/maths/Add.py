# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:41:51 2018

@author: William
"""

from maths.BinaryExpression import BinaryExpression

class Add(BinaryExpression):
    def __init__(self,l,r):
        BinaryExpression.__init__(self,l,r,"+")    #imported to from the main expression where it has been checked
    def value(self):
        return self.leftValue() + self.rightValue()
    
