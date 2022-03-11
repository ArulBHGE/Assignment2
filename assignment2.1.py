# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 17:55:05 2022

@author: 105042833
"""
# input data seperated by space
user_in = list(tuple(map(int,input().split())) for r in range(int(input('enter no of rows : '))))  
print("The list keyed in is:", user_in)
user_in.sort(key=lambda i:i[1],reverse=False)
print(user_in)