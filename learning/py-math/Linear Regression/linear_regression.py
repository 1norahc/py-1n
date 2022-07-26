import numpy as np
import matplotlib.pyplot as plt



def test_values(sample_range: int, dfY=True):
    _dfY = []
    _ = 0.1
    for i in range(0, sample_range-1):
        _+=0.1
        _dfY.append(_)
    #_dfY[-1] = 1.0
    random_sample = [np.random.random_sample(2) for _ in range(0, sample_range-1)]
    if dfY != True:
        X, Y = [v[0] for v in random_sample], [v[1] for v in random_sample]
    else:
        X, Y = [v[0] for v in random_sample], _dfY
    return X, Y

print(test_values(10))
