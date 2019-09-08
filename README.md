# CCSN
Data analysis pipeline of gravitational waves from Core Collapse Supernova. 


    D I S C L A I M E R:
    
    There are so much information needed to document all the technical stages of the pipeline as well as for the 
    theoretical information about the models used here, so it will take a significant amount of time to complete the 
	documentation.
    
	The whole idea here is to describe the methods contained on each module and give some practical examples. 
    
    

This pipeline goes from data collection to a succesful signal recognition with a matched filter technique (https://en.wikipedia.org/wiki/Matched_filter) which allow us to recover the optimal
signal to noise ratio (SNR) from a given template and a recorded signal. This pipeline also includes a Chi-squared veto.
 
 
 It's written on python 2.7. The libraries needed to run it are:
 
 - Numpy
 - Scipy
 - PyCBC
 
 
 Data can be directly downloaded from https://www.gw-openscience.org/about/ , be aware that for a trusty detection data segments need to 
 pass the data quality flags. 
 
