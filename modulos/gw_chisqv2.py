#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 16:37:45 2018

@author: jprieto
"""
import numpy as np
from pycbc.psd import interpolate, inverse_spectrum_truncation
from pycbc.vetoes import power_chisq
from pycbc.events import newsnr
from pycbc import types
import pylab


def xis(snr,template,strain,psd_o,fc,grafica,time_max,duration,hc,shift,time_trigger):
    
    
    nbins = 16
    
    chisq = power_chisq(template, strain, nbins, psd_o, low_frequency_cutoff=fc,high_frequency_cutoff=hc)
        
    chisq = chisq.crop(4,4)
    
    dof = nbins * 2 - 2
    chisq/= dof
    
    nsnr=newsnr(snr,chisq)
    
    maximo = max(nsnr)
    
    print 'maximo ', abs(maximo)
    

    MaxInd = np.argmax(nsnr)
    
    
    time = snr.sample_times[MaxInd]
        

    if grafica == 1: 
        

        
        pylab.figure('Superposition')
        pylab.plot(snr.sample_times,abs(nsnr),label='Re-weighted SNR')
        #pylab.plot(snr.sample_times,abs(snr),label='Original SNR')
        #pylab.title('Re-weighted SNR')
        #pylab.ylabel('Signal-to-noise ratio')
        pylab.xlabel('Time(s)')
        pylab.legend()
        #pylab.xlim(time_max-0.05, time_max+0.05)
        pylab.grid()
        pylab.show()  
        
        pylab.figure('Re-weighted SNR')
        pylab.plot(snr.sample_times,abs(nsnr))
        pylab.grid()
        pylab.show()

    
    
    return maximo, time,nsnr
