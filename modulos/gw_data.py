#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 12:27:01 2018

@author: jprieto
"""

from pycbc import frame
import random as randi
from pycbc import types
#--------------------------------------------------------------------------
#   This is just a time for reading in the LIGO data
    
def ligo():
    
    
#	Number of seconds for the injection to be shifted 

    shift  = randi.randrange(5, 27, 1) 
    
    tiempo_carga = 1126072320
    
#	Reading LIGO strain
#    strain = frame.read_frame('L-L1_LOSC_16_V1-1126072320-4096.gwf','L1:GWOSC-16KHZ_R1_STRAIN',tiempo_carga+10,tiempo_carga+52)
    
    strain = 1
    
    return strain, shift



import random


def gaussian(total_time,fs):
    
#   Number of points for the time vector
    
    N = total_time*fs
    
#	Number of seconds for the injection to be shifted 

    shift  = randi.randrange(5, 27, 1) 
    
    a = []
    for i in range(N):
    
        ran = (random.gauss(0,1E-21))
        
        a.append(ran)

    strain = types.TimeSeries(initial_array=a,delta_t=1.0/fs,epoch=0)
    
    return strain, shift     
    