# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 12:19:08 2018

@author: William
"""

from maths.Expression import Expression

class Divide(Expression):
    def __init__(self,l,r):
        Expression.__init__(self,l,r,"/")    #imported to from the main expression where it has been checked
    def evaluate(self):
        sum = self.left() / self.right()
        return sum
