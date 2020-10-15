"""
Author: Yousef Nami
Problem description: convert matrix equation of a multibody mechanical system into a state-space form
Date started: 15.10.2020
Date complete: 15.10.2020
"""
import numpy as np

def convert_to_space(M: 'in KG' = np.asarray([[1,0],[0,1]]),
                    
                     ):
    """
    Converts a matrix equation of a multibody mechanical system into state-space form
    
    Parameters
    ----------
    mass : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    if isinstance(M, list):
        n = int(np.sqrt(len(M)))
        M = np.asarray(M).reshape(-n,n)
        
    