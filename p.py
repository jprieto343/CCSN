#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 20:28:53 2018

@author: jprieto

To report any bug please write to me at josue.jonathan@outlook.com


"""
#	importing miscelaneous libraries
#-----------------------------------------------------------------------
import multiprocessing
import urllib

#----------------------------------------------------------------------------
#	Making the printed results directory
#tiempo = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
#carpeta = 'Resultados '+tiempo
#os.mkdir(carpeta)

#############################################################################
#---------------------------------------------------------------------------#
#               	    Main cycle function				                         #
#---------------------------------------------------------------------------#
#############################################################################


def principal(runs,archivo_nombre,local):

	
#   Loading our modules
    from modulos import gw_resample, gw_injection, gw_matched_filter
    from modulos import  gw_detection, gw_expected, gw_qtransform, gw_data, gw_chisqv2, gw_readtemplatev
    from Noise_Sources import gw_load_noise, load
    import numpy as np
    import random as randi
    from pycbc import frame, types
    import urllib
    grafica = 0


    SNRthr = 5
    
    NSegmnt = 3
    
    #initial distance
    
    i_d = 1
    
    #final distance 
    
    f_d = 10
    
    #number of slices
    
    N_d = 2
    
    #dic = np.linspace(i_d,f_d,N_d)
    #di = []

    di = [1,5,10,15,20,25,30,35,40,45,50]

    #di.extend(dic)
    #if local == False:
        
    #url = 'https://www.gw-openscience.org/archive/data/O1_16KHZ/1125122048/H-H1_LOSC_16_V1-'
    #urllib.urlretrieve(url+str(archivo_nombre)+'-4096.gwf', str(archivo_nombre)+'.gwf')


#-------------------------------------------------------------------------
#temporal stuff


    aprox = 'NEW'
    
    numero = 1

    total_time = 32
    fs = 8192 # Sampling frequency
    
    fs_ligo = 16384
#---------------------------------------------------------------------------#
#               loading files                                               #
#---------------------------------------------------------------------------#

    archivo = str(archivo_nombre)+'.gwf'

    strain_initial = frame.read_frame(archivo, 'L1:GWOSC-16KHZ_R1_STRAIN')

    strain_n = strain_initial.data

    del strain_initial

    strain_light = []

    for i in range(NSegmnt):
        a = i * total_time * fs_ligo
        b = (i + 1) * total_time * fs_ligo
        strain_light.append(strain_n[a:b])
###############################################################################
#
#       vectores de resultados
#        
###############################################################################        
    SNRrec = []
    SNRexp = []
    trigger_time = []
    injection_time = []
    total_flag = []



    for dat in  range(len(strain_light)):
        
        print dat, ' indice de segmento'


        strain = strain_light[dat]
        
            
        strain = types.TimeSeries(initial_array=strain, delta_t=1.0/fs_ligo , epoch=0)


        rec = []
        exp = []
        flag = []
        tt = []
        dist = []
        ti = []


        assert isinstance(runs, object)

        for d in range(len(di)):


            distancia = di[d]

            n=numero
            
            print distancia, ' distancia'

                #	Reading template
            h,dt,nombre = gw_readtemplatev.lectura(n,aprox)
                #	Distance
                
                
            hh, dts,dtf = gw_resample.interpolacion(h,dt,grafica,fs)
                
            hh = hh/distancia
                
           
            shift = randi.randrange(5, 27, 1)

            template, noise = gw_resample.resampleado(strain,hh,grafica,fs,fs_ligo)


#   Making uniform the distribution of the dt in the template
#   These function returns the resampled strain,

#Resampling and resizing data

#   Making the injection of the template into the data
            strain_inj,tmax,injection_shift = gw_injection.make(noise,template,shift,grafica)

#   The limit values for the frequency in the filters
            fc = 15
            hc = 1200
            mc = 733
                        #	Making the matched filter
                        #	This function give us the timeseries object of the snr over the time, the maximum value of the snr and
#	the time that it occurs
            snr,psd,index_snr_trigger,time,rho,psd_o,rho_0 = gw_matched_filter.make(strain_inj,template,fc,mc,hc,grafica)
            

#   Getting the Chi^2 value
            snr2,HSNR2_time,nsnr = gw_chisqv2.xis(snr,template,strain_inj,psd_o,fc,grafica,time,dtf,hc,shift,index_snr_trigger)
            
#   Getting the theoretical value of snr
#-------------------------------------------------------------------------------------------------------------------------
#   Detection part
            desicion = gw_detection.decision(snr2,SNRthr)

#--------------------------------------------------------------------------------------------------------------------------
#	The time, amplitude, and phase of the SNR peak tell us how to align
#	our proposed signal with the data.

            rec.append(abs(snr2))
            exp.append(abs(rho_0))
            flag.append(desicion)
            tt.append(shift)
            ti.append(HSNR2_time)
            
        SNRrec.extend(rec)
        SNRexp.extend(exp)
        total_flag.extend(flag)
        trigger_time.extend(ti)
        injection_time.extend(tt)
        
        
        rec = []
        exp = []
        flag = []
        tt = []
        dist = []
        ti = []

            
            
    np.savetxt('SNRrec'+str(archivo_nombre)+'.out',SNRrec,fmt='%3.2f')         
    np.savetxt('SNRexp'+str(archivo_nombre)+'.out',SNRexp,fmt='%3.2f')
    np.savetxt('FLAG'+str(archivo_nombre)+'.out',total_flag,fmt='%3.2f')
    np.savetxt('TT'+str(archivo_nombre)+'.out',trigger_time,fmt='%3.2f')
    np.savetxt('TI'+str(archivo_nombre)+'.out',injection_time,fmt='%3.2f')
    np.savetxt('Total'+str(archivo_nombre)+'.out',(SNRrec,SNRexp,total_flag,trigger_time,injection_time),fmt='%3.2f')

          
   
    return

###############################################################################
###############################################################################
#									      							                        #
#			 	Multiprocessing part		      	      			                  #
#									      						                           #
###############################################################################
###############################################################################

#------------------------------------------------------------------------------
#	You can choose any number of processes to be ran, each will execute 1
#	single time the above function.

processes = []

Num_Process = 2

a = 0

loc = False





#files = [1129623552,1129541632,1129627648,1129631744,1129639936,1129545728,1129558016,1129451520,1129439232,1129459712,1129517056,1129512960]


files = [1129623552,1129541632]


for nombre in files:
    
    url = 'https://www.gw-openscience.org/archive/data/O1_16KHZ/1129316352/L-L1_LOSC_16_V1-'
    urllib.urlretrieve(url+str(nombre)+'-4096.gwf', str(nombre)+'.gwf')


for fila in files:

    
    t = multiprocessing.Process(target=principal, args=(2,fila,loc))
    
    processes.append(t)
    t.start()

for one_process in processes:

    one_process.join()
