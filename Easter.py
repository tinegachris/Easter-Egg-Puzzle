# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 04:29:04 2021

@author: DAVID WARUTUMO
"""

def get_ints():
    valid = []
    
    '''try values from 1 to 1e6'''
    for z_int in range(1, int(1e6)):
         z = z_int
         
         for y_int in range(z_int+1, int(1e6)):
             y = y_int
             test_radical = 8*z**3, y**2

             if is_int(test_radical[0], test_radical[1]):
                 x = test_radical[0]/test_radical[1] - y
                 
                 '''already y>z, so test if x > y'''
                 if x > y:
                     valid.append([x,y,z])#add triplets to possible results
                     print([x,y,z])
                     
         '''stop if more than 10 sets of answers are found'''
         if len(valid) > 10:
             break
    return valid

'''test if radical has remainder. if remainder = 0, the denominator b divides the numerator a'''           
def is_int(a,b):
    if a%b == 0:
        return True
    else:
        return False
    
    