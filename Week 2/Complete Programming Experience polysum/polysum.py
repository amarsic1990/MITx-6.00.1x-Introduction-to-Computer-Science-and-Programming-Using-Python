# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 22:24:03 2017

@author: marsic
"""

def polysum(n, s):
    '''
    n: positive integer,  number of sides of a regular polygon
    s: length of each side of a regular polygon
    
    returns:  the sum of the area and square of the perimeter\
    of a regular polygon, rounded to 4 decimal places.
    '''
    import math as m
    return round((0.25*n*s**2)/(m.tan(m.pi/n)) + n**2*s**2, 4)