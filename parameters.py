# Store the parameters for the model

import numpy as np

t = 150  # duration

initials = [10, 10, 0, 0, 0, 0]  # a, b, c

# a -> b, Population change: a - 1, b + 1
# b -> a, Population change: a + 1, b - 1
# b -> c, Population change: b - 1, c + 1
# c -> b, Population change: b + 1, c - 1
# a -> na, Population change: a, na + 1
# b -> nb, Population change: b, nb + 1
# c -> nc, Population change: c, nc + 1

stoichiometry = [[-1, 1, 0, 0, 0, 0],
                 [1, -1, 0, 0, 0, 0],
                 [0, -1, 1, 0, 0, 0],
                 [0, 1, -1, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 1]]

alpha = 1
beta = 1.5  # 0.1 for two crossings
gamma = 0.1
deltas = [0.000]  # np.linspace(0.001, 0.5, 250)

# alpha = 1
# beta = 1
# gamma = 1
# deltas = [1]

# k_a = 0.5
# k_b = 0.5
# k_c = 0.5

k_a = 3
k_b = 1.5
k_c = 2
