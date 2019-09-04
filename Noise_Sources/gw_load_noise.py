""""
This module loads the noise data from  the detectors

"""


def get_noise(detector):

    import pycbc.frame as frame
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

    l1_list = ['L-L1_LOSC_16_V1-1126088704-4096.gwf', 'L-L1_LOSC_16_V1-1126105088-4096.gwf',
               'L-L1_LOSC_16_V1-1127018496-4096.gwf', 'L-L1_LOSC_16_V1-1127022592-4096.gwf',
               'L-L1_LOSC_16_V1-1127030784-4096.gwf',
               'L-L1_LOSC_16_V1-1127051264-4096.gwf', 'L-L1_LOSC_16_V1-1127059456-4096.gwf',
               'L-L1_LOSC_16_V1-1127096320-4096.gwf', 'L-L1_LOSC_16_V1-1129521152-4096.gwf',
               'L-L1_LOSC_16_V1-1134870528-4096.gwf',
               'L-L1_LOSC_16_V1-1136615424-4096.gwf', 'L-L1_LOSC_16_V1-1136631808-4096.gwf']

    l1_begin = [1126088704, 1126105088, 1127018496, 1127022592, 1127030784, 1127051264, 1127059456, 1127096320,
                1129521152, 1134870528, 1136615424, 1136631808]

    if detector == 'O1-H':

        file_index = randi.randrange(1, 12, 1)
        print file_index

        a = h1_begin[file_index]
        print a

        start_time = randi.randrange(a, a + 4054, 1)
        print start_time

        file = h1_list[file_index]
        print file

        strain = frame.read_frame(file, 'H1:GWOSC-16KHZ_R1_STRAIN')

    elif detector == 'O1-L':

        a = l1_begin[file_index]
        print a
        file_index = randi.randrange(1, 12, 1)
        print file_index
        start_time = randi.randrange(a, l1_begin[file_index] + 4054, 1)
        print start_time

        file = l1_list[file_index]

        strain = frame.read_frame(file, 'L1:GWOSC-16KHZ_R1_STRAIN', start_time, start_time + 32)

    shift = randi.randrange(5, 27, 1)

    return strain, shift
