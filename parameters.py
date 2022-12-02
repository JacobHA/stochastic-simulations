# Store the parameters for the model

import numpy as np

t = 15  # duration

initials = [10, 15, 0]  # a, b, c

# a -> b, Population change: a - 1, b + 1
# b -> a, Population change: a + 1, b - 1
# b -> c, Population change: b - 1, c + 1
# c -> b, Population change: b + 1, c - 1

stoichiometry = [[-1, 1, 0],
                 [1, -1, 0],
                 [0, -1, 1],
                 [0, 1, -1]]

alpha = 0.5
beta = 0.5
gamma = 0.5
deltas = np.linspace(0.001, 0.5, 250)
