import pandas as pd
df=pd.read_csv(r"C:\Users\asifh\OneDrive\Desktop\Data Sets\heart.csv")
#print(df)

#1.total no.of missing value

#print(df.isna().sum())

#-------------------------------------------

#2.each target column count

# df1=df.groupby('target') ['target'].count()
# print(df1)

#---------------------------------------------

# 3. separtae x and y

# x=df.iloc[:,:-1]
# #print(x)
# #
# y=df.iloc[:,-1]
# print(y)

#---------------------------------------------------
 #4 .fill the missing value using proper method

#trestbps , restecg ,thalach ,ca   ,thal

#print(df.dtypes)
#print(df['trestbps']).unique()

# x=df['trestbps'].mean()
# df['trestbps'].fillna(x,inplace=True)
# #print(df)
#

# df1=df['restecg'].unique()
# print(df1)

# y=df['restecg'].mode()[0]
# df['restecg'].fillna(y,inplace=True)
# # print(df)
# # print(df.isna().sum())
#
# q=df['thalach'].mean()
# df['thalach'].fillna(q,inplace=True)
# # print(df)
# # print(df.isna().sum())
#
# z=df['ca'].mode()[0]
# df['ca'].fillna(z,inplace=True)
# # print(df)
# # print(df.isna().sum())
#
# s=df['thal'].mode()[0]
# df['thal'].fillna(s,inplace=True)
# print(df)
# print(df.isna().sum())

#-------------------------------------------------------

#trestbps column value 180 wrong data (mean)

# x=df['trestbps'].mean()
# for i in df.index:
#     if df.loc[i,'trestbps']>180:
#         df.loc[i,'trestbps']= x
# print(df)
