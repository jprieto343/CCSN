# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 10:03:08 2018

@author: chiva
"""

import numpy as np
import pylab

files = [1126105088,1126100992]

rec1 = np.loadtxt('SNRrec1126105088.out',usecols=(0))
rec2 = np.loadtxt('SNRrec1126100992.out',usecols=(0))
exp1 = np.loadtxt('SNRexp1126105088.out',usecols=(0))
exp2 = np.loadtxt('SNRexp1126100992.out',usecols=(0))
tt1 = np.loadtxt('TT1126105088.out',usecols=(0))
tt2 = np.loadtxt('TT1126100992.out',usecols=(0))
ti1 = np.loadtxt('TI1126105088.out',usecols=(0))
ti2 = np.loadtxt('TI1126100992.out',usecols=(0))
flag1 = np.loadtxt('FLAG1126100992.out',usecols=(0))
flag2 = np.loadtxt('FLAG1126105088.out',usecols=(0))
di = [1,5,10,15,20,25,30,35,40,45,50]


Nsegmnt = 128

N_d = 11



tt = []
ti = []
flag = []
exp = []
rec = []

tri = []
inj = []
bandera = []
ex = []
re = []

for i in range(Nsegmnt*N_d):
    
    
    tri.append(tt1[i])
    inj.append(ti1[i])
    bandera.append(flag1[i])
    re.append(rec1[i])
    ex.append(exp1[i])
    
    if (i+1) % 11 == 0:
        
        
        tt.append(tri)
        ti.append(inj)
        flag.append(bandera)
        exp.append(ex)
        rec.append(re)
        
        
        tri = []
        inj = []
        bandera = []
        ex = []
        re = []
        

tri = []
inj = []
bandera = []
ex = []
re = []
    
for i in range(len(tt[0])):
    
    a = []
    b = []
    c = []
    d = []
    e = []
    
    
    for j in range(len(tt)):
        
        a.append(tt[j][i])
        b.append(ti[j][i])
        c.append(flag[j][i])
        d.append(rec[j][i])
        e.append(exp[j][i])
        
        
        
    tri.append(a)
    inj.append(b)
    bandera.append(c)
    re.append(d)
    ex.append(e)
    

N_s =[]

a = 0

for i in range(len(bandera)):
    
    contador = 0
    
    for j in range(len(bandera[0])):
        
        a = bandera[i][j]
        
        contador = contador + a
    
    
    N_s.append(contador)

N_tp = []

rec_t = []
exp_t = []

rec_f = []
exp_f = []

for i in range(len(tri)):
    
    contador = 0
    
    for j in range(len(tri[0])):
        
        
        if bandera[i][j] == 1:
        
            if inj[i][j] <= tri[i][j] <= (inj[i][j]+0.47):
            
                contador = contador + 1
            
                rec_t.append(re[i][j])
                exp_t.append(ex[i][j])
                
        else:
            
                rec_f.append(re[i][j])
                exp_f.append(ex[i][j])
                
    
        
    N_tp.append(contador)
        
# detection probability

DP = []  

# false detection

FD = [] 

# false positives

N_fp = [] 

# no triggers

N_n = []    


alpha = []

    
for i in range(len(N_s)):
    
    
    N_fp.append(N_s[i]-N_tp[i])
    
    if N_s[i] == 0:
        
        DP.append(0)
        FD.append(1)
        
        
        
    else:
        
        DP.append(N_tp[i]/N_s[i])
        FD.append(N_fp[i]/N_s[i])



for i in range(len(N_s)):
    
    
    N_n.append(Nsegmnt-N_s[i])
    
    if N_n[i] == 0:
        
        alpha.append(0)
    else:
        
        alpha.append(N_fp[i]/N_n[i])




###############################################################################
###############################################################################

rec_av = []


for i in range(len(re)):
    
    a=[]
    
    for j in range(len(re[0])):
        
        a.append(re[i][j])
        
    
    rec_av.append(np.average(a))



pylab.loglog(exp_t,rec_t,'-*')
pylab.title('L1')
pylab.grid()
pylab.xlim((1,50))
pylab.ylim((1,50))
pylab.show()

pylab.loglog(exp_f,rec_f,'-*')
pylab.title('L1')
pylab.xlim((1,50))
pylab.ylim((1,50))
pylab.grid()
pylab.show()


pylab.plot(rec_av,DP)
pylab.title('L1')
pylab.xlabel('SNRrec (128 runs average)')
pylab.ylabel('Detection efficiency')
pylab.grid()
pylab.show()


pylab.plot(di,exp1[0:11],'-')
pylab.title('L1')
pylab.xlabel('Distance (Kpc)')
pylab.ylabel('SNRexp')
pylab.grid()
pylab.show()


pylab.plot(exp1[0:11],DP)
pylab.title('L1')
pylab.xlabel('SNRexp')
pylab.ylabel('Detection efficiency')
pylab.grid()
pylab.show()




pylab.plot(di,FD,'-',label='False detection')
pylab.title('L1')
#pylab.plot(di,alpha,label='False positive rate')
pylab.legend()
pylab.grid()
pylab.xlabel('Distance (Kpc)')
pylab.ylabel('Rate')
pylab.show()
    
pylab.plot(di,DP,'-',label='Detection efficiency')

pylab.title('L1')
#pylab.plot(di,alpha,label='False positive rate')
pylab.legend()
pylab.grid()
pylab.xlabel('Distance (Kpc)')
pylab.ylabel('Rate')
pylab.show()
    