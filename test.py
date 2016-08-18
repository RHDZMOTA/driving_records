
'''
Python script just to test ideas... (mostly learning)
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

print(data)
plt.plot(data.t0,data.tf)
print('All right!')