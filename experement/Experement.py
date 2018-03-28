import numpy as np


def standardization_pm(data):
    rec_data = np.array(data)
    for i in range(len(rec_data)):
        delta_max = max(rec_data[i])
        delta_min = min(rec_data[i])

        delta_x = (delta_max - delta_min) / 2
        center_plan = sum(rec_data[i]) / len(rec_data[i])

        rec_data[i] = (center_plan - rec_data[i]) / delta_x
    return rec_data


def create_matrix_plan(dataVar, numExp):
    numVar = len(dataVar)
    size = pow(numVar, numExp)
    plan = [[0 for x in range(numExp)] for y in range(size)]
    for idxExp in range(size):
        for i
    return plan