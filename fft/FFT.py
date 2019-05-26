# -*- coding: utf-8 -*-
"""
对时域信号进行傅里叶变换，得到频谱
输入：时域信号
输出：频率数组
	  振幅数组
"""

import numpy as np

def myfft(signal, s_rate):
    s_length = len(signal)
    freqs = np.linspace(0, s_rate/2, s_length/2+1)
    xf = np.fft.rfft(signal) / s_length
    xfp = np.abs(xf) * 2
    return freqs, xfp

    
