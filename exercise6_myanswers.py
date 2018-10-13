# below are some simple ways you could solve these problems
# remember that there are MANY MANY ways to solve the same problem

###################################################################
#imports section
import pandas as pd
import numpy as np

######################## Problem 1 ########################
#return first n lines like head (0.5 pts)
file_name='iris.csv'
num_lines = 5
data=pd.read_csv(file_name,header=0,sep=",")
data.iloc[:num_lines,]
#or as a function
def print_lines(filename, n):
    data=pd.read_csv(filename, header=0, sep=',')
    print data.iloc[:n,]

print_lines('iris.csv', 5)
#compare to data1.head(), they should look the same
data1.head()

######################## Problem 2 ########################
#read in the data
data1=pd.read_csv('iris.csv',header=0,sep=",")

### Part A (0.5 pts)
#print last two rows in the last 2 columns
#three different ways
data1.iloc[-2:,-2:]
data1.iloc[148:,3:]
data1.iloc[148:150,3:5]

### Part B (0.5 pts)
#number of observations for each species
#can do separately
len(data1[data1.Species=='setosa'])
len(data1[data1.Species=='versicolor'])
len(data1[data1.Species=='virginica'])
#if we want to orient the output
print "Number of setosa obs:", len(data1[data1.Species=='setosa']) #same for others
#or can do all together
data1['Species'].value_counts()

### Part C (0.5 pts)
#get rows with Sepal.Width > 3.5
data1[data1['Sepal.Width'] > 3.5]

### Part D (0.5 pts)
#write data for species setosa to csv
setosa_data = data1[data1.Species=='setosa']
setosa_data.to_csv('setosa_file.csv')

### Part E (0.5 pts)
#calc mean, min, max of Petal.Length from virginica
#first got all rows for the species
pl_vir = data1[data1.Species=='virginica']
np.mean(pl_vir['Petal.Length'])
min(pl_vir['Petal.Length'])
max(pl_vir['Petal.Length'])
#or
pl_vir['Petal.Length'].mean()
pl_vir['Petal.Length'].min()
pl_vir['Petal.Length'].max()
#another print example
print "Mean petal length for virginica:", pl_vir['Petal.Length'].mean()
