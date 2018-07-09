import numpy as np

a = np.array([1010, 1000, 900])
np.exp(a) / np.sum(np.exp(a))
c = np.max(a)
a - c
np.exp(a - c) / np.sum(np.exp(a - c))