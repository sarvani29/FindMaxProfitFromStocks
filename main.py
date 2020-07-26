import pandas as pd
import sys
from maxprofit import MaxProfit

data = pd.read_csv(sys.argv[1], error_bad_lines=False)
arr1 = data.columns[1:]
for col in arr1:
    arr = data[col].to_numpy()
    solution = MaxProfit.maxProfit(arr)
    print("The maximum profit for " + col + " is: ", solution)

