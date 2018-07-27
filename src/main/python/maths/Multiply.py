# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 12:12:06 2018

@author: William
"""


class Multiply:
    def __init__(self,leftNumb,rightNumb):
        self.lNumb = leftNumb
        self.rNumb = rightNumb
    def evaluate(self):
        sum = self.lNumb * self.rNumb
        return sum