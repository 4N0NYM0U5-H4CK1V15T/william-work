# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 12:19:08 2018

@author: William
"""

class Divide:
    def __init__(self,leftNumb,rightNumb):
        self.lNumb = leftNumb
        self.rNumb = rightNumb
    def evaluate(self):
        sum = self.lNumb / self.rNumb
        return sum
