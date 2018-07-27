# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:41:51 2018

@author: William
"""

class sum:
    def __init__(self,numb1,numb2):
        self.n1 = numb1
        self.n2 = numb2
    def evaluate(self):
        sum = self.n1 + self.n2
        return sum
    
def test():
    a = sum(2,3)
    return a.evaluate()

print(test())