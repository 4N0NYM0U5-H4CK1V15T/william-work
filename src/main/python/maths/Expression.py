# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:42:30 2018

@author: William
"""

class Expression:       #This class a several sub classes that it runs to 
   
    def valueOf(self,x):
        if isinstance(x, str):          #Checks what data type it will be 
            return float(x)
        elif isinstance(x,Expression):
            return x.evaluate()
        else:
            return x
