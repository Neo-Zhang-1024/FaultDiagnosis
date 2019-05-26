# -*- coding: utf-8 -*-
"""
计算振动信号的时域、频域衡量指标
输入：振动信号
输出：10维时域特征数组
	  2维频域特征数组
时域指标（10个）：  
	  最大值、均值、峰峰值、均方根、波形因子、峰值因子、裕度因子、脉冲因子、峭度因子、歪度因子   
频域指标（2 个）：  
	  中心频率、频率方差
时频域指标（8个）：
	  小波包能量
"""

import numpy as np
import pandas as pd
import math
from FFT import myfft
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn import preprocessing
import pywt
import pywt.data

#计算时域特征
def calc_ft(arr):
    #最大值
    a_max = np.max(arr)  
    #均值
    a_mean = np.mean(arr)  
    #峰峰值
    a_ffz = np.max(arr) - np.min(arr)  
    #均方根
    a_rms = math.sqrt(np.mean(pow(arr, 2)))
    #波形因子
    a_boxing = a_rms / (np.mean(np.abs(arr)))
    #峰值因子
    a_fengzhi = np.max(np.abs(arr)) / a_rms
    #裕度因子
    a_yudu = np.max(np.abs(arr)) / pow((np.mean(np.sqrt(np.abs(arr)))), 2)
    #峭度因子
    a_qd = np.mean(pow((np.abs(arr) - a_mean), 4))
    a_qiaodu = a_qd / pow(a_rms, 4)
    #脉冲因子
    a_mc = np.max(np.abs(arr)) / pow((np.mean(np.abs(arr))), 2)
    #歪度因子
    a_wd = np.mean(pow((np.abs(arr) - a_mean), 3))
    a_waidu = a_wd / pow(a_rms, 3)
    # 定义一个10维数组存放数据
    featuretime_list = [a_max, a_mean, a_ffz, a_rms, a_boxing, a_fengzhi, 
           a_yudu, a_qiaodu, a_mc, a_waidu]
    return featuretime_list

#计算频域特征
def calc_ff(arr):
    f, s = myfft(arr, 12000)  #进行傅里叶变换，得到频谱
    a_fc = np.mean(f * s) / np.mean(s)  #中心频率
    a_vf = np.mean(s * pow((f - a_fc), 2)) / np.mean(s)  #频率方差
    featurefrequency_list = [a_fc, a_vf]
    return featurefrequency_list

#获取时频域特征
def calc_fwpt(arr):
    a_wpt = np.zeros(8)
    wpt = pywt.WaveletPacket(arr, wavelet='db3', mode='symmetric', maxlevel=3) #小波包三层分解
    aaa = wpt['aaa'].data #第1个节点
    aad = wpt['aad'].data #第2个节点
    ada = wpt['ada'].data #第3个节点
    add = wpt['add'].data #第4个节点
    daa = wpt['daa'].data #第5个节点
    dad = wpt['dad'].data #第6个节点
    dda = wpt['dda'].data #第7个节点
    ddd = wpt['ddd'].data #第8个节点
    #求取节点的范数
    ret1 = np.linalg.norm(aaa,ord=None) #第一个节点系数求得的范数/ 矩阵元素平方和开方
    ret2 = np.linalg.norm(aad,ord=None)
    ret3 = np.linalg.norm(ada,ord=None)
    ret4 = np.linalg.norm(add,ord=None)
    ret5 = np.linalg.norm(daa,ord=None)
    ret6 = np.linalg.norm(dad,ord=None)
    ret7 = np.linalg.norm(dda,ord=None)
    ret8 = np.linalg.norm(ddd,ord=None)
    a_wpt = [ret1, ret2, ret3, ret4, ret5, ret6, ret7, ret8]
    return a_wpt






















