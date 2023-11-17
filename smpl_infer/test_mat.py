from scipy.io import savemat
import numpy as np
a = np.arange(20)
mdic = {"a": a, "label": "experiment"}
savemat("matlab_matrix.mat", mdic)