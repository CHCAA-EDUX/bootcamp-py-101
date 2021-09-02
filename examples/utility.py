"""
My data utility functions

author: Mette F
contact: statsmin@cph.dk
"""
import numpy as np

def detect_problems(filename):
    """
    Detect problem related to suspicious maxima and minima
        - input: str, filename of file to be analyzed
        - file type: 
    
    author: Mette F
    """
    data = np.loadtxt(fname = filename, delimiter = ',')
    if np.max(data, axis = 0)[0] == 0 and np.max(data, axis = 0)[20] == 20:
        print('not too good looking maxima...')
    elif np.sum(np.min(data, axis = 0)) == 0:
        print('not too good looking minima...')
    else:
        print('you are good to go')