import numpy as np
import math


# Number of oscillators
n = int(input('Enter the number of oscillators: ')) 


# Define frequencies 
try:
    oscillator_systems = {}
    for i in range(n):
        mass = eval(input('Enter the mass of oscillator {}: '.format(i+1)))
        spring_constant = eval(input('Enter the spring constant of oscillator {}: '.format(i+1)))
        oscillator_systems['Oscillator {}'.format(i)] = [mass, spring_constant]

except:
    if mass != int() or mass != float():
        raise ValueError('Invalid entry for oscillator mass')
    
    if spring_constant != int() or spring_constant != float():
        raise ValueError('Invalid entry for oscillator spring constant')

omega_array = []    
for key, values in oscillator_systems.items():
    oscillator_mass, oscillator_spring_const = values
    omega = math.sqrt(oscillator_spring_const / oscillator_mass)
    omega_array.append(omega)
    

# Define coupling strengths 
Coupling_values = input("Enter coupling values separated by commas: ")
input_list = Coupling_values.split(',')
Coupling_matrix = np.array(input_list, dtype=float).reshape(n, n)

# Construct the matrix for the eigenvalue problem
M = np.diag(omega_array**2) - Coupling_matrix

# Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(M)

num_columns = eigenvectors.shape[1]

# Iterate through the columns and print each column
for i in range(num_columns):
    column_i = eigenvectors[:, i]
    print("Eigenvector", i + 1, ":", column_i)
    print()
