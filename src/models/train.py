import numpy as np
from scipy.stats import linregress


def split_data(data_arr):
    """
    Splits data_arr into training and testing set
    """
    dim = data_arr.ndim
    if dim != 2:
        raise ValueError(f"Argument data_arr must be 2D. Got {dim}D array instead!")
    num_rows = data_arr.shape[0]
    if num_rows < 2:
        raise ValueError(f"Argument data_arr must have at least 2 rows, It actually has just got {num_rows}")

    # split data
    num_train = int(0.75 * data_arr.shape[0])
    permuted_indices = np.random.permutation(data_arr.shape[0])
    return data_arr[permuted_indices[:num_train], :], data_arr[permuted_indices[num_train:], :]


def model_test(testing, slope, intercept):
    pass
