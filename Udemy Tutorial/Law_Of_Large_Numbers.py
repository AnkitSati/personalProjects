import numpy as np
from numpy.random import randn


N = 10000000
counter = 0
for i in randn(N):
    if -1 < i < 1:
        counter = counter+1
answer = counter / N
print(answer)