import numpy as np


def calculate(list):

    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    new_arr = np.array(list)
    grid = new_arr.reshape(3, 3)

    calculations = {}

    # calculate the mean
    cols_mean = grid.mean(axis=0)
    rows_mean = grid.mean(axis=1)
    total_mean = grid.mean()
    solution_mean = [cols_mean.tolist(), rows_mean.tolist(), total_mean]
    calculations['mean'] = solution_mean

    # calculate the variance
    cols_variance = grid.var(axis=0)
    rows_variance = grid.var(axis=1)
    total_variance = grid.var()
    solution_variance = [cols_variance.tolist(
    ), rows_variance.tolist(), total_variance]
    calculations['variance'] = solution_variance

    # calculate the standard deviation
    cols_std = grid.std(axis=0)
    rows_std = grid.std(axis=1)
    total_std = grid.std()
    solution_std = [cols_std.tolist(), rows_std.tolist(), total_std]
    calculations['standard deviation'] = solution_std

    # calculate the max
    cols_max = grid.max(axis=0)
    rows_max = grid.max(axis=1)
    total_max = grid.max()
    solution_max = [cols_max.tolist(), rows_max.tolist(), total_max]
    calculations['max'] = solution_max

    # calculate the min
    cols_min = grid.min(axis=0)
    rows_min = grid.min(axis=1)
    total_min = grid.min()
    solution_min = [cols_min.tolist(), rows_min.tolist(), total_min]
    calculations['min'] = solution_min

    # calculate the sum
    cols_sum = grid.sum(axis=0)
    rows_sum = grid.sum(axis=1)
    total_sum = grid.sum()
    solution_sum = [cols_sum.tolist(), rows_sum.tolist(), total_sum]
    calculations['sum'] = solution_sum

    return calculations
