#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 12:27:01 2018

@author: jprieto
"""
from typing import Any, Union

import pycbc
import random as randi

inicio_l = 1126051217
final_l =1137254417


date: Union[int, Any] = randi.randrange(inicio_l, final_l, 1)

print(date)
