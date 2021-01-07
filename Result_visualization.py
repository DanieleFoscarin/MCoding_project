# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 01:52:40 2021

@author: fosca
"""



import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.io


D = scipy.io.loadmat('D_record.mat')
# print(D)
D = D["D_record"]
D = np.asarray(D)
print(" shape ", np.shape(D))

D_std = np.std(D[:,:,:], 1)
D_mean = np.mean(D[:,:,:,] ,1)
print(np.shape(D_mean))
print(D_std)

# fig, ax = plt.subplots(1,1)
# ax.errorbar(range(4), D_mean[1,:], D_std[1,:], ls= 'none', color = 'red')
# ax.bar(range(4), D_mean[1,:])


# Res = [[0.0015235, 0.0013127, 0.0008924, 0.0018855],
#        [0.0030751, 0.0024397, 0.0031538, 0.012074],
#        [0.0038377, 0.0033012, 0.0023745, 0.0050617],
#        [0.0079957, 0.005072, 0.0049455, 0.0050373],
#        [0.0024103, 0.0054019, 0.0065141, 0.0075302],
#        [0.00079332, 0.00052396, 0.00057959, 0.0027143],
#        [0.0036438, 0.0042442, 0.0035754, 0.0053274],
#        [0.0015776, 0.0018484, 0.0037697, 0.0046214]]

Res = np.asarray(Res)
labels_d = ['RandReg', 'StdNorm', 'StdScaled', 'jpeg50']
labels_i = ['Lena', 'baboon', 'peppers1', 'gradient', 'peppers2', 'autumn', 'lighthouse', 'pears']
path = 'C:\\Users\\fosca\\Documents\\UNIPD\\Magistrale_ICT\\Multimedia_Coding\\overleaf_images\\bar_charts\\'

for i in range(8):
    fig, ax = plt.subplots(1,1)
    ax.errorbar(range(4), D_mean[i,:], D_std[i,:], capsize=10, ls = ':', elinewidth=5)
    ax.scatter(range(4), D_mean[i,:], s=100)
    # ax.bar(range(4), D_mean[i,:])
    ax.set_xticks(range(4))
    ax.set_xticklabels(labels_d)
    # ax.set_ylabel("distortion")
    ax.set_title(labels_i[i])
    fig.savefig(path +labels_i[i]+'_bar.pdf')
    # ax[i].set_title(lab)