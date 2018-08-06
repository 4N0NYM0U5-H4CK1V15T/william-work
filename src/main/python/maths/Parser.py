# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 14:14:39 2018

@author: William
"""

from maths.Add import Add
from maths.Subtract import Subtract
from maths.Multiply import Multiply
from maths.Divide import Divide
from maths.Constant import Constant

class Parser:
    def __init__(self):
        pass
    
    def tokens(string):
        strList = list(string)
        finalList = []
        temp = ""
        
        def record(s):
            if (s == '' or s == ' '):
                return
            if isNumeric(s[0]):
                finalList.append(float(s))
            else:
                finalList.append(s)
                
        def isNumeric(s):
           return (ord(s) in range(48,58) or s == ".")
       
        
        for x in range(0, len(strList)):
            if isNumeric(strList[x]):
                temp = temp + strList[x]
            else:
                record(temp)
                temp = ""
                record(strList[x])
        
        record(temp)
        return finalList
    
    def parse(s):
        toks = Parser.tokens(s)
        tokenCount = len(toks)
        if tokenCount == 0:
            return None
        if tokenCount == 1:
            return Constant(toks[0])
        if tokenCount != 3:
            return None
        
        left = toks[0]
        symbol = toks[1]
        right = toks[2]
        
        if symbol == "+":
            return Add(left, right)
        elif symbol == "-":
            return Subtract(left, right)
        elif symbol == "*":
            return Multiply(left, right)
        elif symbol == "/":
            return Divide(left, right)
        
        