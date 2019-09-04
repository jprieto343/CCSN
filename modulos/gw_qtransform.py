#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 12:04:15 2018

@author: jprieto
"""
import pylab
import numpy as np

def make(conditioned,aligned,grafica,time,psd):

    
    t, f, p = conditioned.whiten(4, 4).qtransform(.001,logfsteps=100,qrange=(8, 8),frange=(150, 2048))
                       

    pylab.figure(figsize=[15, 5])
    pylab.title('Peak time qtransform')
    pylab.pcolormesh(t, f, p**0.5, vmin=1, vmax=7)
    pylab.yscale('log')
    pylab.xlabel('Time (s)')
    pylab.ylabel('Frequency (Hz)')
    pylab.xlim(time-0.05, time+0.35)
    pylab.show()                           
                                                  

    pylab.figure(figsize=[15, 5])
    pylab.title('Power Spectral Density')
    pylab.loglog(psd.sample_frequencies, np.sqrt(psd))
    pylab.ylabel('$Strain^2 / Hz$')
    pylab.xlabel('Frequency (Hz)')
    pylab.grid()
    pylab.xlim(150, 4096)
    pylab.show()
    
    return