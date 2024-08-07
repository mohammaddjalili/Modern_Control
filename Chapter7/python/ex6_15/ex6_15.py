# -*- coding: utf-8 -*-
"""ex6_15.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QRD3AeEjjJUEyIb5e-S9xyctth4CHB6G
"""

import numpy as np
import control

# Define the system matrices
A = np.array([[0, 1, 0, 0],
              [0, 0, 4.438, -7.396],
              [0, -12, -24, 0],
              [0, 0, 0, -1]])

b = np.array([[0], [0], [20], [0]])

# Define the weighting matrices
R = 1
Q1 = np.diag([9, 0, 0, 0])

# Calculate the LQR gain matrix
k, _, _ = control.lqr(A, b, Q1, R)

print("LQR gain matrix k:")
print(k)