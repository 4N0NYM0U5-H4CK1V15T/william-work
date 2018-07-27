# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:41:51 2018

@author: William
"""

from maths.Expression import Expression

class Add(Expression):
    def __init__(self,leftNumb,rightNumb):
        Expression.__init__(self,leftNumb,rightNumb)
    def evaluate(self):
        sum = self.left() + self.right()
        return sum
    
