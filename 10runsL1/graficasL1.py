# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 11:46:44 2018

@author: jprieto

"""
import numpy as np
import pylab

di = [1,5,10,15,20,25,30,35,40,45,50]


Nsegmnt = 128

N_d = 11

N_f = 10

tw = 0.47

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
fg = []



files = [1129623552,1129541632,1129627648,1129639936,1129545728,1129558016,1129451520,1129439232,1129517056,1129512960]

SNRrec = []
SNRexp = []

for fi in files:
    
    

    fila = open('Total'+str(fi)+'.out','r')

    recc = fila.readline()

    reco = list(map(float,recc.split()))
    
    expe =  fila.readline()
    
    exx = list(map(float,expe.split()))
    
    f = fila.readline()
    
    flag = list(map(float,f.split()))
    
    trig = fila.readline()
    
    ttt = list(map(float,trig.split()))
    
    injec = trig = fila.readline()
    
    tti = list(map(float,injec.split()))
    
    re.extend(reco)
    ex.extend(exx)
    fg.extend(flag)
    tt.extend(ttt)
    ti.extend(tti)
    
del flag
Triger = []
Injection = []
SNRr=[]
SNRe=[]
flag = []



for i in range(Nsegmnt*N_f*N_d):

    Triger.append(tt[i])
    Injection.append(ti[i])
    flag.append(fg[i])
    SNRr.append(re[i])
    SNRe.append(ex[i])
    


    

    if (i+1) % 11 == 0:
        
        
        tri.append(Triger)
        inj.append(Injection)
        bandera.append(flag)
        exp.append(SNRe)
        rec.append(SNRr)
        
        
        Triger = []
        Injection = []
        flag = []
        SNRr=[]
        SNRe=[]
####################################################################################################################
tt=[]
ti=[]
flag=[]
re=[]
ex=[]

    
for i in range(len(tri[0])):
    
    a = []
    b = []
    c = []
    d = []
    e = []
    
    
    for j in range(len(tri)):
        
        a.append(tri[j][i])
        b.append(inj[j][i])
        c.append(bandera[j][i])
        d.append(rec[j][i])
        e.append(exp[j][i])
        
        
        
    tt.append(a)
    ti.append(b)
    flag.append(c)
    re.append(d)
    ex.append(e)
    


###########################################################################################################



N_s =[]

a = 0

for i in range(len(flag)):
    
    contador = 0
    
    for j in range(len(flag[0])):
        
        a = flag[i][j]
        
        contador = contador + a
    
    
    N_s.append(contador)

################################################################################

rec_av=[]
exp_av=[]

N_tp = []


rec_t = []
exp_t = []

rec_f = []
exp_f = []

for i in range(len(tt)):
    
    contador = 0
    a = []
    b = []    

    for j in range(len(tt[0])):
        
        
        if flag[i][j] == 1:
        
            if ti[i][j] <= tt[i][j] <= (ti[i][j]+tw):
            
                contador = contador + 1
                
                ind = re[i][j]
                rec_t.append(re[i][j])
                a.append(ind)
                exp_t.append(ex[i][j])
                b.append((ex[i][j]))
        else:
            
                rec_f.append(re[i][j])
                exp_f.append(ex[i][j])
                
            
            
        
    N_tp.append(contador)
    rec_av.append(np.average(a))
    exp_av.append(np.average(b))
    
##################################################################################        
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
"""
rec_av = []


for i in range(len(re)):
    
    a=[]
    
    
    
    for j in range(len(re[0])):
        
        if flag[i][j] == 1:
        
            a.append(re[i][j])
        
    
    rec_av.append(np.average(a))
"""
##################################################################################    
   


pylab.loglog(exp_t,rec_t,'*')
pylab.loglog(exp_av,rec_av,'o-',label='Average')
pylab.title('L1 Detections')
pylab.xlabel('SNRexp',fontsize=20)
pylab.ylabel('SNRrec',fontsize=20)
pylab.xlim((1,50))
pylab.ylim((1,50))
pylab.grid()
pylab.legend()
pylab.show()

pylab.loglog(exp_f,rec_f,'*')
pylab.title('L1 No Detections')
pylab.xlabel('SNRexp',fontsize=20)
pylab.ylabel('SNRrec',fontsize=20)
pylab.xlim((1,50))
pylab.ylim((1,50))
pylab.grid()
pylab.show()

pylab.plot(di,exx[0:11])
pylab.xlabel('Distance (Kpc)')
pylab.title('L1')
pylab.ylabel('SNRexp')
pylab.grid()
pylab.show()

pylab.plot(exp_av,DP,'-o')
pylab.xlabel('SNRexp (1280 runs average)')
pylab.title('L1')
pylab.ylabel('Detection efficiency')
pylab.grid()
pylab.show()


pylab.plot(rec_av,DP,'-o')
pylab.title('L1')
pylab.xlabel('SNRrec (1280 runs average)')
pylab.ylabel('Detection efficiency')
pylab.grid()
pylab.show()




pylab.plot(di,DP,label='Detection probability')
pylab.plot(di,FD,label='False detection')
pylab.title('L1')
#pylab.plot(di,alpha,label='False positive rate')
pylab.legend()
pylab.grid()
pylab.xlabel('Distance (Kpc)')
pylab.ylabel('Rate')
pylab.show()
    
pylab.plot(di,FD,'-',label='False detection')
pylab.title('L1')
#pylab.plot(di,alpha,label='False positive rate')
pylab.legend()
pylab.grid()
pylab.xlabel('Distance (Kpc)')
pylab.ylabel('Rate')
pylab.show()
    
pylab.plot(di,DP,'-o',label='Detection efficiency')

pylab.title('H1')
#pylab.plot(di,alpha,label='False positive rate')
pylab.legend()
pylab.grid()
pylab.xlabel('Distance (Kpc)')
pylab.ylabel('Rate')
pylab.show()

