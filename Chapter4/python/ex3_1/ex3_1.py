# -*- coding: utf-8 -*-
"""ex3_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1B1kMIbvyikf7cNz9rhl4Je4Lz9mQo8TK
"""

import numpy as np
import control as ctrl
from scipy.linalg import null_space
# Define matrices A and C
A = np.array([[-1.5, 0.5], [0.5, -1.5]])
C = np.array([[1, -1]])

# Compute the observability matrix using control library
O = ctrl.obsv(A, C)

# Compute the rank of the observability matrix
rank_O = np.linalg.matrix_rank(O)

# Compute the null space of the observability matrix
null_O = null_space(O)

print("Observability matrix O:\n", O)
print("Rank of O:", rank_O)
print("Null space of O:\n", null_O)