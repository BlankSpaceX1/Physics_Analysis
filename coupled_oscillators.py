import numpy as np


# Number of oscillators
n = int(input('Enter the number of oscillators: ')) 


# Define frequencies 
omega = input("Enter frequencies separated by comma: ")

try:
    omega_array = np.array(omega.split(','), dtype=float)
except:
    ValueError

# Define coupling strengths 
Coupling_values = input("Enter coupling values separated by commas (defined as k_ij and x_i): ")
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
    print("Column", i + 1, ":", column_i)
