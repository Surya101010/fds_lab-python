import pandas as pd
data={'name':['jai','prince','gaurav','anuj'],'age':[27,24,22,32],'address':['delhi','kanpur','allahabad','kannaj'],'qualification':['msc','ma','mca','phd']}
df=pd.DataFrame(data)
print(df)
print(df[['name','qualification']])