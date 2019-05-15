"""
Jump license is too expansive so we decide to write a python function.
"""

import os
os.system('cls')
#def cls():
#    os.system('cls' if os.name == 'nt' else 'cls')
#cls()

#def datareader():

import re, statistics 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename
import scipy.stats as stats
import seaborn as sns

#sets working directory and file to extract data
filename = askopenfilename()

#creates a list of dataframes for specimen info from the first 6 lines        
fileData = pd.read_excel(filename)

#filter rows for key tests in fileData

ashData = fileData[(fileData['ICHAR'])=='ASH']
x = ashData.iloc[1: , 6]
y = ashData.iloc[1: , -4].astype(float)

usl=32
lsl=28

meanValue = statistics.mean(y.dropna()) #y.dropna can remove na in the list
stdValue = statistics.stdev(y.dropna())
Cp = float(usl-lsl)/(6*stdValue)
Cpu = float(usl - meanValue)/(3*stdValue)
Cpl = float(meanValue - lsl)/(3*stdValue)
Cpk = min([Cpu, Cpl])

plt.figure(figsize=(20,10))
plt.plot(x,y, 'o', label = 'Ash Content')
plt.axhline(y=meanValue, color='b', linestyle='-', label = 'Mean Value')


plt.axhline(y=usl, color='r', linestyle='-', label = 'Up Limit')
plt.axhline(y=lsl, color='g', linestyle='-', label = 'Bottom Limit')

plt.xlabel('Date')
plt.ylabel('Ash [%]')
plt.title('Ash Content')

plt.legend(loc='best')
plt.savefig('Ash Content')
plt.show()

plt.figure(figsize=(20,10))

ySort = y.dropna().sort_values(ascending=True)
weights = np.ones_like(ySort)/float(len(ySort))
plt.hist(ySort, color = 'blue', edgecolor = 'black', weights=weights)

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
plt.plot(x, stats.norm.pdf(x, meanValue, stdValue)/5)

plt.xlabel('Ash [%]')
plt.ylabel('%')
plt.title('Ash Content Histrogram')
plt.show()

#Consider Batch Processing using glob

#Case Insensitive Search
#isKeyword = re.search('ash',str(fileData['ICHAR']), re.IGNORECASE)

#Display mean value and standard deviation on top of the figure

#Legend Better Location; Better Font

