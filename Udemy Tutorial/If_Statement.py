import numpy as np
from numpy.random import randn

answer = None  # to get none instead of variable not defined if loop returns True
x = randn()
if x > 1:
    answer = "Greater than 1"
print(x)
print(answer)

########################################################################################################################

# ELSE LOOP

########################################################################################################################
answer = None
x = randn()
if x > 1:
    answer = "Greater than 1"
else:
    answer = "Less than 1"
print(x)
print(answer)

########################################################################################################################

# NESTED STATEMENTS

########################################################################################################################
answer = None
x = randn()
if x > 1:
    answer = "Greater than 1"
else:
    if x >= -1:
        answer = "Between -1 and 1"
    else:
        answer = "Less than -1"
print(x)
print(answer)

########################################################################################################################

# CHAINED STATEMENTS

########################################################################################################################
answer = None
x = randn()
if x > 1:
    answer = "Greater than 1"
elif x >= -1:
    answer = "Between -1 and 1"
else:
    answer = "Less than -1"
print(x)
print(answer)
