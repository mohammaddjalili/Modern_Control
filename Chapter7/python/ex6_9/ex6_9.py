# -*- coding: utf-8 -*-
"""ex6_9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eUnN9-RmEe9XHoRJRnQwY4Lf41mef1rL
"""

import numpy as np
import control as ctrl

# Define matrices A, B, and f
A = np.array([[-2, -1, 2], [-1, -2, 2], [-2, 0, 2]])
B = np.array([[0, 0], [0, 1], [1, 0]])
f = np.array([[1], [1]])

b = np.dot(B, f)
# Calculate controllability matrix C
C = ctrl.ctrb(A, b)
# Desired closed-loop poles (modified to a 1D array)
pd = np.array([-2, -2, -2])  # Changed to a 1D array

Psi = np.array([[1, 2, -1],[0, 1 ,2],[0, 0, 1]])

delta = np.array([4, 13, 10]).reshape((-1, 1))
M = np.dot(delta.T, np.linalg.inv(np.dot(C,Psi)))
K1= np.dot(f, M)

# Calculate state feedback gain K using control.acker
K = ctrl.acker(A, b, pd)

# Calculate K1
K1 = np.dot(f,M)
# Calculate K1
K2 = np.dot(f,K)

# Calculate the closed-loop system matrix Ac and its eigenvalues
Ac = A - np.dot(B, K1)
eigenvalues, _ = np.linalg.eig(Ac)
# Print results
print('M: ')
print(M)
print(" K:")
print(K)
print("\n K1:")
print(K1)
print("\n K2:")
print(K2)
print("\nEigenvalues of Ac:")
print(eigenvalues)