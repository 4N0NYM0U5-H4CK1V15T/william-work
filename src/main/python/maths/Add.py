# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:41:51 2018

@author: William
"""

class Add:
    def __init__(self,leftNumb,rightNumb):
        self.lNumb = leftNumb
        self.rNumb = rightNumb
    def evaluate(self):
        sum = self.lNumb + self.rNumb
        return sum
    
