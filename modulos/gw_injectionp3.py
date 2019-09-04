#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 00:36:19 2018

@author: jprieto
"""
import pylab
from pycbc import types

def make(strain,template,shift,grafica):
        
    template.resize(len(strain))
    injection = template
    
#   Getting parameters for the injection

    start = strain.start_time
    
    delta = strain.delta_t
    
    
#	Seting the parameters in the injection
    
    data_i = template.data
    
    delta_i = delta
    
    inicio = start
    
#   Creating the injection vector
    injection = types.TimeSeries(initial_array=data_i,delta_t=delta_i,epoch=inicio)
    
    injection_shift = injection.cyclic_time_shift(shift)

    maximo = abs(injection_shift).numpy().argmax()
    injmax = injection_shift[maximo]
    tmax = injection.sample_times[maximo]
#	Printing the time where the amplitud is maximum
    


    strain.data = injection_shift.data + strain.data


    if grafica == 1:
    
        print('tiempo template maximo')
        print(tmax)
        pylab.figure(figsize=[15, 5])
        pylab.plot(injection,label='Original resized template')
        pylab.plot(injection_shift.sample_times,injection_shift,label='Injecion resized and shifted')
        pylab.title('Injection resized and shifted')
        pylab.legend()
        pylab.show()
    
    #print 'valor máximo'
    #print injmax  
        
    return strain,tmax,injection_shift
