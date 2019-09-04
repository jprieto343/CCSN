#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 14:26:25 2018

@author: jprieto
"""

import numpy as np
import random as randi
import os
    
def lectura(n,aprox):
    
    
    
    directorio = '/Datsets/'
#	The total amount of templates are listed below, this function gives you a template
#	according with the choosen index     
    catalogo =[]
    
    if aprox == 'LS':
    	
     #68   
    	catalogo = [
		directorio+'signal_e15a_ls.dat',
		directorio+'signal_e15b_ls.dat',
		directorio+'signal_e20a_ls.dat',
		directorio+'signal_e20b_ls.dat',
                directorio+'signal_s11a1o01_ls.dat'	,
                directorio+'signal_s11a1o05_ls.dat'	,
                directorio+'signal_s11a1o07_ls.dat'	,
                directorio+'signal_s11a1o09_ls.dat'	,
                directorio+'signal_s11a1o13_ls.dat'	,
                directorio+'signal_s11a2o05_ls.dat'	,
                directorio+'signal_s11a2o07_ls.dat'	,
                directorio+'signal_s11a2o09_ls.dat'	,
                directorio+'signal_s11a2o13_ls.dat'	,
                directorio+'signal_s11a2o15_ls.dat'	,
                directorio+'signal_s11a3o05_ls.dat'	,
                directorio+'signal_s11a3o07_ls.dat'	,
                directorio+'signal_s11a3o09_ls.dat'	,
                directorio+'signal_s11a3o12_ls.dat'	,
                directorio+'signal_s11a3o13_ls.dat'	,
                directorio+'signal_s11a3o15_ls.dat'	,
                directorio+'signal_s15a1o01_ls.dat'	,
                directorio+'signal_s15a1o05_ls.dat'	,
                directorio+'signal_s15a1o07_ls.dat'	,
                directorio+'signal_s15a1o09_ls.dat'	,
                directorio+'signal_s15a1o13_ls.dat'	,
                directorio+'signal_s15a2o05_ls.dat'	,
                directorio+'signal_s15a2o07_ls.dat'	,
                directorio+'signal_s15a2o09_ls.dat'	,
                directorio+'signal_s15a2o13_ls.dat'	,
                directorio+'signal_s15a2o15_ls.dat'	,
                directorio+'signal_s15a3o05_ls.dat' ,
                directorio+'signal_s15a3o07_ls.dat'	,
                directorio+'signal_s15a3o09_ls.dat'	,
                directorio+'signal_s15a3o12_ls.dat'	,
                directorio+'signal_s15a3o13_ls.dat'	,
                directorio+'signal_s15a3o15_ls.dat'	,
                directorio+'signal_s20a1o01_ls.dat'	,
                directorio+'signal_s20a1o05_ls.dat'	,
                directorio+'signal_s20a1o07_ls.dat'	,
                directorio+'signal_s20a1o09_ls.dat'	,
                directorio+'signal_s20a1o13_ls.dat'	,
                directorio+'signal_s20a2o05_ls.dat'	,
                directorio+'signal_s20a2o07_ls.dat'	,
                directorio+'signal_s20a2o09_ls.dat'	,
                directorio+'signal_s20a2o13_ls.dat'	,
                directorio+'signal_s20a2o15_ls.dat'	,
                directorio+'signal_s20a3o05_ls.dat'	,
                directorio+'signal_s20a3o07_ls.dat'	,
                directorio+'signal_s20a3o09_ls.dat'	,
                directorio+'signal_s20a3o12_ls.dat'	,
                directorio+'signal_s20a3o13_ls.dat'	,
                directorio+'signal_s20a3o15_ls.dat'	,
                directorio+'signal_s40a1o01_ls.dat'	,
                directorio+'signal_s40a1o05_ls.dat'	,
                directorio+'signal_s40a1o07_ls.dat'	,
                directorio+'signal_s40a1o09_ls.dat'	,
                directorio+'signal_s40a1o13_ls.dat'	,
                directorio+'signal_s40a2o05_ls.dat'	,
                directorio+'signal_s40a2o07_ls.dat'	,
                directorio+'signal_s40a2o09_ls.dat'	,
                directorio+'signal_s40a2o13_ls.dat'	,
                directorio+'signal_s40a2o15_ls.dat'	,
                directorio+'signal_s40a3o05_ls.dat'	,
                directorio+'signal_s40a3o07_ls.dat'	,
                directorio+'signal_s40a3o09_ls.dat'	,
                directorio+'signal_s40a3o12_ls.dat'	,
                directorio+'signal_s40a3o13_ls.dat'	,
                directorio+'signal_s40a3o15_ls.dat']
        

	if aprox == 's20a1':
               catalogo = [directorio+'signal_a1b0.05.dat'	,
                    directorio+'signal_a1b0.07.dat'	,
                    directorio+'signal_a1b0.10.dat'	,
                    directorio+'signal_a1b0.15.dat'	,
                    directorio+'signal_a1b0.25.dat'	,
                    directorio+'signal_a1b0.35.dat'	,
                    directorio+'signal_a1b0.50.dat'	,
                    directorio+'signal_a1b0.70.dat'	,
                    directorio+'signal_a1b0.90.dat'	,
                    directorio+'signal_a1b1.10.dat'	,
                    directorio+'signal_a1b1.30.dat'	,
                    directorio+'signal_a1b1.60.dat'	,
                    directorio+'signal_a1b1.80.dat'	,
                    directorio+'signal_a1b2.00.dat'	,
                    directorio+'signal_a1b2.50.dat'	,
                    directorio+'signal_a1b3.00.dat'	,
                    directorio+'signal_a1b3.50.dat'	,
                    directorio+'signal_a1b4.00.dat']
        
        
    if aprox == 's20a2':
    	catalogo = [directorio+'signal_a2b0.05.dat',
                    directorio+'signal_a2b0.07.dat'	,
                    directorio+'signal_a2b0.10.dat'	,
                    directorio+'signal_a2b0.15.dat'	,
                    directorio+'signal_a2b0.25.dat'	,
                    directorio+'signal_a2b0.35.dat'	,
                    directorio+'signal_a2b0.50.dat'	,
                    directorio+'signal_a2b0.70.dat'	,
                    directorio+'signal_a2b0.90.dat'	,
                    directorio+'signal_a2b1.10.dat'	,
                    directorio+'signal_a2b1.30.dat'	,
                    directorio+'signal_a2b1.60.dat'	,
                    directorio+'signal_a2b1.80.dat'	,
                    directorio+'signal_a2b2.00.dat'	,
                    directorio+'signal_a2b2.50.dat'	,
                    directorio+'signal_a2b3.00.dat'	,
                    directorio+'signal_a2b3.50.dat'	,
                    directorio+'signal_a2b4.00.dat']

	if aprox == 's20a3':

		catalogo = [directorio+'signal_a3b0.05.dat',
                    directorio+'signal_a3b0.07.dat'	,
                    directorio+'signal_a3b0.10.dat'	,
                    directorio+'signal_a3b0.15.dat'	,
                    directorio+'signal_a3b0.25.dat'	,
                    directorio+'signal_a3b0.35.dat'	,
                    directorio+'signal_a3b0.50.dat'	,
                    directorio+'signal_a3b0.70.dat'	,
                    directorio+'signal_a3b0.90.dat'	,
                    directorio+'signal_a3b1.10.dat'	,
                    directorio+'signal_a3b1.30.dat'	,
                    directorio+'signal_a3b1.60.dat'	,
                    directorio+'signal_a3b1.80.dat'	,
                    directorio+'signal_a3b2.00.dat'	,
                    directorio+'signal_a3b2.50.dat'	,
                    directorio+'signal_a3b3.00.dat'	,
                    directorio+'signal_a3b3.50.dat'	,
                    directorio+'signal_a3b4.00.dat']
                        
    
    if aprox == 'SHEN':
            catalogo = [
                directorio+'signal_e15a_shen.dat',
                directorio+'signal_e15b_shen.dat',
                directorio+'signal_e20a_shen.dat',
                directorio+'signal_e20b_shen.dat',
                directorio+'signal_s11a1o01_shen.dat',
                directorio+'signal_s11a1o05_shen.dat',
                directorio+'signal_s11a1o07_shen.dat',
                directorio+'signal_s11a1o09_shen.dat',
                directorio+'signal_s11a1o13_shen.dat',
                directorio+'signal_s11a2o05_shen.dat',
                directorio+'signal_s11a2o07_shen.dat',
                directorio+'signal_s11a2o09_shen.dat',
                directorio+'signal_s11a2o13_shen.dat',
                directorio+'signal_s11a2o15_shen.dat',
                directorio+'signal_s11a3o05_shen.dat',
                directorio+'signal_s11a3o07_shen.dat',
                directorio+'signal_s11a3o09_shen.dat',
                directorio+'signal_s11a3o12_shen.dat',
                directorio+'signal_s11a3o13_shen.dat',
                directorio+'signal_s11a3o15_shen.dat',
                directorio+'signal_s15a1o01_shen.dat',
                directorio+'signal_s15a1o05_shen.dat',
                directorio+'signal_s15a1o07_shen.dat',
                directorio+'signal_s15a1o09_shen.dat',
                directorio+'signal_s15a1o13_shen.dat',
                directorio+'signal_s15a2o05_shen.dat',
                directorio+'signal_s15a2o07_shen.dat',
                directorio+'signal_s15a2o09_shen.dat',
                directorio+'signal_s15a2o13_shen.dat',
                directorio+'signal_s15a2o15_shen.dat',
                directorio+'signal_s15a3o05_shen.dat',
                directorio+'signal_s15a3o07_shen.dat',
                directorio+'signal_s15a3o09_shen.dat',
                directorio+'signal_s15a3o12_shen.dat',
                directorio+'signal_s15a3o13_shen.dat',
                directorio+'signal_s15a3o15_shen.dat',
                directorio+'signal_s20a1o01_shen.dat',
                directorio+'signal_s20a1o05_shen.dat',
                directorio+'signal_s20a1o07_shen.dat',
                directorio+'signal_s20a1o09_shen.dat',
                directorio+'signal_s20a1o13_shen.dat',
                directorio+'signal_s20a2o05_shen.dat',
                directorio+'signal_s20a2o07_shen.dat',
                directorio+'signal_s20a2o09_shen.dat',
                directorio+'signal_s20a2o13_shen.dat',
                directorio+'signal_s20a2o15_shen.dat',
                directorio+'signal_s20a3o05_shen.dat',
                directorio+'signal_s20a3o07_shen.dat',
                directorio+'signal_s20a3o09_shen.dat',
                directorio+'signal_s20a3o12_shen.dat',
                directorio+'signal_s20a3o13_shen.dat',
                directorio+'signal_s20a3o15_shen.dat',
                directorio+'signal_s40a1o01_shen.dat',
                directorio+'signal_s40a1o05_shen.dat',
                directorio+'signal_s40a1o07_shen.dat',
                directorio+'signal_s40a1o09_shen.dat',
                directorio+'signal_s40a1o13_shen.dat',
                directorio+'signal_s40a2o05_shen.dat',
                directorio+'signal_s40a2o07_shen.dat',
                directorio+'signal_s40a2o09_shen.dat',
                directorio+'signal_s40a2o13_shen.dat',
                directorio+'signal_s40a2o15_shen.dat',
                directorio+'signal_s40a3o05_shen.dat',
                directorio+'signal_s40a3o07_shen.dat',
                directorio+'signal_s40a3o09_shen.dat',
                directorio+'signal_s40a3o12_shen.dat',
                directorio+'signal_s40a3o13_shen.dat',
                directorio+'signal_s40a3o15_shen.dat']
            #68
    if aprox == 'NEW':
        template ='And1815fr1kpc_equ.txt'

    if aprox == 'NEW':

        archivo = template
        dt = np.loadtxt(archivo, usecols=(0))
        hp = np.loadtxt(archivo, usecols=(1))
        hc = np.loadtxt(archivo, usecols=(2))
        h = hp + hc

    elif aprox != 'NEW':

        #	Here, the information in the file is read and asigned to a variable, col 0 i the time and col 1 is the strain
        archivo = catalogo[n]
        dt = np.loadtxt(archivo, usecols=(0))
        h = np.loadtxt(archivo, usecols=(1))
        h = h / distance

    return h,dt,archivo
