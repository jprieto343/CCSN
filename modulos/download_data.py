eventList = [
[815976703, 'GRB051114'],
[818228794, 'GRB051210'],
[818304618, 'GRB051211'],
[821917508, 'GRB060121'],
]

import json
import urllib


def fetchTimeline(timelineID, GPSstart, GPSend, level, detector, dataset='S5'):
    urlformat = 'https://www.gw-osc.orgtimelinejson/{0}/{1}_{2}/{3}/{4}/{5}/'
    url = urlformat.format(dataset, detector, timelineID, GPSstart, GPSend-GPSstart, level)
    print "Fetching ", url
    r = urllib.urlopen(url).read()
    timelines = json.loads(r)
    return timelines[0]

for event in eventList:
    t = event[0]   # GPS time of a GRB
    detector = 'H1'    # One of the detectors we are interested in
    level = 9          # so that 2^level seconds is about 2 minutes
    timelineData = fetchTimeline( 'CBCLOW_CAT2', t, t, level, detector)
    duty = timelineData[0][1]    # it returns a list that has one [time,duty] pair
    print "%s CAT2 duty cycle over 128 seconds: %3.2f" % (detector, duty)


def fetchStrain(GPStime, detector, dataset='S5'):
    observatory = detector[0]         # first letter of the detector H or L
    hour        = GPStime&0xFFFFF000  # the filename rounding down to a multiple of 4096
    fortnight   = GPStime&0xFFF00000  # the directory by rounding down to multiple of 4096*256
    filename = '{0}-{1}_LOSC_4_V1-{2}-4096.hdf5'.format(observatory, detector, hour)
    urlformat = 'https://www.gw-osc.orgarchive/data/{0}/{1}/{2}'
    url = urlformat.format(dataset, fortnight, filename)
    print "Fetching data file from ", url
    print 'Fetching ', filename,
    r = urllib.urlopen(url).read()
    f = open(filename, 'w')   # write it to the right filename
    f.write(r)
    f.close()

t = eventList[3][0]   # GPS time of a GRB
detector = 'H1'
fetchStrain(t, detector)