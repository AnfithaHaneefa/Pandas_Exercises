import pandas as pd
df=pd.read_csv(r"C:\Users\asifh\OneDrive\Desktop\Data Sets\txn.csv")
print(df)

#Q1 : Find Row count

print(df.shape)
#
# --------------------------
#Q2 : jan month oid,cusno,category,product,state
 #    A. Row count


df1=df.loc[(df['dat']>='01-01-2011') & (df['dat']<='01-31-2011')] [['cid','category','product','state']]
print(df1)
print(df1.shape)

# ---------------------------------------

#Q3 : July Month oid,cusno,category,product,state
#     B. Row count
#
df1=df.loc[(df['dat']>='07-01-2011') & (df['dat']<='07-31-2011')] [['cid','category','product','state']]
print(df1)
print(df1.shape)
#
# -------------------------------------------------------------
# 4. Each category [count desc sort]

df1=df.groupby('category')['category'].count().sort_values(ascending=False)
print(df1)
# ---------------------------------------------------------
#5. Category full deatils

df1=df.loc[df['category']=='Outdoor Recreation']
print(df1)


# ----------------------------------------
#6. Each paymethod count
#
df1=df.groupby('method')['method'].count()
print(df1)

#-------------------------------------------
# 7. jan-july month purchase count [include]

df1=df.loc[(df['dat']>='01-01-2011') & (df['dat']<='07-31-2011')].count()
print(df1)

#------------------------------------------------------
#8. Each category total amount

df1=df.groupby('category')['amount'].sum()
print(df1)

#---------------------------------------------------------
#9. Each category maximum amount

df1=df.groupby('category')['amount'].max()
print(df1)

#----------------------------------------------------
#9. Each category maximum amount

df1=df.groupby('category')['amount'].mean()
print(df1)

#----------------------------------------------
#11.total amount by cash and credit card

df1=df.groupby('method')['amount'].sum()
print(df1)

#-----------------------------------------------------
#12. Indoor games ,total amount

df1=df.loc[df['category']=='Indoor Games'] ['amount'].sum()
print(df1)

#--------------------------------------------
#13. Each state count

df1=df.groupby('state')['state'].count()
print(df1)