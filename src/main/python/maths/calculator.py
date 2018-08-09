# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 14:49:32 2018

@author: William
"""

from maths.Parser import Parser

while True:
    userInput = input("Input: ")
    exp =  Parser.parse(userInput)
    print(str(exp) + " = " + str(exp.value()))