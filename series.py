import numpy as np 
import pandas as pd 
data = pd.Series([0.25, 0.5, 0.75, 1.0]) 
print(data) 
print(data.values) 
print(data.index) 
print(data[1]) 
print(data[1:3]) 
#series as numpy array 
data = pd.Series([0.25, 0.5, 0.75, 1.0],index=['a', 'b', 'c', 'd']) 
print(data) 
print(data['b']) 
data = pd.Series([0.25, 0.5, 0.75, 1.0],index=[2, 5, 3, 7]) 
print(data) 
print(data[5]) 
#series as specilized dictionary 
population_dict = {'California': 38332521, 
 'Texas': 26448193, 
 'New York': 19651127, 
 'Florida': 19552860, 
 'Illinois': 12882135} 
population = pd.Series(population_dict) 
print(population) 
print(population['California']) 
print(population['California':'Florida']) 
#constructing series objects 
a=pd.Series([2, 4, 6]) 
print(a) 
b=pd.Series(5, index=[100, 200, 300]) 
print(b) 
c=pd.Series({2:'a', 1:'b', 3:'c'}) 
print(c); 
#after indexing 
c=pd.Series({2:'a', 1:'b', 3:'c'}, index=[3, 2]) 
print(c) 