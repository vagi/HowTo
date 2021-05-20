# Multiple comparisons in ANOVA

import scipy.stats as stats
from matplotlib import pyplot
import itertools
import numpy as np

M = 0
D = 1


def ttest(a, b):
    se = np.sqrt(a['SD'] ** 2 / a['N'] + b['SD'] ** 2 / b['N'])
    t = (a['Mx'] - b['Mx']) / se
    dfreedom = a['N'] + b['N'] - 2
    return stats.t.sf(np.abs(t), dfreedom) * 2


# n - number of elements in a sample
# m - number of samples
# a -  probability

def false_alarm(m, n, a):
    trys = 1000  # number of experiments
    hist = {'Yes': 0, 'No': 0}  # outcome of comparison
    data = list(range(m))  # initialization of groups with samples

    # Initializing experiments
    for i in range(trys):

        # Filling in m-samples and grouping them by SD, Mx, N
        for j in range(m):
            dt = stats.norm.rvs(loc=M, scale=D, size=n)
            data[j] = {'SD': np.std(dt, ddof=1), 'Mx': np.mean(dt), 'N': n}

        # Comparing samples by 2 groups - two cycles or use itertools
        for first, second in itertools.combinations(data, 2):
            if ttest(first, second) <= a:
                hist['Yes'] += 1
                break
        else:
            hist['No'] += 1

    # Plotting hystogramm of frequency
    barlist = pyplot.bar(hist.keys(), hist.values(), color='b')
    barlist[0].set_color('r')
    pyplot.title(round(hist['Yes'] / trys, 3))
    pyplot.ylabel('quantity')
    pyplot.show()


false_alarm(2, 30, 0.05)
