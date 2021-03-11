import numpy as np
import matplotlib.pyplot as plt
import xlwt
from tempfile import TemporaryFile

fileCostTrackerArray = np.load("C:/Users/smith/OneDrive/Documents/GitHub/PHYS379-Exoplanets/LR0,025_Cost_FinalColumns.npy", allow_pickle = True)
costTracker = fileCostTrackerArray.tolist()

print(costTracker)


book = xlwt.Workbook()
sheet1 = book.add_sheet('Costs')

for i,e in enumerate(costTracker):
    sheet1.write(i,1,e)

name = "CostTracking.xls"
book.save(name)
book.save(TemporaryFile())

plt.plot(costTracker, "ro")
plt.show()