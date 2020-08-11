import numpy as np
# 选择多个数组成一个数


def rec_subset(arr, i, surplus):
    if surplus == 0:
        return True
    elif i == 0:
        return arr[i] == surplus
    elif arr[i] > surplus:
        return rec_subset(arr, i - 1, surplus)
    else:
        A = rec_subset(arr, i - 1, surplus - arr[i])
        B = rec_subset(arr, i - 1, surplus)
        return A or B


def dp_subset(arr, surplus):
    subset = np.zeros((len(arr), surplus + 1), dtype=bool)
    subset[0, :] = False
    subset[:, 0] = True
    """第一列都为True, 第一行除了arr[0]和第一列得部分,都为False"""
    if arr[0] <= surplus:
        subset[0, arr[0]] = True
    for i in range(1, len(arr)):
        for j in range(1, surplus + 1):
            if arr[i] > j:
                subset[i, j] = subset[i - 1, j]
            else:
                A = subset[i - 1, j - arr[i]] #选择当前这个数
                B = subset[i - 1, j]          #不选这个数
                subset[i, j] = A or B
    r, c = subset.shape
    return subset[r - 1, c -1]