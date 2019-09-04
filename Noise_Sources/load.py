""""
This module loads the noise data from  the detectors

"""


def get_noise(detector):

    from pycbc import frame
    import random as randi
    import os



    h1_list = ['H-H1_LOSC_16_V1-1126084608-4096.gwf', 'H-H1_LOSC_16_V1-1126109184-4096.gwf',
               'H-H1_LOSC_16_V1-1126264832-4096.gwf', 'H-H1_LOSC_16_V1-1126293504-4096.gwf',
               'H-H1_LOSC_16_V1-1127194624-4096.gwf',
               'H-H1_LOSC_16_V1-1128042496-4096.gwf', 'H-H1_LOSC_16_V1-1128345600-4096.gwf',
               'H-H1_LOSC_16_V1-1128407040-4096.gwf', 'H-H1_LOSC_16_V1-1128624128-4096.gwf',
               'H-H1_LOSC_16_V1-1128665088-4096.gwf',
               'H-H1_LOSC_16_V1-1129127936-4096.gwf', 'H-H1_LOSC_16_V1-1129664512-4096.gwf']
    h1_begin = [1126084608, 1126109184, 1126264832, 1126293504, 1127194624, 1128042496, 1128345600, 1128407040,
                1128624128, 1128665088, 1129127936, 1129664512]



    if detector == 'O1-H':

        file = 'H-H1_LOSC_16_V1-1126084608-4096.gwf'

        strain = frame.read_frame(file, 'H1:GWOSC-16KHZ_R1_STRAIN',1126084608,1126084608+32)




    return strain
