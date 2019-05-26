# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 21:42:29 2019
特征的升维提取：
输入：原始振动信号的n*1200.csv文件, n为样本个数，k为模态数
输出：n*20k.csv文件
@author: Neo
"""

import numpy as np
import pandas as pd
from VMD import vmd
from featureCalc import calc_ff
from featureCalc import calc_ft
from featureCalc import calc_fwpt

def signal_feature(path, n, k):
    data = pd.read_csv(path, header=None)  #读取数据
    #设置vmd的参数
    alpha = 2000       # moderate bandwidth constraint
    tau = 0.3            # noise-tolerance (no strict fidelity enforcement)
    K = k             # 4 modes
    DC = 0             # no DC part imposed
    init = 1          # initialize omegas uniformly
    tol = 1e-7

    #循环进行vmd分解
    U = np.zeros((n, K, 1200))  #定义一个空数组
    for i in range(n):
        f = data.loc[i].values
        u, u_hat, omega = vmd(f, alpha, tau, K, DC, init, tol)  # u是分解后的信号
        U[i, :, :] = u
    #print(U.shape)

    #循环进行求时域、频域特征，并保存在一个（100* 20K）数组里面
    feature = np.zeros((n, K * 20))
    for i in range(n):
        for j in range(K):
            feature[i, j*20:(j*20+10)] = calc_ft(U[i, j, :])
            feature[i, (j*20+10):(j*20+12)] = calc_ff(U[i, j, :])
            feature[i, (j*20+12):(j*20+20)] = calc_fwpt(U[i, j, :])
    #print(feature.shape)
    #转换成pandas的DataFrame格式、导出文件
    df = pd.DataFrame(feature)
    df.to_csv(path[:-4]+'4080.csv', header=False, index=False)
    return U.shape, feature.shape

    










