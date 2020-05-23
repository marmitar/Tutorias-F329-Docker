from scipy import odr
import numpy as np

x = np.arange(15)
a, b = odr.ODR(odr.Data(x, x), odr.models.unilinear).run().beta

assert abs(a - 1) < 0.01
assert abs(b) < 0.01

import pandas
import xlrd

df = pandas.read_excel('data.xlsx')
df.to_csv('data.csv')
