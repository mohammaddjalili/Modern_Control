# -*- coding: utf-8 -*-
"""ex5_4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BbSmTDXQ5XRyLRD889Btajuz2dvcAJTl
"""

import numpy as np
from scipy import signal

# Define state-space matrices directly
A = [[-1, 0], [1, -1]]
B = [[2], [1]]
C = [[1, 0]]
D = [[0]]

# Create the state-space system
sys = signal.StateSpace(A, B, C, D)

# Define a function to simplify state-space representation (mimicking minreal)
def my_minreal(sys):
    # Extract matrices from the system
    A, B, C, D = sys.A, sys.B, sys.C, sys.D

    # Reduce to minimal realization (example here is a basic form, not full reduction)
    A_min, B_min, C_min, D_min = A, B, C, D  # Placeholder for minimal realization

    # Create a new StateSpace system with minimal realization
    return signal.StateSpace(A_min, B_min, C_min, D_min)

# Simplify the state-space system (mimicking minreal)
sys_min = my_minreal(sys)

# Display the simplified state-space system
print(sys_min)