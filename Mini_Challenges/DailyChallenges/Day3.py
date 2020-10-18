"""
Author: Yousef Nami
Problem description: convert matrix equation of a multibody mechanical system into a state-space form
Date started: 15.10.2020
Date complete: 16.10.2020
"""
import numpy as np

def convert_to_space(M: 'in KG or KG m^2' = np.asarray([[1,0],[0,1]]),
                     K: 'in N/m or N/theta radians' = np.asarray([[1,-1],[-1,1]]),
                     C: 'in N/m*s or N/theta radians*s' = np.array([[0,0],[0,0]]),
                     f: 'in N' = [0,0]
                     ):
    """
    Converts a matrix equation of a multibody mechanical system into state-space form
    
    The matrix equation is of the form:
        M * x_ddot + C * x_dot + K * x = f
        Where all the paramters have their usual meaning
        The convenction for x is: x = [x1, x2, x3, theta_x1, theta_x2, theta_x3]
        
    State-space form:
        x_dot = A * x + B * u
        Note here that the direction vectors (x_dot, x are concatenated)
        So we have: x = [x1, x2 ... xn, x1_dot, x2_dot ... xn_dot]
        And therefore, x_dot = [x1_dot, x2_dot ... xn_dot, x1_ddot, x2_ddot ... xn_ddot]
    
    Parameters
    ----------
    M (optional -- defaults to 1 unit per each mass): np.array OR list
        The mass matrix for the equationof motion. Note that in the case of rotations, you have the mass moment
        of inertia instead of mass.
        
    K (optional -- defaults to 1 unit per each mass): np.array OR list
        The sitffness matrix for the equation of motion.
        
    C (optional -- defaults to 0 i.e. no damping): np.array or list
        The damping matrix for the equation of motion.
    
    f (optional -- defaults to 0 i.e. no harmonic force): list
        The force vector

    Returns
    -------
    A: np.array
        This is the 'mass-stiffness' matrix in the state-space form of showing the equation of motion 
        
    B: np.array
        This is the 'force' vector in the atate-space form of showing the equation of motion
    """
    M = list_to_array(M) if isinstance(M,list) else M
    K = list_to_array(K) if isinstance(K,list) else K
    C = list_to_array(C) if isinstance(C,list) else C
    M_inv = np.linalg.inv(M)
    
    n = M.shape[0]
    A = np.concatenate(
        (np.zeros([n,n]), np.identity(2)),
        axis = 1
        )
    
    A = np.concatenate(
        (A, np.concatenate(
            (np.matmul(M_inv, K), np.matmul(M_inv, C)), axis = 1)
            ),
        axis = 0
        )

    B = np.zeros(n)
    B = np.concatenate(
        (B, np.matmul(M_inv, f))
        )
    
    # need to make sure that the force part of this is correct... technically according to
    # x_dot = Ax + Bu, Bu would be a hadamard product since B is actually a vector. Must check the correct
    # form of this before assuming that this is complete
    # need to think about how this works for a harmonic force?
    
    # need to check if the multiplication with f works
    # extension: can you extend this for the case of simulations? Also for he case of changing damping?
    
    return A, B
    
def list_to_array(input_list):
    n = int(np.sqrt(len(input_list)))
    return np.asarray(input_list).reshape(-n,n)

convert_to_space()