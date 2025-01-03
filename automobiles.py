import pandas as pd
from numpy.ma.core import inner

df=pd.read_csv(r"C:\Users\asifh\OneDrive\Desktop\Data Sets\Automobile_data.csv")
#print(df)

#-------------------------------------------

#1. From the given dataset print the first and last five rows

# x=df.head(1)
# y=df.tail(5)
# df1=x._append(y)
# print(df1)

#---------------------------------------------------------

#2. Find the missing values and Check if there is any duplicate values

#print(df.isna().sum())
#print(df.duplicated().sum())

#-------------------------------------------------

#3. Print All Toyota Cars details.

# df1=df.loc[df['company']=='toyota']
# print(df1)

#----------------------------------------------

#4. Count total cars per company

# df1=df.groupby(by='company') ['company'].count()
# print(df1)

#--------------------------------------------

#5. Find each company’s Highest price car.

# df1=df.groupby(by='company') ['price'].max()
# print(df1)

#-----------------------------------------------

#6. Find the average mileage of each car making company.

# df1=df.groupby(by='company') ['average-mileage'].mean()
# print(df1)

#-----------------------------------------------

#7. Sort all cars by Price column.

# df1=df.sort_values(by='price')
# print(df1)

#---------------------------------------------------

#8. Sort all cars by Price column

# df1=df.sort_values(by='price',ascending=False)
# print(df1)

#------------------------------------------

#9. Concatenate two data frames using the following condition.
#Create two data frames using the following two dictionaries.

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'],
'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan',
'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}

df1=pd.DataFrame(GermanCars)
#print(df1)
df2=pd.DataFrame(japaneseCars)
#print(df2)

df3=pd.concat([df1,df2],keys=['German',"Japan"])
print(df3)

#-------------------------------------------------------------

# 10.Merge two data frames using the following condition.
# Create two data frames using the following two Dicts, Merge two
# data frames, and append the second data frame as a new column to
# the first data frame.
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'],
'Price': [23845, 17995, 135925 , 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'],
'horsepower': [141, 80, 182 , 160]}

# df1=pd.DataFrame(Car_Price)
# #print(df1)
# df2=pd.DataFrame(car_Horsepower)
# #print(df2)
# df3=pd.merge(df1,df2,on='Company',how='left')
# print(df3)

