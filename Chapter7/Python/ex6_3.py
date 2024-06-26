# -*- coding: utf-8 -*-
"""ex6_3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kE0JEQl1PyTLZP1W_g1O7qm5uy4Fu3-E
"""

import numpy as np
from scipy.linalg import solve_continuous_are
from scipy.linalg import inv


# Define matrices and vectors
A = np.array([[0, 1, 0, 0],
              [0, 0, -9.8, 0],
              [0, 0, 0, 1],
              [0, 0, 19.6, 0]])
b = np.array([[0],
              [1],
              [0],
              [-1]])
Q = np.diag([4, 0, 8.16, 0])
R = 1/400

# Solving the continuous time Algebraic Riccati Equation (ARE)
P = solve_continuous_are(A, b, Q, R)

# Calculating the LQR gain matrix
k = np.dot(inv(R), np.dot(b.T, P))

print("Gain matrix k:")
print(k)

import numpy as np
from scipy.linalg import solve_continuous_are

# Define matrices and vectors
A = np.array([[0, 1, 0, 0],
              [0, 0, -9.8, 0],
              [0, 0, 0, 1],
              [0, 0, 19.6, 0]])
b = np.array([[0],
              [1],
              [0],
              [-1]])
Q = np.diag([4, 0, 8.16, 0])
R = 1/400

# Solving the continuous time Algebraic Riccati Equation (ARE)
P = solve_continuous_are(A, b, Q, R)

# Calculating the LQR gain matrix
k = np.dot(np.linalg.inv(np.array([[R]])), np.dot(b.T, P))

print("Gain matrix k:")
print(k)