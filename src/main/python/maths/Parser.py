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
                
        def isSignPrefix(s):
            tokensSoFar = len(finalList)
            isSign = s in ['+','-']
            isStartOfNewToken = temp == ""
            followsANumber = tokensSoFar > 0 and isinstance(finalList[tokensSoFar - 1], float)
            
            return isSign and isStartOfNewToken and not followsANumber
        
        def isNumeric(s):
            return isSignPrefix(s) or (ord(s) in range(48,58) or s == ".")
               
        for x in range(0, len(strList)):
            if isNumeric(strList[x]):
                temp = temp + strList[x]
            else:
                record(temp)
                temp = ""
                record(strList[x])
        
        record(temp)
        return finalList

    def newExpression(l,r,operator):
        if operator == "+":
            return Add(l, r)
        elif operator == "-":
            return Subtract(l, r)
        elif operator == "*":
            return Multiply(l, r)
        elif operator == "/":
            return Divide(l, r)
        
    def parse(s):
        acc = None
        operator = None        
        
        def isOperator(s):
            return s in ['+','-','*','/']
        
        toks = Parser.tokens(s)
        for tok in toks:
            if isOperator(tok):
                operator = tok
            else: # Otherwise, assume that tok is a number
                if acc is None:
                    acc = Constant(tok)
                elif operator == None:
                    raise ValueError("No operator found before " + tok)
                else:
                    acc = Parser.newExpression(acc,tok,operator)
 
                operator = None
            
        return acc