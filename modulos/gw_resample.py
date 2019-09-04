#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 23:54:36 2018

@author: jprieto
"""

from pycbc.filter import resample_to_delta_t
import numpy as np
import pylab
from pycbc import types
from scipy.interpolate import CubicSpline


def interpolacion(h,dt,grafica, fs):

    
#   This is the resampling part of the method, because there's no uniform 
#   sampling we make a cubic spline interpolation.
#   In this part, we asign the last value of time vector as the final time,
#   after that we use it to create the new uniform time vector.
#   The folloing two lines need to be changed in case of use a different resolution.
    
    l = len(dt)
    
    dtf = dt[l-1]
    dti = dt[0]
      
    dts = np.arange(dti, dtf, (1.0/(fs)))
#   Here's where the interpolation method begins
    hs = CubicSpline(dt, h)
#	h is the function that calls the interpolate method, using the dts vector
#	as the time indepent variable wich is EQUALLY spaced.
    hh=hs(dts)
   
    if grafica == 1:
        pylab.figure(figsize=[15, 5])
        pylab.title('Interpolation of the template')
        pylab.plot(dt,h,label='Original')
        #pylab.plot(dts,hh,'-',label='Interpolated')
        pylab.grid()
        pylab.xlabel('Time(s)',fontsize=18)
        pylab.ylabel('Strain',fontsize=18)
        pylab.legend()
        pylab.show()

    return hh,dts,dtf


def resampleado(strain,hh,grafica,fs,fs_ligo):
    
    template = types.TimeSeries(initial_array=hh, delta_t=1.0/fs , epoch=0)
    
#	Downsampling the data to 4096Hz || 8192Hz || 16KHz

    strain = resample_to_delta_t(strain, 1.0/fs)

   
    if grafica == 1:
    
        pylab.figure('Fig_strain')
        pylab.title('Strain resampled')
        pylab.plot(strain.sample_times, strain)
        pylab.xlabel('Time (s)')
        pylab.grid()
        pylab.show()

        pylab.figure('Fig_template')
        pylab.title('Template resampled')
        pylab.plot(template.sample_times, template)
        pylab.grid()
        pylab.xlabel('Time (s)')
        pylab.show()
   
   

    return template, strain


