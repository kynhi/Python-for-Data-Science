#Write your code here
import numpy as np
import pandas as pd

heights_A = pd.Series([176.2,158.4,167.6,156.2,161.4],index = ['s1','s2','s3','s4','s5'])
weights_A = pd.Series([85.1,90.2,76.8,80.4,78.9],index = ['s1','s2','s3','s4','s5'])
df_A = pd.DataFrame({'Student_height': heights_A,'Student_weight':weights_A })
<<<<<<< HEAD
np.random.seed(100)
heights_B = pd.Series(np.random.normal(170.0,25,5),index = ['s1','s2','s3','s4','s5'])
weights_B = pd.Series(np.random.normal(75.0,12,5),index = ['s1','s2','s3','s4','s5'])
df_B = pd.DataFrame({'Student_height': heights_B,'Student_weight':weights_B })
=======
heights_B = pd.Series(np.random.normal(170.0,25,5),index = ['s1','s2','s3','s4','s5'])
weights_B = pd.Series(np.random.normal(75.0,12,5),index = ['s1','s2','s3','s4','s5'])
>>>>>>> 7a2f312bb4d13308db186864b80a9cc3e09c7890

df_B = pd.DataFrame({'Student_height': heights_B,'Student_weight':weights_B })
print(heights_A.shape)
<<<<<<< HEAD
=======

>>>>>>> 7a2f312bb4d13308db186864b80a9cc3e09c7890

print(weights_A.dtype)



print(df_A.shape)

<<<<<<< HEAD

=======
np.random.seed(100)
>>>>>>> 7a2f312bb4d13308db186864b80a9cc3e09c7890

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

<<<<<<< HEAD
#4 INDEXING DATAFRAMES
dates = pd.date_range('01-09-2017','15-09-2017')

print(dates[2])

datelist = ['14-Sep-2017','9-Sep-2017']
dates_to_be_search = pd.to_datetime(datelist)

print(dates_to_be_search)

print(dates_to_be_search.isin(dates))

arraylist = [['classA']*5 + ['classB']*5,['s1','s2','s3','s4','s5']*2]

mi_index = pd.MultiIndex.from_arrays(arraylist)

print(mi_index.levels)

#5 DATA CLEANING

df_A.loc['s3'] = np.nan

df_A.loc['s5'].Student_weight = np.nan

df_A2 = df_A.dropna()

print(df_A2)

=======
>>>>>>> 7a2f312bb4d13308db186864b80a9cc3e09c7890
#6 DATA AGGREGATION

df_A_filter1 = df_A[df_A['Student_height'] > 160] & df_A[df_A['Student_weight'] > 80]

print(df_A_filter1)


df_A_filter2 = df_A.filter(regex='5$',axis = 0)
print(df_A_filter2)

df_A['Gender'] = ['M','F','M','M','F']
df_groups =  df_A.groupby('Gender')

<<<<<<< HEAD
print(df_groups.mean())

#DATA MERGING 1

df_A['Gender'] = ['M','F','M','M','F']

s = pd.Series([165.4,82.7,'F'],index = ['Student_height','Student_weight','Gender'])
s.name = 's6'

df_AA = df_A.append(s)

print(df_AA)
df_B.index = ['s7','s8','s9','s10','s11']
#df_B = df_B.rename( index= {'s1' : 's7','s2':'s8','s3':'s9','s4':'s10','s5':'s11'})

df_B['Gender'] = ['F','M','F','F','M']

df = pd.concat([df_AA,df_B])

print(df)

#DATA MERGING 2
nameid = pd.Series(range(101,111))
name = pd.Series(['person' + str(i) for i in range(1,11)])

master = pd.DataFrame({'nameid':nameid,'name':name})
print(master)
transaction = pd.DataFrame({'nameid':[108,108,108,103],'product':['iPhone','Nokia','Micromax','Vivo']})
print(transaction)
mdf = master.merge(transaction,on = 'nameid',how= 'inner')

print(mdf)
=======
print(df_groups.mean())
>>>>>>> 7a2f312bb4d13308db186864b80a9cc3e09c7890
