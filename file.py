# first step is to import the necessary libraries 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
 
# second step is rew mesy data lode using pandas library
df = pd.read_csv("/Users/macbook/Desktop/covid19_raw.csv")
print(df)
# so we have 104 rows and 6 columns and then we will do task for understand what problems exist. These 4 print statements tell you everything about the data — size, sample rows, types, and nulls.
print(df.shape)
print(df.head())
print(df.dtypes)
print(df.isnull().sum())
# so we have identifiied that there are some null values in the data and latter also uneven distribution of data so we will do some data cleaning and data preprocessing to make the data more useful for analysis and visualization.
df["country"] = df["country"].str.strip().str.title()
df["country"]=df["country"].replace("Usa","USA")
print(df["country"].unique())
# here i fix str.strip() removes extra spaces. str.title() makes first letter capital — "india" → "India". Then we fix "Usa" → "USA" manually.
df["date"] = pd.to_datetime(df["date"],format="mixed")
print(df["date"].dtype)
# next step is remove duplicate vaule and also remove null value 
print(df.shape)
df = df.drop_duplicates()
print(df.shape)
# here result is fist shape 104X6 after remove duplicates value so noe data is 102X6 and reomve the null value .
num_cols = ["confirmed","deaths","recovered","active"]
df[num_cols]= df[num_cols].fillna(0).astype(int)
print(df.isnull().sum())
#  here null value count is 0 and then next step to add new some cols .
df["mortality_rate"]= (df["deaths"] / df["confirmed"].replace(0,np.nan) * 100).round(2)
df["recovery_rate"]=(df["recovered"]/ df["confirmed"].replace(0,np.nan) * 100).round(2)

print(df[["country","mortality_rate","recovery_rate"]].head()) 
# here we have added two new columns mortality_rate and recovery_rate and then we will do some data visualization to understand the data better.
df = df.to_csv("covid19_cleaned.csv")

