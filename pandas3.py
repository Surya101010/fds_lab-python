import pandas as pd
import numpy as np
dict={'first score':[100,90,np.nan,95],'second score':[30,np.nan,45,56],'third score':[53,440,80,98],'fourth score':[np.nan,np.nan,np.nan,65]}
df=pd.DataFrame(dict)
df.dropna
print(df)