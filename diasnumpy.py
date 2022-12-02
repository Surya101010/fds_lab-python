import numpy as np
x2=np.random.randint(10,size=(3,4))
x2_sub=x2[:2,:2]
print(x2_sub)
x2_sub[0,0]=99
print(x2_sub)
print(x2)