# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:42:30 2018

@author: William
"""

class Expression:       #This class a several sub classes that it runs to 
    def __init__(self,leftVal,rightVal,symbol):
        self.leftVal = leftVal
        self.rightVal = rightVal
        self.symbol = symbol
        
    def left(self):
        return self.valueOf(self.leftVal)    #valueOf is the expression used to check that it is a int
    def right(self):
        return self.valueOf(self.rightVal)
    
    def valueOf(self,x):
        if isinstance(x, str):          #Checks what data type it will be 
            return float(x)
        elif isinstance(x,Expression):
            return x.evaluate()
        else:
            return x
        
    def __str__(self):
        return "(" + str(self.leftVal) + " " + self.symbol + " " + str(self.rightVal) + ")"
            