# -*- coding: utf-8 -*-
"""
计算一个序列的样本熵：
输入：n维向量
输出：样本熵
"""
import numpy as np

def SampEn(U, m, r):
    
    N = len(U)
    
    def _maxdist(x_i, x_j):
        return max([abs(ua - va) for ua, va in zip(x_i, x_j)])
    
    def _phi(m):
        x = [[U[j] for j in range(i, i + m - 1 + 1)] for i in range(N - m + 1)]
        B = [(len([1 for x_j in x if _maxdist(x_i, x_j) <= r]) - 1.0) / (N - m) for x_i in x]
        return (N - m + 1.0)**(-1) * sum(B)
    
    return -np.log(_phi(m+1) / _phi(m))