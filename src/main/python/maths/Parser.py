# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 14:14:39 2018

@author: William
"""

class Parser:
    def __init__(self):
        pass
    
    def tokens(string):
        strList = list(string)
        finalList = []
        temp = ""
        
        def record(s):
            if (s != '' and s != ' '):
                finalList.append(s)
                
        def isNumeric(s):
           return (ord(s) in range(48,58) or s == ".")
       
        def numbToFloat(s):
            try:
                float(s)
                return float(s)           
            except ValueError:
                return(s)
        
        for x in range(0, len(strList)):
            if isNumeric(strList[x]):
                temp = temp + strList[x]
            else:
                record(numbToFloat(temp))
                temp = ""
                record(strList[x])
        
        record(numbToFloat(temp))
        return finalList
    
    def parser(s):
        pass