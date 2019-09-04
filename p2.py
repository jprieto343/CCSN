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
import time
import os

#----------------------------------------------------------------------------
#	Making the printed results directory
tiempo = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
carpeta = 'Resultados '+tiempo
os.mkdir(carpeta)

#############################################################################
#---------------------------------------------------------------------------#
#               	    Main cycle function				                    #
#---------------------------------------------------------------------------#
#############################################################################


def principal(runs,numero_hilo):


    print 'Hilo:'
    print numero_hilo

#   Loading our modules
    from modulos import gw_resample, gw_injection, gw_matched_filter, gw_visualization
    from modulos import  gw_detection, gw_expected, gw_qtransform, gw_data, gw_chisqv2, gw_readtemplatev2
    from Noise_Sources import gw_load_noise, load
    import numpy as np
    import random as randi
    import os
    grafica = 0

    dic = np.linspace(1,100,10)

    di = []

    di.extend(dic)


#   Creating vectors for the printed results and complete run

    SNRrec = []
    SNRexp = []
    indice = []
    flag = []
    ts = []
    tt = []
    lower_chisq= []


#-------------------------------------------------------------------------
#temporal stuff

    data_source = ['Gaussian','O1-H','O1-L']

    aprox = 'NEW'

    total_time = 32

    freq_sampling = 16384

#---------------------------------------------------------------------------#
#               loading files                                               #
#---------------------------------------------------------------------------#

    archivo = ['H-H1_LOSC_16_V1-1129644032-4096.gwf', 'H-H1_LOSC_16_V1-1129664512-4096.gwf']

    for ar in archivo:


        strain_initial = frame.read_frame(ar, 'H1:GWOSC-16KHZ_R1_STRAIN')

        strain_n = strain_initial.data

        del strain_initial

        strain_light = []

            for i in range(32):
                a = i * 32 * 16384
                b = (i + 1) * 32 * 16384

                strain_light.append(strain_n[a:b])


        for dat in  range(len(strain_light)):


            strain = strain_light[dat]

            k =  'Data'+str(dat)

            assert isinstance(runs, object)

            for d in range(len(di)):


                distancia = di[d]


                SNRrec = []
                SNRexp = []
                indice = []
                flag = []
                tof = []
                ts = []
                tt = []
                lower_chisq = []
                dist=[]




                n=numero

                #	Reading template
                h,dt,nombre,dista = gw_readtemplatev2.lectura(n,aprox,k)
                hh, dts,dtf = gw_resample.interpolacion(h,dt,grafica)
                tof.append(dtf)

                shift = randi.randrange(5, 27, 1)

                template, noise = gw_resample.resampleado(strain,hh,grafica)

                        #   Making uniform the distribution of the dt in the template
                        #   These function returns the resampled strain,

#						Resampling and resizing data

        #   Making the injection of the template into the data
                strain_inj,tmax,injection_shift = gw_injection.make(noise,template,shift,grafica)
                ts.append(tmax)

                        #   The limit values for the frequency in the filters
                fc = 15
                hc = 1500
                mc = 733
                        #	Making the matched filter
                        #	This function give us the timeseries object of the snr over the time, the maximum value of the snr and
    #	the time that it occurs
                snr,psd,index_snr_trigger,time,rho,psd_o,rho_0 = gw_matched_filter.make(strain_inj,template,fc,mc,hc,grafica)
                tt.append(time)

    #   Getting the Chi^2 value
                chisq, low_chisq,chisq_time = gw_chisqv2.xis(snr,template,strain_inj,psd_o,fc,grafica,time,dtf,hc,shift,index_snr_trigger)

    #   Getting the theoretical value of snr
    #   snr_predicted = gw_expected.make(template,strain_inj,psd,injection_shift,grafica)
#-------------------------------------------------------------------------------------------------------------------------
#   Detection part
                desicion = gw_detection.decision(tmax,time,dtf,rho,rho_0, low_chisq)

#--------------------------------------------------------------------------------------------------------------------------
#	The time, amplitude, and phase of the SNR peak tell us how to align
#	our proposed signal with the data.
                SNRrec.append(rho)
                SNRexp.append(rho_0)
                indice.append(n)
                flag.append(desicion)
                lower_chisq.append(low_chisq)
                dist.append(distancia)



                    
            os.chdir(carpeta)
            exp=open('expe'+str(k)+data+str(corrida)+'Thread'+numero_hilo+'.out','w')
            exp.close()
            rec=open('rec'+str(k)+data+str(corrida)+'Thread'+numero_hilo+'.out','w')
            rec.close()
            bandera=open('bandera'+str(k)+data+str(corrida)+'Thread'+numero_hilo+'.out','w')
            bandera.close()
            indic=open('indice'+str(k)+data+str(corrida)+'Thread'+numero_hilo+'.out','w')
            indic.close()
            bandera.close()
            tsn = open('snrmax'+str(k)+data+str(corrida)+'Thread'+numero_hilo+'.out','w')
            tsn.close()
            tm = open('templatetimemax'+str(k)+data+str(corrida)+'Thread'+numero_hilo+'.out','w')
            tm.close()
            chi=open('chi_l'+str(k)+data+str(corrida)+'Thread'+numero_hilo+'.out','w')
            chi.close()
            d = open('distance' + str(k)  + data + str(corrida) + 'Thread' + numero_hilo + '.out', 'w')
            d.close()
                    
                    


            for i in range(len(flag)):

                exp=open('expe'+str(k)+data+str(corrida)+'Thread'+numero_hilo+'.out','a')
                rec=open('rec'+str(k)+data+str(corrida)+'Thread'+numero_hilo+'.out','a')
                bandera=open('bandera'+str(k)+data+str(corrida)+'Thread'+numero_hilo+'.out','a')
                indic=open('indice'+str(k)+data+str(corrida)+'Thread'+numero_hilo+'.out','a')
                tsn = open('snrmax'+str(k)+data+str(corrida)+'Thread'+numero_hilo+'.out','a')
                tm = open('templatetimemax'+str(k)+data+str(corrida)+'Thread'+numero_hilo+'.out','a')
                chi = open('chi_l'+str(k)+data+str(corrida)+'Thread'+numero_hilo+'.out','a')
                distance = open('distance'+str(k)+data+str(corrida)+'Thread'+numero_hilo+'.out','a')
                a = np.abs(SNRrec[i])
                b = np.abs(SNRexp[i])
                c = np.abs(indice[i])
                d = np.abs(flag[i])
                f = np.abs(ts[i])
                g = np.abs(tt[i])
                h = lower_chisq[i]
                j = dist[i]
                print >> exp,a
                print >> rec,b
                print >> bandera,d
                print >> indic, c
                print >> tsn, f
                print >> tm, g
                print >> chi, h
                print >> distance, j
                exp.close()
                rec.close()
                bandera.close()
                indic.close()
                tsn.close()
                tm.close()
                chi.close()
                distance.close()
            os.chdir('../')

    return


###############################################################################
###############################################################################
#									      							          #
#			 	Multiprocessing part		      	      			          #
#									      						              #
###############################################################################
###############################################################################


#------------------------------------------------------------------------------
#	You can choose any number of processes to be ran, each will execute 1
#	single time the above function.

processes = []

Num_Process = 2

a = 0

for i in range(Num_Process):
    a = a + i
    b = str(a)
    t = multiprocessing.Process(target=principal, args=(2,b))
    
    processes.append(t)
    t.start()

for one_process in processes:

    one_process.join()

