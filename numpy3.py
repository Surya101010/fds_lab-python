from array import array
import numpy as np
a=np.array([[1,2,3],[3,4,5],[4,5,6]])
print("our array is :")
print(a)
print("the item in the second column are:")
print(a[...,1])
print('\n')
print("the item in the second row are:")
print(a[1,...])