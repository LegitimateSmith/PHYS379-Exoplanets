import copy
import sys
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import random

fileParametersArray = np.load("C:/Users/smith/OneDrive/Documents/GitHub/PHYS379-Exoplanets/LR0,025.npy", allow_pickle = True)
parameters = fileParametersArray.tolist()

pd.set_option('display.max_columns', None)

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

dataFrame = pd.read_csv("C:/Users/smith/OneDrive/Documents/GitHub/PHYS379-Exoplanets/ExoplanetsTestDataset.csv", error_bad_lines=False)


lineOfBestFit = []
hypotheses = []
for row in range(dataFrame.shape[0]):
    sumOfxTheta = 0.0
    for column in range(len(parameters)):
        sumOfxTheta += parameters[column]*dataFrame.iloc[row, column + 1]
    lineOfBestFit.append(sumOfxTheta)
    hypotheses.append(1/(1 + np.exp(-lineOfBestFit[row])))

successRate = 0

for i in range(len(hypotheses)):
        if (hypotheses[i] >= 0.5 and dataFrame.iloc[i,0] == 1):
            successRate += 1
        elif (hypotheses[i] < 0.5 and dataFrame.iloc[i,0] == 0):
            successRate += 1


print((successRate/dataFrame.shape[0])*100, "%")