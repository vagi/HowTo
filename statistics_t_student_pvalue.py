# Student-distribution
# We have a sample with 15 observations, t-test of H_0 (hypothesis0) shows:
# m = 10 and t = -2, so p-value can be calculated as follow:

import numpy as np
from scipy import stats

n = 15
tt = -2

p_value = stats.t.sf(np.abs(tt), n-1) * 2
print("Two-sided p-value:{}".format(round(p_value, 5)))
