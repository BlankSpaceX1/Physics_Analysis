import numpy as np

class Matrix_Calulator:
    def __init__(self, matrix=[]):
        self.matrix = matrix
    
    def matrix_constructor(self):
        new_matrix = np.matrix(self.matrix)
        return new_matrix
    
    def determinate_calculator(self):
        new_matrix = self.matrix_constructor()
        det = np.linalg.det(new_matrix)
        return print(det)
        
