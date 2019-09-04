# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 23:17:49 2018

@author: jprieto
"""
import pylab
import numpy as np
import scipy.fftpack
import scipy.signal as signal

 
def make(template,conditioned,psd,injection_shift,grafica):
    
    h = injection_shift.data # y 
    h_sample = injection_shift.delta_t #T
    h_samplef = injection_shift.delta_f
    N = len(injection_shift)    
    fs = conditioned.sample_rate
  
#   Sample spacing
  
#   calculating the FFT of the template

  
    T = h_sample
    y = h
    yf = scipy.fftpack.fft(y)
    xf = np.linspace(0.0, 1.0/(2.0*T), N/2+1)
    yfa =2.0/N * np.abs(yf[:N/2+1])**2
    if grafica == 1:
        
        pylab.figure(figsize=[15, 5])
        pylab.title('FFT of template')
        pylab.plot(xf,np.sqrt(yfa))
        pylab.show()
   
    xs = conditioned.data
    
    
#   Getting the expexted value of the snr
    deltaf= h_samplef

    
    expected = 2*np.sqrt(deltaf*(yfa/psd))  

    if grafica == 1:
        
        pylab.figure('Expected_SNR',figsize=[15, 5])
        pylab.title('$rho_0$')
        pylab.plot(psd.sample_frequencies,expected)
        pylab.xlabel('Hz')
        pylab.show()
    print 'SNR esperado'

    maximo = max(expected)
    print maximo
    if grafica == 1:
        
        f, Pxx_den = signal.welch(xs, fs,nperseg=8192)
        pylab.figure(figsize=[15, 5])
        pylab.title('Amplitude Spectral Density of strain ')
        pylab.loglog(f, np.sqrt(Pxx_den))
        pylab.ylabel('$Strain^2 / Hz$')
        pylab.xlabel('Frequency (Hz)')
        pylab.grid()
        pylab.xlim(150, 4096)
        pylab.show()
    
    return maximo