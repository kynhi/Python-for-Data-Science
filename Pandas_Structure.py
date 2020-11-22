#Write your code here
import numpy as np
import pandas as pd

heights_A = pd.Series([176.2,158.4,167.6,156.2,161.4],index = ['s1','s2','s3','s4','s5'])

print(heights_A.shape)
weights_A = pd.Series([85.1,90.2,76.8,80.4,78.9],index = ['s1','s2','s3','s4','s5'])

print(weights_A.dtype)

df_A = pd.DataFrame({'Student_height': heights_A,'Student_weight':weights_A })

print(df_A.shape)

np.random.seed(100)
heights_B = pd.Series(np.random.normal(170.0,25,5),index = ['s1','s2','s3','s4','s5'])
weights_B = pd.Series(np.random.normal(75.0,12,5),index = ['s1','s2','s3','s4','s5'])
print(heights_B.mean())

df_B = pd.DataFrame({'Student_height': heights_B,'Student_weight':weights_B })
print(df_B.columns)

p = pd.Panel({'ClassA' : df_A,
   'ClassB' : df_B})
print(p.shape)