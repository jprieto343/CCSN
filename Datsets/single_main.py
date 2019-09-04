# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 20:11:39 2018

@author: jprieto
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 20:28:53 2018

@author: jprieto
"""

#	Loading our modules
import gw_resample, gw_injection, gw_matched_filter, gw_visualization, gw_detection
import gw_expected_single, gw_qtransform, gw_readtemplate, gw_data
import numpy as np
import pylab

#   For debugging and visualization purposes set grafica to 1 

grafica = 1

#   Creating vectors for the printed results

SNRrec = []
SNRexp = []
indice = []
flag = []

#----------------------------------------------------------------------------
    
#   Type of data, gaussian for gaussian random noise or O1 for the LIGO data

data = 'gaussian'
#data = 'O1'

#----------------------------------------------------------------------------
#for i in range(40,55):
   
#	This is the index of the list of templates 
#	it goes from 0 to 134 (for now...)

n=58 

#	Reading template

h,dt,nombre = gw_readtemplate.lectura(n)

#   Making uniform the distribution of the dt in the template
#   These function returns the resampled strain,
hh,dts,dtf = gw_resample.interpolacion(h,dt,grafica)

        
straing, shiftg = gw_data.gaussian(32,16384)
        
strainl,shiftl = gw_data.ligo()

shiftl =shiftg

#	Resampling and resizing data

template, noiseg = gw_resample.resampleado(straing,hh,grafica)

template, noisel = gw_resample.resampleado(strainl,hh,grafica)

#   Making the injection of the template into the data

straing,tmaxg,injection_shiftg = gw_injection.make(noiseg,template,shiftg,grafica)

strainl,tmaxl,injection_shiftl = gw_injection.make(noisel,template,shiftl,grafica)


#   The limit values for the frequency in the filters


fc = 40  
hc = 780 
mc = 733 
#	Making the matched filter
#	This function give us the timeseries object of the snr over the time, the maximum value of the snr and
#	the time that it occurs
snrg,psdg,peakg,timeg,snrpg = gw_matched_filter.make(straing,template,fc,mc,hc,grafica)

snrl,psdl,peakl,timel,snrpl = gw_matched_filter.make(strainl,template,fc,mc,hc,grafica)
#   Getting the theoretical value of snr 

snr_predictedg,fftg,pxg,fg,ft = gw_expected_single.make(template,straing,psdg,injection_shiftg,grafica)

snr_predictedl,fftl,pxl,fl,ft = gw_expected_single.make(template,strainl,psdl,injection_shiftl,grafica)


pylab.figure(figsize=[15, 5])
pylab.loglog(ft, fftg,label='FFT of template')
pylab.loglog(fg,pxg,label='PSD of GN')
pylab.loglog(fl,pxl,label='PSD of LIGO data')
pylab.ylabel('$Strain / Hz^{1/2}$',fontsize=18)
pylab.xlabel('Frequency (Hz)',fontsize=18)
pylab.legend()
pylab.grid()
pylab.xlim(10, 4096)
pylab.show()


#-------------------------------------------------------------------------------------------------------------------------
#   Detection part
#desicion = gw_detection.decision(tmax,time,dtf)
#--------------------------------------------------------------------------------------------------------------------------
#	The time, amplitude, and phase of the SNR peak tell us how to align
#	our proposed signal with the data.
#SNRrec.append(snrp)
#SNRexp.append(snr_predicted)
#indice.append(n)
#flag.append(desicion)
print n
    
    
#	Visualizing the data
#if grafica == 1 :
    

#    aligned = gw_visualization.closer(strain,time,snrp,fc,mc,hc,template,psd,grafica)

#   Visualizing the periodigram and the psd
#if grafica == 1 :
    
#    transformada = gw_qtransform.make(strain,aligned,grafica,time,psd)

#	Writing the data to a file

np.savetxt('datos-o1-55-134.out',(np.abs(SNRrec),np.abs(SNRexp),np.abs(indice),np.abs(flag)),fmt='%3.3f')
