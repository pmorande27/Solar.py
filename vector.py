# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 17:33:33 2020

@author: Pablo Morandé
"""
import math
class Vector(object):
    def __init__(self,value_x,value_y):
        self.value_x = value_x
        self.value_y = value_y
    def get_x(self):
        return self.value_x
    def get_y(self):
        return self.value_y
    def mdoulus(self): 
        return math.sqrt(self.value_x**2+ self.value_y**2)
    @staticmethod
    def distance(vector1, vector2):
        result = Vector (vector2.get_x() - vector1.get_x(), vector2.get_y() - vector1.get_y())
        return result
    def __truediv__(self,scalar):
        return Vector(self.value_x/scalar,self.value_y/scalar)
    def __mul__(self,scalar):
        return Vector(self.value_x*scalar,self.value_y*scalar)
    def __iadd__(self,vector):
        return Vector(self.value_x + vector.value_x, self.value_y+vector.value_y)