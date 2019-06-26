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
import math
from tkinter import *
from tkinter import ttk

#sets working directory and file to extract data
filename = askopenfilename()

#creates a list of dataframes for specimen info from the first 6 lines        
fileData = pd.read_excel(filename)

#filter rows for key tests in fileData
listProperty=sorted(list(set(fileData['OMSCH'])))
listInfo = list(fileData.columns.values)
         
#class Checkbar(Frame):
#    
#    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
#        Frame.__init__(self, parent)
#        self.vars = []
#        
#        for pick in picks:
#            var = IntVar()
#            chk = Checkbutton(self, text=pick, variable=var, anchor=W)
#            chk.pack(fill=BOTH, expand=YES)
#            self.vars.append(var)
#            
#    def state(self):
#        return map((lambda var: var.get()), self.vars)
#        
#    root = Tk()
#    root.title("Select the property you want to display")
#    root.minsize(300,300)
#    checkBoxBar = Checkbar(root, listProperty[0:10])
#    checkBoxBar.pack()
#    checkBoxBar.config(relief=GROOVE, bd=2)
#    
#    def allstates(): 
#        print(checkBoxBar.state())
#    
#    Button(root, text='Confirm', command=state).pack()
#    
#root.mainloop()

selectProperty = ['Ash Content', 'Density']
#selectProperty = ['Ash Content', 'Density','Copper Content (Heat stabilizer)','Charpy Impact','Dtul @ 1.8 mpa']

for property in selectProperty:
    propertyData = fileData[(fileData['OMSCH'])==property]
    x = propertyData['DATE'] # Extract date information
    y = propertyData['MIDWR'].astype(float) #Extract measured values w/ float 

    usl=propertyData['TOLOB'].iloc[1].astype(float) #Define upper limit
    lsl=propertyData['TOLUN'].iloc[1].astype(float) #Define lower limit
    
    meanValue = statistics.mean(y.dropna()) #y.dropna can remove na in the list; Calculate mean
    stdValue = statistics.stdev(y.dropna()) #Calculate standard deviation
    Cp = float(usl-lsl)/(6*stdValue)        #Calculate Cp, Cpu, Cpl, Cpk
    Cpu = float(usl - meanValue)/(3*stdValue)
    Cpl = float(meanValue - lsl)/(3*stdValue)
    Cpk = min([Cpu, Cpl])
    
    plt.figure(figsize=(20,10)) #Define figure size
    plt.plot(x,y, 'o', label = str(property)) #Plot data using dot w/ auto label
    plt.axhline(y=meanValue, color='b', linestyle='-', label = 'Mean Value')
    
    if usl is not None and lsl is not None:
        plt.axhline(y=usl, color='r', linestyle='-', label = 'Up Limit') #Up limit
        plt.axhline(y=lsl, color='g', linestyle='-', label = 'Bottom Limit') #Bottom limit
    
    plt.xlabel('Date', fontsize=24) 
    plt.ylabel(str(property)+' '+str(propertyData['UNIT'].iloc[1]),fontsize=24) #Auto ylabel
    plt.title(str(property), fontsize=24) #Auto Title
    
    t=str('mean = ')+str("%.2f" % meanValue)+'\n' + \
      str('Stdev = ')+ str("%.2f" % stdValue)
    plt.text(x.sort_values(ascending=True).iloc[round(x.size*0.1+0.5)], 
             lsl+(usl-lsl)*0.8, t, fontsize=24)
    plt.rcParams.update({'font.size': 14})
    
    plt.savefig(str(property))
    plt.show()
    
    # The histogram still has huge problem, I'll fix this later
#    plt.figure(figsize=(20,10))
#    
#    ySort = y.dropna().sort_values(ascending=True)
#    weights = np.ones_like(ySort)/float(len(ySort))
#    plt.hist(ySort, color = 'blue', edgecolor = 'black', weights=weights)
#    
#    xmin, xmax = plt.xlim()
#    xinHis = np.linspace(xmin, xmax, 100)
#    plt.plot(xinHis, stats.norm.pdf(xinHis, meanValue, stdValue)/5)
#    
#    plt.xlabel(str(property)+' '+str(propertyData['UNIT'].iloc[1]))
#    plt.ylabel('%')
#    plt.title(str(property)+' Histogram', fontsize=24)
#    
#    #plt.savefig(str(property)+' Histogram')
#    plt.show()

#Consider Batch Processing using glob

#Case Insensitive Search
#isKeyword = re.search('ash',str(fileData['ICHAR']), re.IGNORECASE)


#Legend Better Location; Better Font

