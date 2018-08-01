# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 14:14:39 2018

@author: William
"""

def tokens(string):
    strList = list(string)
    finalLst = []
    temp = ""
    
    for x in range(0, len(strList)):
        if ord(strList[x]) in range(48,57):
            temp = temp + strList[x]
        else:
            temp = temp + strList[x]
            finalLst.append(temp)
            temp = ""
            
    return finalLst

print(tokens("123 + 45"))