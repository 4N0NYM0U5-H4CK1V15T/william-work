# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:42:30 2018

@author: William
"""

class Expression:       #This class a several sub classes that it runs to 
    def __init__(self,leftNumb,rightNumb):
        self.leftNumber = leftNumb
        self.rightNumber = rightNumb        
    def left(self):
        return self.valueOf(self.leftNumber)    #valueOf is the expression used to check that it is a int
    def right(self):
        return self.valueOf(self.rightNumber)
    
    def valueOf(self,x):
        if isinstance(x, str):          #Checks what data type it will be 
            return float(x)
        elif isinstance(x,Expression):
            return x.evaluate()
        else:
            return x
            