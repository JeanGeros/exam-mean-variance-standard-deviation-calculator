import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
        
    matriz = np.array(list).reshape(3, 3)
    print(matriz)
    mean_value = [(matriz.mean(axis=0).tolist()), (matriz.mean(axis=1).tolist()),
            (matriz.flatten().mean())]

    variance_value = [(matriz.var(axis=0).tolist()), (matriz.var(axis=1).tolist()),
            (matriz.flatten().var())]

    standard_deviation_value = [(matriz.std(axis=0).tolist()), (matriz.std(axis=1).tolist()),
            (matriz.flatten().std())]

    max_value = [(matriz.max(axis=0).tolist()), (matriz.max(axis=1).tolist()),
            (matriz.flatten().max())]

    min_value = [(matriz.min(axis=0).tolist()), (matriz.min(axis=1).tolist()),
            (matriz.flatten().min())]

    sum_value = [(matriz.sum(axis=0).tolist()), (matriz.sum(axis=1).tolist()),
            (matriz.flatten().sum())]

    calculations = {'mean': mean_value, 
                    'variance': variance_value, 
                    'standard deviation': standard_deviation_value, 
                    'max': max_value,
                    'min': min_value,
                    'sum': sum_value, }
    print(calculations)

    return calculations