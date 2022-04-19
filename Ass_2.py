""" NAME: Srishu Chintakindi
ID: 20CE012
GitHub repositary link: https://github.com/srishu272/Python_Programming
Write a procedure to find min, max, mean, standard deviation, variance of number list.
Example
Input: 10 50 80 70 49 23 11 4
output: 4 80 37.13 27.25 848.70"""

import numpy as np
arr = list(map(int, input().split(' ')))

minimum = min(arr)
maximum = max(arr)
mean = np.mean(arr)
Variance = float(np.var(arr))
Standard_Deviation = float(np.std(arr))

print(minimum, maximum, mean, '{:.2f}'.format(Variance), '{:.2f}'.format(Standard_Deviation))