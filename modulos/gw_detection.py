#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 11:44:18 2018

@author: jprieto
"""

def decision(SNRrec,SNRthr):
    
#   tmax is the time where is the maximum value of the injected gw
#   time is the time where the snr is maximum
#   dtf is the duration in seconds of the gw
    
    
    if SNRrec > SNRthr:
        flag = 1
    else:
        
        flag = 0
        
    return flag 
