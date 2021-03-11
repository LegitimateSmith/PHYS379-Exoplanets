import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import xlwt
from tempfile import TemporaryFile


pd.set_option('display.max_columns', None)

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

TableOfData = pd.read_csv("C:/Users/smith/OneDrive/Documents/GitHub/PHYS379-Exoplanets/EP&FP_FinalColumns.csv", error_bad_lines=False)

fileParametersArray = np.load("C:/Users/smith/OneDrive/Documents/GitHub/PHYS379-Exoplanets/LR0,025_FinalColumns.npy", allow_pickle = True)
parameters = fileParametersArray.tolist()

lineOfBestFit = []
hypotheses = []
for row in range(TableOfData.shape[0]):
    sumOfxTheta = 0.0
    for column in range(len(parameters)):
        sumOfxTheta += parameters[column]*TableOfData.iloc[row, column + 1]
    lineOfBestFit.append(sumOfxTheta)
    hypotheses.append(1/(1 + np.exp(-lineOfBestFit[row])))

numberOfSucesses = 0

for row in range(TableOfData.shape[0]):
    if (hypotheses[row] >= 0.5 and TableOfData.iloc[row,0] == 1):
        numberOfSucesses += 1
    elif (hypotheses[row] < 0.5 and TableOfData.iloc[row,0] == 0):
        numberOfSucesses += 1

print(hypotheses)
print(numberOfSucesses)

book = xlwt.Workbook()
sheet1 = book.add_sheet('Hypotheses')

for i,e in enumerate(hypotheses):
    sheet1.write(i,1,e)

name = "HypothesesTracking.xls"
book.save(name)
book.save(TemporaryFile())