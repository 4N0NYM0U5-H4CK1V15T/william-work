# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 12:12:06 2018

@author: William
"""

from maths.BinaryExpression import BinaryExpression

class Multiply(BinaryExpression):
    def __init__(self,l,r):
        BinaryExpression.__init__(self,l,r,"*")    #imported to from the main expression where it has been checked
    def evaluate(self):
        sum = self.left() * self.right()
        return sum