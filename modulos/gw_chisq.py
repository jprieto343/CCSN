#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 16:37:45 2018

@author: jprieto
"""
import numpy as np
from pycbc.vetoes import power_chisq
from pycbc.events import newsnr
import pylab


def xis(snr,template,strain,psd,fc,grafica,time_max,duration,hc,shift):
    
    
    nbins = 32
    
    
    start_time = strain.start_time
    
    end_time = strain.start_time+32
    
    #crop_left = abs(start_time - time_max-5)
    
    #crop_right = abs(end_time - time_max-5)
    
   
    #strain = strain.crop(crop_left,crop_right)
    #psd   = psd.crop(crop_left,crop_right)
    
    chisq = power_chisq(template, strain, nbins, psd, low_frequency_cutoff=fc,high_frequency_cutoff=hc)
    chisq = chisq.crop(4, 4)
    dof = 2*nbins-2
    
    chisq /= dof
    
    
    
    
    low_chisq = min(chisq)
    
    #print 'Lower value of Chi'
    #print low_chisq

    if grafica == 1: 
        
        nsnr=newsnr(snr,chisq)
        
        pylab.plot(chisq.sample_times,chisq)
        pylab.ylabel('$chi^2_r$')
        pylab.xlabel('Time(s)')
        pylab.xlim(time_max-0.1, time_max+0.1)
        
        pylab.grid()
        pylab.show() 
        
        pylab.figure('Superposition',figsize=[15,5])
        pylab.plot(snr.sample_times,abs(nsnr),label='Re-weighted SNR')
        pylab.plot(snr.sample_times,abs(snr),label='Original SNR')
        pylab.plot(chisq.sample_times,chisq,label='$Chi^2$')
        #pylab.title('Re-weighted SNR')
        #pylab.ylabel('Signal-to-noise ratio')
        pylab.xlabel('Time(s)')
        pylab.legend()
        pylab.xlim(time_max-0.05, time_max+0.05)
        
        pylab.grid()
        pylab.show()  
        

        pylab.plot(snr.sample_times,abs(snr))
        pylab.title('Matched filter output')
        pylab.ylabel('Signal-to-noise ratio')
        pylab.xlabel('Time(s)')
        pylab.xlim(time_max-0.1, time_max+0.1)
        
        pylab.grid()
        pylab.show()  
    
    
    return chisq, low_chisq
