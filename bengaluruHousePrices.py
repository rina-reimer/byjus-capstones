## Bengaluru House Prices
# A practice in data cleaning
# There exists a dataset for Bengaluru house prices on the internet.
# The dataset found is vast with some useless information and some empty values. 
# We only want to extract some of the useful information from the dataset.

# The dataset acquired by the techie is full of irregularities, incorrect values, and missing values. As a data scientist (or analyst in this context), your task is to clean the dataset given to you.
# This process of preparing data for analysis by removing or modifying data that is incorrect, incomplete, irrelevant, duplicated, or improperly formatted is known as data cleaning.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/bengaluru-house-prices/Bengaluru_House_Prices.csv")
print("Null values:\n", df.isna().sum())
print("Percentage missing values:\n", (df.isna().sum()/df.shape[0]) * 100)
print("Missing value rows from location column:", df.loc[df["location"].isnull(), "location"])
df = df.drop(568, axis = 0)
print("Missing value rows from size column:",df.loc[df["size"].isnull(), "size"])
df = df.drop([579, 1775, 2264, 2809, 2862, 5333, 6423, 6636, 6719, 7680, 8306, 8565, 8703, 10634, 11019, 11569], axis = 0)
print("Rows with more than 5 bathrooms:", df.loc[df["bath"]>5, "bath"])
df = df.drop(df.loc[df["bath"]>5, "bath"].index, axis = 0)
print("Null values:\n", df.isna().sum())