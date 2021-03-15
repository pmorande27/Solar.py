# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 17:33:33 2020

@author: Pablo Morandé
"""
import math
class Vector(object):
    """
    Class used to represent 2D real vectors
    """
    def __init__(self,value_x,value_y):
        """
        Constructor of the class, used to assign the value of x and y
        """
        self.value_x = value_x
        self.value_y = value_y
    def get_x(self):
        """
        Method to retrieve the x value
        """
        return self.value_x
    def get_y(self):
        """
        Method to retrieve the x value
        """
        return self.value_y
    def mdoulus(self): 
        """
        Method to return the modulus of a vector
        """
        return math.sqrt(self.value_x**2+ self.value_y**2)
    @staticmethod
    def distance(vector1, vector2):
        """
        Static Method to return the distance vector between two vectors
        """
        result = Vector (vector2.get_x() - vector1.get_x(), vector2.get_y() - vector1.get_y())
        return result
    def __truediv__(self,scalar):
        """
        Overridden / operator for scalar division
        """
        return Vector(self.value_x/scalar,self.value_y/scalar)
    def __mul__(self,scalar):
        """
        Overridden * operator for scalar multiplication
        """
        return Vector(self.value_x*scalar,self.value_y*scalar)
    def __iadd__(self,vector):
        """
        Overridden += operator for addition.
        """
        return Vector(self.value_x + vector.value_x, self.value_y+vector.value_y)
    def __add__(self,vector):
        """
        Overridden + operator for addition.
        """
        return Vector(self.value_x + vector.value_x, self.value_y+vector.value_y)
    def __sub__(self,vector):
        """
        Overridden + operator for addition.
        """
        return Vector(self.value_x - vector.value_x, self.value_y-vector.value_y)