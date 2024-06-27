

import numpy as np
from scipy.signal import place_poles

# Define the matrix A and vector c
A = np.array([
    [0, 1, 0, 0],
    [0, 0, 4.438, -7.396],
    [0, -12, -24, 0],
    [0, 0, 0, 0]
])

c = np.array([[1], [0], [0], [0]])

# Define the desired pole locations
pd = np.array([-5 + 5j, -5 - 5j, -7 + 7j, -7 - 7j])

# Use the place_poles function to find the gain matrix G
result = place_poles(A.T, c, pd)
G = result.gain_matrix

# Print the result
print("Gain matrix G:\n", G)
