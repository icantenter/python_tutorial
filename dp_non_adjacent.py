import numpy as np
#选择不相邻的数使得和最大
arr = []

def rec_opt(arr, i):
    if i == 0:
        return arr[0]
    elif i == 1:
        return max(arr[0], arr[1])
    else:
        A = rec_opt(arr, i - 2) + arr[i]
        B = rec_opt(arr, i - 1)
        return max(A, B)

def dp_opt(arr):
    if len(arr) <= 0:
        return -1
    opt = np.zeros(len(arr))
    opt[0] = arr[0]
    if len(arr) >= 2:
        opt[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        A = opt[i - 2] + arr[i]
        B = opt[i - 1]
        opt[i] = max(A, B)
    return opt[len(arr) - 1]

print(dp_opt(arr))
