# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:42:30 2018

@author: William
"""

class Expression:
    def __init__(self,leftNumb,rightNumb):
        self.leftNumber = leftNumb
        self.rightNumber = rightNumb        
    def left(self):
        return self.valueOf(self.leftNumber)    
    def right(self):
        return self.valueOf(self.rightNumber)
    
    def valueOf(self,x):
        if isinstance(x, str):
            return float(x)
        else:
            return x
            