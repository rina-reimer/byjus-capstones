## Life Expectancy Analysis
# The term Life Expectancy refers to the number of years a person can expect to live. It is based on an estimate of the average age of a population when they die. 
# Life expectancy is one of the key metrics used for assessing the overall health of a population.
# The increases are nearly universal, from the richest to the poorest countries. Let's dive deeper into the life expectancy dataset and find out how different factors influence your life expectancy.
# As the head of a leading life insurance company, your job is to formulate global health insurance coverage plans and devise different life insurance solutions for different countries. 
# For this, you need to obtain insightful trends and patterns in people's dying age across different countries. 
# Also, you need to determine the factors that affect the average life expectancy of the people around the world to determine the premium rates for insurance policies.
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

file_path = 'https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/life-expectancy/life-expectancy.csv'
df = pd.read_csv(file_path)
# Remove whitespace from both ends of the column names
for col in df.columns:
  df.rename(columns = {col : col.strip()}, inplace = True)
# Checking for the percentage null values in all the columns.
print(round(df.isnull().sum() * 100 / df.shape[0], 2))
missing_nums = round(df.isnull().sum() * 100 / df.shape[0], 2)
cols_to_drop = missing_nums.loc[missing_nums>15]
cols_to_drop = cols_to_drop.index
df = df.drop(columns = cols_to_drop)
cols_having_null_values = []
for col in df.columns:
  if df[col].isnull().sum() > 0:
    cols_having_null_values.append(col)
print("Columns with missing values:\n", cols_having_null_values)

# Statistics of Developed Countries
grouped_status = df.groupby('Status')
developed_df = grouped_status.get_group('Developed')
cols_developed_null_values = developed_df[cols_having_null_values].isnull().sum().loc[developed_df[cols_having_null_values].isnull().sum()>0]
cols_developed_null_values = cols_developed_null_values.index
print("Descriptive Statistics Summary:\n", developed_df[cols_developed_null_values].describe())
# Replacing the missing values of the developed countries DataFrame with the median value of the respective columns.
for col in cols_developed_null_values:
  developed_df[col].fillna((developed_df[col].median()), inplace = True)
print("New Descriptive Statistics Summary:\n", developed_df[cols_developed_null_values].describe())

# Statistics of Developing Countries
grouped_status = df.groupby(by = "Status")
developing_df = grouped_status.get_group('Developing')
cols_developing_null_values = developing_df[cols_having_null_values].isnull().sum().loc[developing_df[cols_having_null_values].isnull().sum()>0]
cols_developing_null_values = cols_developing_null_values.index
print("Descriptive Statistics Summary:\n", developing_df[cols_developing_null_values].describe())
# Replacing the missing values of the developing countries DataFrame with the median value of the respective columns.
for col in cols_developing_null_values:
  developing_df[col].fillna((developing_df[col].median()), inplace = True)
print("New Descriptive Statistics Summary:\n", developing_df[cols_developing_null_values].describe())

# Life expectancy w.r.t Year using bar plot for developed countries
plt.figure(figsize = (18, 5))
plt.bar(developed_df.groupby('Year')['Year'].unique(), developed_df.groupby('Year')['Life expectancy'].mean())
plt.xlabel("Year", fontsize = 12)
plt.ylabel("Average Life Expectancy", fontsize = 12)
plt.title("Average Life Expectancy w.r.t Year")
plt.show()

# Life expectancy w.r.t Year using bar plot for developing countries
plt.figure(figsize = (18, 5))
plt.bar(developing_df.groupby('Year')['Year'].unique(), developing_df.groupby('Year')['Life expectancy'].mean())
plt.xlabel("Year", fontsize = 12)
plt.ylabel("Average Life Expectancy", fontsize = 12)
plt.title("Average Life Expectancy w.r.t Year")
plt.show()

# Create a bar plot for yearly life expectancy of developing and developed countries in a single bar chart.
plt.figure(figsize = (18, 5))
plt.bar(developed_df.groupby('Year')['Year'].unique(), developed_df.groupby('Year')['Life expectancy'].mean(), color = "yellow")
plt.bar(developed_df.groupby('Year')['Year'].unique(), developing_df.groupby('Year')['Life expectancy'].mean(), color="red")
plt.xlabel("Year", fontsize = 12)
plt.ylabel("Average Life Expectancy", fontsize = 12)
plt.title("Average Life Expectancy w.r.t Year")
plt.show()

# Finding the overall average life expectancy of developed and developing countries
round(df[['Status','Life expectancy']].groupby(['Status']).mean())