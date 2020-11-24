#Write your code here
import numpy as np
import pandas as pd

heights_A = pd.Series([176.2,158.4,167.6,156.2,161.4],index = ['s1','s2','s3','s4','s5'])
weights_A = pd.Series([85.1,90.2,76.8,80.4,78.9],index = ['s1','s2','s3','s4','s5'])
df_A = pd.DataFrame({'Student_height': heights_A,'Student_weight':weights_A })
heights_B = pd.Series(np.random.normal(170.0,25,5),index = ['s1','s2','s3','s4','s5'])
weights_B = pd.Series(np.random.normal(75.0,12,5),index = ['s1','s2','s3','s4','s5'])

df_B = pd.DataFrame({'Student_height': heights_B,'Student_weight':weights_B })
print(heights_A.shape)


print(weights_A.dtype)



print(df_A.shape)

np.random.seed(100)

print(heights_B.mean())

print(df_B.columns)

p = pd.Panel({'ClassA' : df_A,
   'ClassB' : df_B})
print(p.shape)


# //df_s1s4 = df_A.loc[df_A['index'].apply(lambda x : x.endswith('1'))]
# WORKING WITH CSV FILE

df_A.to_csv('classA')

df_A2= pd.read_csv('classA')

print(df_A2)

df_A3 = pd.read_csv('classA',index_col=0)

print(df_A3)

df_B.to_csv('classB')

df_B2 = pd.read_csv('classB')

print(df_B2)

df_B3 = pd.read_csv('classB', header = None)

print(df_B3)

df_B4 = pd.read_csv('classB', header = None,skiprows = 2)

print(df_B4)

#6 DATA AGGREGATION

df_A_filter1 = df_A[df_A['Student_height'] > 160] & df_A[df_A['Student_weight'] > 80]

print(df_A_filter1)


df_A_filter2 = df_A.filter(regex='5$',axis = 0)
print(df_A_filter2)

df_A['Gender'] = ['M','F','M','M','F']
df_groups =  df_A.groupby('Gender')

print(df_groups.mean())