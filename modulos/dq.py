import numpy as np
import matplotlib.pyplot as plt
import h5py

#----------
# Open File
#----------
filename = 'H-H1_LOSC_4_V1-815411200-4096.hdf5'
dataFile = h5py.File(filename, 'r')

#-----------------------------
# Print out the channel names
#-----------------------------
dqInfo = dataFile['quality']['simple']
bitnameList = dqInfo['DQShortnames'].value
nbits = len(bitnameList)

for bit in range(nbits):
    print bit, bitnameList[bit]

#-----------------------------
# Make 1 Hz DQ Channels
#----------------------------
qmask = dqInfo['DQmask'].value
sci = (qmask >> 0) & 1
burst1  = (qmask >> 9) & 1
goodData_1hz = sci & burst1

#-------------------------
# Plot DQ channels
#-------------------------
plt.plot(goodData_1hz + 4, label='Good_Data')
plt.plot(burst1 + 2, label='BURST_CAT1')
plt.plot(sci, label='DATA')
plt.axis([0, 4096, -1, 8])
plt.legend(loc=1)
plt.xlabel('Time (s)')

# ----------------------
# Obtain a segment list
# based on "good data"
# ---------------------
gpsStart = dataFile['meta']['GPSstart'].value
dummy = np.zeros(goodData_1hz.shape)
masked_dummy = np.ma.masked_array(dummy, np.logical_not(goodData_1hz) )
segments = np.ma.flatnotmasked_contiguous(masked_dummy)
segList = [(int(seg.start+gpsStart), int(seg.stop+gpsStart)) for seg in segments]

