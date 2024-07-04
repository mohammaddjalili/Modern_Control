# -*- coding: utf-8 -*-
"""train_model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10w8lY8BNvQodIuHxTkKCQj1cFz4BVVDs
"""

import numpy as np
from scipy.integrate import solve_ivp

def train_model(t, x):
    A = np.array([
        [0,    0,   0,   0,   0,    1,      0,      0,   0,   0],
        [0,    0,   0,   0,   0,    1,     -1,      0,   0,   0],
        [0,    0,   0,   0,   0,    0,      1,     -1,   0,   0],
        [0,    0,   0,   0,   0,    0,      0,      1,  -1,   0],
        [0,    0,   0,   0,   0,    0,      0,      0,   1,  -1],
        [0, -12.5,  0,   0,   0,  -0.75,   0.75,    0,   0,   0],
        [0,  62.5, -62.5, 0,  0,   3.75,  -7.5,   3.75,  0,   0],
        [0,  0, 62.5, -62.5,  0,    0,  3.75,  -7.5,  3.75,  0],
        [0,  0,  0, 62.5, -62.5,    0,     0,  3.75,  -7.5,  3.75],
        [0,    0,   0,   0,  62.5,  0,     0,    0,  3.75, -3.75]
    ])

    b1 = np.array([0, 0, 0, 0, 0, 0.005, 0, 0, 0, 0])  # Force input
    b2 = np.array([0, 0, 0, 0, 0, 250, 0, 0, 0, -1250])  # Constant input

    u = 750 * np.exp(-t / 10)  # Exponentially decreasing input
    # u = 750  # Constant input

    xp = A.dot(x) + b1 * u + b2
    return xp