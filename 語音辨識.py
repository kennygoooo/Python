#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 21:13:03 2021

@author: kenny
"""

import re
import numpy as np

String = input()
regex = re.compile(r'長度(\d+) ,角度(-*\d+)')
match = regex.search(String)
length = match.group(1)
angle = match.group(2)
angle = int(angle)
length = int(length)
sin = np.sin(np.deg2rad(angle))#角度轉弧度
X = length*sin
cos = np.cos(np.deg2rad(angle))#角度轉弧度
Y = length*cos
print("X:",round(X,2))#四捨五入取小數後第二位
print("Y:",round(Y,2))#四捨五入取小數後第二位