import numpy as np
import math



class Matrix_Calulator:
    def __init__(self, matrix=[]):
        self.matrix = matrix
    
    '''Constructs a matrix using numpy'''
    def matrix_constructor(self):
        new_matrix = np.matrix(self.matrix)
        return new_matrix
    
    '''Returns the determinate of the constructed matrix'''
    def determinate_calculator(self):
        new_matrix = self.matrix_constructor()
        det = np.linalg.det(new_matrix)
        return print(det)
        

'''Uses the parent class of matrix calculator in order to construct matricies and calculate determinates'''
class Oscillations(Matrix_Calulator):
    def __init__(self, mass, spring_constant, coupling_constant): #initializes the mass, spring, and coupling const.
        super().__init__(matrix=[])
        self.mass = mass
        self.spring_constant = spring_constant
        self._coupling_constant = coupling_constant
    

    '''the excitation of two frequencies simultaneously, the sum of separate oscillating solutions becomes 
    the oscilation value for the equation of motion'''
    def angular_frequency(self, other):
        omega_1s = math.sqrt((self.spring_constant/self.mass))
        omega_2s = math.sqrt((other.spring_constant/other.mass))
        omega = ((omega_1s + omega_2s)/2)
        return omega
    
    def matrix_of_oscilation(self):
        pass
    
