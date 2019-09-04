#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 23:44:52 2018

@author: jprieto
"""

from scipy.interpolate import CubicSpline
import numpy as np
import pylab
from pycbc import types
from pycbc.filter import resample_to_delta_t


def interpolacion(h,dt,grafica, fs):
#   The original data comes in units of milliseconds, so we make a conversion
#   to match it with the data in LIGO
    


    
#   This is the resampling part of the method, because there's no uniform 
#   sampling we make a cubic spline interpolation.
#   In this part, we asign the last value of time vector as the final time,
#   after that we use it to create the new uniform time vector.
#   The folloing two lines need to be changed in case of use a different resolution.
    
    l = len(dt)
    
    dtf = dt[l-1]
    dti = dt[0]
    
    print dtf,dti
    
    #df = abs(dt[0]-dt[1])
    #print df
    
    #fs = 1.0/df
    
    print fs
    
    dts = np.arange(dti, dtf, (1.0/(fs)))
#   Here's where the interpolation method begins
    hs = CubicSpline(dt, h)
#	h is the function that calls the interpolate method, using the dts vector
#	as the time indepent variable wich is EQUALLY spaced.
    hh=hs(dts)
   
    if grafica == 1:
        pylab.figure(figsize=[15, 5])
        pylab.title('Interpolation of the template')
        pylab.plot(dt,h,'-o',label='Original')
        pylab.plot(dts,hh,'-',label='Interpolated')
        pylab.grid()
        pylab.xlabel('Time(s)',fontsize=18)
        pylab.ylabel('Strain',fontsize=18)
        pylab.legend()
        pylab.show()





def resampleado(strain,hh,grafica):
    

    template = types.TimeSeries(initial_array=hh, delta_t=1.0/8192 , epoch=0)


#	Downsampling the data to 4096Hz || 8192Hz || 16KHz

    strain = resample_to_delta_t(strain, 1.0/8192)

    template = resample_to_delta_t(template, 1.0/8192)
    
    if grafica == 1:
    
        pylab.figure(figsize=[15, 5])
        pylab.title('strain resampled')
        pylab.plot(strain.sample_times, strain)
        pylab.xlabel('Time (s)')
        pylab.show()




dt = np.loadtxt('And1815fr1kpc_equ.txt',usecols=(0))

hp = np.loadtxt('And1815fr1kpc_equ.txt',usecols=(1))
hc = np.loadtxt('And1815fr1kpc_equ.txt',usecols=(2))
h =  hc + hp

fs = 8192

pylab.figure('Original')
pylab.plot(dt,h)
pylab.grid()
pylab.show()


template = types.TimeSeries(initial_array=h, delta_t=1.0/2048 , epoch=0)

pylab.figure('Original')
pylab.plot(template.sample_times,template)
pylab.grid()
pylab.show()

template = resample_to_delta_t(template, 1.0/1024)

pylab.figure('Original')
pylab.plot(template.sample_times,template)
pylab.grid()
pylab.show()

interpolacion(h,dt,1,fs)


