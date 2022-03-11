# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 18:14:22 2022

@author: 105042833
"""

import string
dictionary={}
for letter in string.ascii_lowercase:
    dictionary[letter[0]]=ord(letter[0])
print(dictionary)
