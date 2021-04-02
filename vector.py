# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 17:33:33 2020

@author: Pablo Morandé
"""
import math


class Vector(object):
    """Class used to represent 2D real vectors
    """

    def __init__(self, value_x, value_y):
        """Constructor of the class, used to assign the value of x and y

        Args:
            value_x (float): value of the component in the x direction
            value_y (float): value of the component in the t direction
        """
        self.value_x = value_x
        self.value_y = value_y

    def __copy__(self):
        """Overridden method used to make a copy of a given vector

        Returns:
            Vector: Vector with the same x,y components
        """
        return type(self)(self.value_x, self.value_y)

    def get_x(self):
        """Method to retrieve the x value

        Returns:
            float: value of the component in the x direction of a vector
        """
        return self.value_x

    def get_y(self):
        """Method to retrieve the y value

        Returns:
            float: value of the component in the y direction of a vector
        """
        return self.value_y

    def mdoulus(self):
        """Method to return the modulus of a vector

        Returns:
            float: modulus of the vector
        """
        return math.sqrt(self.value_x ** 2 + self.value_y ** 2)

    @staticmethod
    def distance(vector1, vector2):
        """Static Method to return the distance vector between two vectors

        Args:
            vector1 (Vector): Vector one
            vector2 (Vector): Vector two

        Returns:
            Vector: distance distance vector between vectors 1 and 2.
        """
        result = Vector(vector2.get_x() - vector1.get_x(), vector2.get_y() - vector1.get_y())
        return result

    def __truediv__(self, scalar):
        """Overridden / operator for scalar division


        Args:
            scalar (float): Number to divide all the ocmponents by

        Returns:
            Vector: New Vector after dividing by scalar all the components
        """
        return Vector(self.value_x / scalar, self.value_y / scalar)

    def __mul__(self, scalar):
        """Overridden * operator for scalar multiplication

        Args:
            scalar (float): Number to multiply all the components by

        Returns:
            Vector : New Vector afte multiplying all the components by scalar.
        """
        return Vector(self.value_x * scalar, self.value_y * scalar)

    def __iadd__(self, vector):
        """ Overridden += operator for addition.

        Args:
            vector (Vector): Vector to be added

        Returns:
            Vector: New Vector result of adding the two vectors
        """
        return Vector(self.value_x + vector.value_x, self.value_y + vector.value_y)

    def __add__(self, vector):
        """ Overridden + operator for addition.

        Args:
            vector (Vector): Vector to be added

        Returns:
            Vector: New Vector result of adding the two vectors
        """
        return Vector(self.value_x + vector.value_x, self.value_y + vector.value_y)

    def __sub__(self, vector):
        """ Overridden - operator for addition.

        Args:
            vector (Vector): Vector to be added

        Returns:
            Vector: New Vector result of substracting the two vectors
        """
        return Vector(self.value_x - vector.value_x, self.value_y - vector.value_y)

    @staticmethod
    def scalar_product(vectorA, vectorB):
        """Static method used to ompute the scalar product between two vectors

        Args:
            vectorA (Vector): Vector One
            vectorB (Vector): Vector Two

        Returns:
            float: Scalar Product between the vectors A and B.
        """
        return vectorA.get_x() * vectorB.get_x() + vectorA.get_y() * vectorA.get_y()
