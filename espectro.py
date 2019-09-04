#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 00:45:45 2018

@author: jprieto
"""
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from pycbc.frame import read_frame

file_name = "H-H1_GWOSC_16KHZ_R1-1187008867-32.gwf"

merger = 1187008882.4


# LOSC bulk data typically uses the same convention for internal channels names
# Strain is typically IFO:LOSC-STRAIN, where IFO can be H1/L1/V1.
channel_name = "H1:GWOSC-16KHZ_R1_STRAIN"

hc = 500
lc = 30

ts = read_frame(file_name, channel_name,1187008867,1187008867+32)

start = ts.start_time

ts = ts.highpass_fir(lc,512)
ts = ts.lowpass_fir(hc,512)


strain = ts.data

psd = ts.psd(2)

whitened = ts.whiten(4,4,low_frequency_cutoff=20)

fs = 10e3
N = 1e5
amp = 2 * np.sqrt(2)
noise_power = 0.01 * fs / 2
time = np.arange(N) / float(fs)
mod = 500*np.cos(2*np.pi*0.25*time)
carrier = amp * np.sin(2*np.pi*3e3*time + mod)
noise = np.random.normal(scale=np.sqrt(noise_power), size=time.shape)
noise *= np.exp(-time/5)
x = carrier + noise





f, t, Sxx = signal.spectrogram(whitened, 16383)
plt.pcolormesh(t, f, Sxx,vmin=0,vmax=6)
plt.yscale('log')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.ylim((lc,hc))
plt.show()



f, t, Zxx = signal.stft(whitened, 16383, nperseg=1000)
plt.pcolormesh(t, f, np.abs(Zxx))
plt.title('STFT Magnitude')
plt.yscale('log')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.ylim((lc,hc))
#plt.xlim((start+5.5,start+6.5))
plt.xlim((11,11.5))
plt.show()


