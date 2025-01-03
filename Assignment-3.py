import pandas as pd
df=pd.read_csv(r"C:\Users\asifh\OneDrive\Desktop\Data Sets\movies_cleaned_pandas.csv",header=None)
df.columns=('id','movie','year','rating','duration')
print(df)

#------------------------------------------------------

##  1. Find row count
#print(df.shape)

#-----------------------------------------------------

#2. Remove duplicates and find row count
#
# df1=df.drop_duplicates()
# print(df1)
# print(df.shape)

#---------------------------------------------------------

#3. Sort data set by release year in des order

# df1=df.sort_values(by='year',ascending=False).head(1)
# print(df1)

#------------------------------------------------------

#4. Find rating mxm 5 movies name,year,rating

# df1=df.sort_values(by='rating',ascending=False) [['movie','year','rating']].head(5)
# print(df1)

#--------------------------------------------------------------
#5. Find rating minimum 3 movies name,year,rating

# df1=df.sort_values(by='rating') [['movie','year','rating']].head(3)
# print(df1)

#----------------------------------------------------------
#6. Find Each year release movie count [count desc order]

# df1=df.groupby('year') ['movie'].count().sort_values(ascending=False)
# print(df1)

#-----------------------------------------------------------

#7. Each rating count [count desc order]

# df1=df.groupby('rating')['rating'].count().sort_values(ascending=False)
# print(df1)

#---------------------------------------------------------------

# 8. 2008 and rating above 3 [collect]
# A. row count

# df1=df.loc[(df['year']==2008) & (df['rating']>3)] [['rating']]
# print(df1.shape)

#---------------------------------------------------------------

# 9. Find duration mxm 1 movies name,year,rating,duration

# df1=df.sort_values(by='duration',ascending=False) [['movie','year','rating','duration']].head(1)
# print(df1)

#----------------------------------------------------------------

#10. Find rating mnm 1 movies name,year,rating,duration

# df1=df.sort_values(by='rating') [['movie','year','rating','duration']].head(1)
# print(df1)

#--------------------------------------------------------------

# 11. Rating above 4 and relase year above 2005
# A. Rating mxm movies full data
# B. Rating mnm movies full data

# df1=df.loc[(df['rating']>4) & (df['year']>2005)].sort_values(by='rating',ascending=False)
# #print(df1)
#
# df2=df1.loc[df1['rating']==4.5]
# #print(df2)
#
# df3=df1.loc[df1['rating']==4.1]
# print(df3)

#---------------------------------------------
#12. 2008 movies count

# df1=df.loc[df['year']==2008].groupby('year')['year'].count()
# print(df1)

#----------------------------------------------------
#13. 1975-2000 movies collect
#A. Row count

# df1=df.loc[(df['year']>=1975) & (df['year']<=2000)]
# print(df1)
# print(df1.shape)

#------------------------------------------------------
#14. 1975-2000 and rating above 3.5 total row count

# df1=df.loc[(df['year']>=1975) & (df['year']<=2000) & (df['rating']>3.5)]
# print(df1)
# print(df1.shape)