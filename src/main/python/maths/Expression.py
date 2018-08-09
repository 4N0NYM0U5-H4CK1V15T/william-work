# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:42:30 2018

@author: William
"""
from abc import ABC, abstractmethod

# This interface indicates that an object is an Expression and that we can find its value by calling the value() method.
class Expression(ABC):     
    
    # Concrete subclasses must provide an implementation of this method.
    @abstractmethod
    def value(self):
        pass