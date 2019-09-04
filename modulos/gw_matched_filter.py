#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 01:07:35 2018

@author: jprieto
"""
from pycbc.psd import interpolate, inverse_spectrum_truncation
import pylab
import numpy as np
from pycbc.filter import matched_filter, sigma, sigmasq_series
def make(conditioned,template,fc,mc,hc,grafica):
    
    
#	We use 4 second samles of our time series in Welch method.
    psd = conditioned.psd(4)

#	Now that we have the psd we need to interpolate it to match our data
#	and then limit the filter length of 1 / PSD. After this, we can
#	directly use this PSD to filter the data in a controlled manner

    psd = interpolate(psd, conditioned.delta_f)

    psd = inverse_spectrum_truncation(psd, 4* conditioned.sample_rate,low_frequency_cutoff=fc)
	
    psd_o = psd
    
    snr = matched_filter(template, conditioned,psd=psd, low_frequency_cutoff=fc)
    sigmasq = sigma(template,psd,low_frequency_cutoff=fc)
    

    #print 'Rho_0'
    #print sigmasq
	
#	Remove time corrupted by the template filter and the psd filter
#	We remove 4 seonds at the beginning and end for the PSD filtering
#	And we remove 4 additional seconds at the beginning to account for
#	the template length (this is somewhat generous for 
#	so short a template). A longer signal such as from a BNS, would 
#	require much more padding at the beginning of the vector.
    snr = snr.crop(4, 4)
	
    if grafica ==1:
        
        pylab.figure('Matched_filter_output')
        pylab.title('Matched filter output')
        pylab.grid()
        pylab.plot(snr.sample_times, abs(snr))
        
        pylab.ylabel('Signal-to-noise ratio')
        pylab.xlabel('Time (s)')
        pylab.show()
        
        
    peak = abs(snr).numpy().argmax()
    snrp = snr[peak]
    time = snr.sample_times[peak]

    #print 'Tiempo de SNR máximo'
    #print time
    #print 'SNR recuperado'
    #print abs(snrp)
    
    return snr,psd,peak,time,snrp, psd_o,sigmasq

    
