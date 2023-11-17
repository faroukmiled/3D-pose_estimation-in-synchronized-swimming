import numpy as np
import scipy.io as sio

# Charger le fichier .mat
mat_data = sio.loadmat('joints.mat')

# Convertir les données en tableaux NumPy
np_data = {}
for var_name, var_value in mat_data.items():
    if isinstance(var_value, np.ndarray):
        np_data[var_name] = var_value

# Enregistrer les tableaux NumPy dans un fichier .npz
np.savez('results/lsp/est_joints.npz', **np_data)

