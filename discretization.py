import pandas as pd
import numpy as np
from scipy.stats import iqr
import math
from sklearn.utils import shuffle

"""
实现Number of bins and width 的代码
https://en.wikipedia.org/wiki/Histogram#Number_of_bins_and_width
"""
np.set_printoptions(precision=4)


def squareRootChoice(data, features):
    length, width = data.shape[0], data.shape[1]
    bins = math.ceil(math.sqrt(length))
    dataNew = data
    print('squareRootChoice bins=', bins)
    for item in features:
        # print(pd.cut(data[item],bins=bins,labels=False))
        tmp = pd.cut(data[item], bins=bins, labels=False)
        dataNew[item] = tmp
    return dataNew


def SturgesFormula(data, features):
    length, width = data.shape[0], data.shape[1]
    bins = math.ceil(math.log2(length) + 1)
    dataNew = data
    print('SturgesFormula bins=', bins)
    for item in features:
        # print(pd.cut(data[item],bins=bins,labels=False))
        tmp = pd.cut(data[item], bins=bins, labels=False)
        dataNew[item] = tmp
    return dataNew


def RiceRule(data, features):
    length, width = data.shape[0], data.shape[1]
    bins = math.ceil(2 * math.pow(length, 1 / 3))
    dataNew = data
    print('RiceRule bins=', bins)
    for item in features:
        # print(pd.cut(data[item],bins=bins,labels=False))
        tmp = pd.cut(data[item], bins=bins, labels=False)
        dataNew[item] = tmp
    return dataNew


def DoaneFormula(data, features):
    length, width = data.shape[0], data.shape[1]
    dataNew = data
    eg1 = math.sqrt(6 * (length - 2) / ((length + 1) * (length + 3)))
    for item in features:
        bins = int(1 + math.log2(length) + math.log2(abs(1 + (data[item].skew()) / eg1)))
        # print('DoaneFormula bins=', bins)
        tmp = pd.cut(data[item], bins=bins, labels=False)
        dataNew[item] = tmp
    return dataNew


def ScottNormalReferenceRule(data, features):
    length, width = data.shape[0], data.shape[1]
    dataNew = data
    for item in features:
        # 分子与分母的计算
        molecule, denominator = 3.5 * np.std(data[item]), math.pow(length, 1 / 3)
        widthNew = molecule / denominator
        bins = math.ceil((data[item].max() - data[item].min()) / widthNew)
        # print('cottNormalReferenceRule bins=', bins)
        tmp = pd.cut(data[item], bins=bins, labels=False)
        dataNew[item] = tmp
    return dataNew


def FreedmanDiaconisChoice(data, features):
    length, width = data.shape[0], data.shape[1]
    dataNew = data
    for item in features:
        # 分子与分母的计算
        molecule, denominator = 2 * iqr(data[item]), math.pow(length, 1 / 3)
        widthNew = molecule / denominator
        if molecule == 0:
            raise ZeroDivisionError("iqr() value =0, please check data!")
        # # print(item, iqr(data[item]), denominator, widthNew)
        bins = math.ceil((data[item].max() - data[item].min()) / widthNew)
        tmp = pd.cut(data[item], bins=bins, labels=False)
        dataNew[item] = tmp
    return dataNew
