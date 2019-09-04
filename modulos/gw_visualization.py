#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 11:07:29 2018

@author: jprieto
"""

from pycbc.filter import sigma
import pylab

def closer(conditioned,time,snrp,fc,mc,hc,template,psd,grafica):
  
#	Shift the template to the peak time
    dt = time - conditioned.start_time
    aligned = template.cyclic_time_shift(dt)

#	Scale the template so that it would have SNR 1 in this data
    aligned /= sigma(aligned, psd=psd, low_frequency_cutoff=fc)
#	Scale the template amplitude and phase to the peak value
    aligned = (aligned.to_frequencyseries() * snrp).to_timeseries()
    aligned.start_time = conditioned.start_time
    
#	We do it this way so that we can whiten both the template and the data# We do  
    white_data = (conditioned.to_frequencyseries() / psd**0.5).to_timeseries()

#	Apply a smoothing of the turnon of the template to avoid a transient
#	from the sharp turn on in the waveform.
    tapered = aligned.highpass_fir(fc, mc, remove_corrupted=False)
    white_template = (tapered.to_frequencyseries() / psd**0.5).to_timeseries()

    white_data = white_data.highpass_fir(fc, mc).lowpass_fir(mc, hc)
    white_template = white_template.highpass_fir(fc, mc).lowpass_fir(mc, hc)
    white_data = white_data.crop(4,4)
    white_template = white_template.crop(4,4)
#	Select the time around the merger
#	White_data = white_data.time_slice(time+0.1, time+0.25)
#	white_template = white_template.time_slice(time+0.1, time+0.25)

#	white_data = white_data.time_slice(merge+10, merge+20)
#	white_template = white_template.time_slice(merge+10, merge+20)

    if grafica ==1:
        
        pylab.figure(figsize=[15, 5])
        pylab.plot(white_data.sample_times, white_data, label="Data")
        pylab.plot(white_template.sample_times, white_template, label="Template")
        pylab.legend('Matched filter output')
        pylab.show()
    return aligned


    