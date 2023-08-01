## Diamond Price Prediction
# A diamond distributor decided to put almost 2000 diamonds for auction. 
# A jewellery company is interested in making a bid to purchase these diamonds in order to expand their business. 
# As a data scientist, your job is to build a prediction model to predict the price of diamonds so that your company knows how much it should bid.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.sparse.construct import random
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, classification_report
from statsmodels.stats.outliers_influence import variance_inflation_factor

df = pd.read_csv("https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/diamonds.csv")
df = df.drop("Unnamed: 0", axis = 1)
print(df.head())

## Exploratory Data Analysis
# Boxplot for 'cut' vs 'price'
sns.boxplot(df["cut"], df["price"])
plt.show()
# Boxplot for 'color' vs 'price'
sns.boxplot(df["color"], df["price"])
plt.show()
# Boxplot for 'clarity' vs 'price'
sns.boxplot(df["clarity"], df["price"])
plt.show()
# Create scatter plot with 'carat' on X-axis and 'price' on Y-axis
plt.scatter(df["carat"], df["price"])
plt.show()
# Create a normal distribution curve for the `price`.
def prob_den(x):
    pt1 = 1 / (x.std() * np.sqrt(2*np.pi))
    pt2 = np.exp( - (x - x.mean())**2 / (2 * x.var()))
    return pt1*pt2
# Create a probablity density function for plotting the normal distribution
z = prob_den(df["price"])
# Plot the normal distribution curve using plt.scatter() 
plt.scatter(df["price"], z)
plt.axvline(df["price"].mean())
plt.show()

## Feature Engineering
# Replace values of 'cut' column
df["cut"].replace({"Fair" : 1, "Good": 2, "Very Good": 3, "Premium": 4, "Ideal": 5}, inplace=True)
# Replace values of 'color' column
df["color"].replace({"D" : 1, "E": 2, "F": 3, "G": 4, "H": 5, "I":6, "J": 7}, inplace=True)
# Replace values of 'clarity' column
df["clarity"].replace({"I1": 1, "SI2": 2, "SI1": 3, "VS2": 4, "VS1": 5, "VVS2": 6, "VVS1": 7, "IF": 8}, inplace = True)

## Model Training
features = df.drop("price", axis = 1)
x_train, x_test, y_train, y_test = train_test_split(features, df["price"], test_size = 0.33, random_state=298374)
lr = LinearRegression().fit(x_train, y_train)
print("Intercept:", lr.intercept_)
for i in range(len(features.columns)):
  print("Features and their Coefficients:\n", features.columns[i], lr.coef_[i]) 
y_pred = lr.predict(x_test)
print(r2_score(y_test, y_pred), mean_squared_error(y_test, y_pred), mean_absolute_error(y_test, y_pred))

##Dealing with Multicollinearity
# Heatmap to pinpoint the columns in the 'df' DataFrame exhibiting high correlation
corr_df = df.corr()
plt.figure(figsize = (30,10))
sns.heatmap(data = corr_df, annot = True)
plt.show()
# Drop features highly correlated with 'carat'
df = df.drop(["x", "y", "z"], axis =1)
features = df.drop("price", axis = 1)
x_train, x_test, y_train, y_test = train_test_split(features, df["price"], test_size = 0.33, random_state=298374)
lr = LinearRegression().fit(x_train, y_train)
print("Intercept:", lr.intercept_)
for i in range(len(features.columns)):
  print("Features and their Coefficients:\n", features.columns[i], lr.coef_[i]) 
y_pred = lr.predict(x_test)
print(r2_score(y_test, y_pred), mean_squared_error(y_test, y_pred), mean_absolute_error(y_test, y_pred))
# Eliminate the features having VIF values above 10
features.insert(0, column = "constant", value = 0)
# Calculate the VIF values for the remaining features using the 'variance_inflation_factor' function.
vif1 = pd.DataFrame()
vif1["Features"] = x_train.columns
vif1["VIF"] = [variance_inflation_factor(x_train.values, i) for i in range(x_train.shape[1])]
print(vif1.head())
# Create a list of features having VIF values less than 10 
lis = []
for i in range(4):
    if vif1.iloc[i, 1] <10:
        lis.append(vif1.iloc[i, 0])
feat = df[lis]
xtr, xte, ytr, yte = train_test_split(feat, df["price"], test_size = 0.33, random_state=345235)
model = LinearRegression().fit(xtr, ytr)
print("Intercept:",model.intercept_)
for i in range(len(feat.columns)):
    print(lis[i], model.coef_[i])
y_pred = model.predict(xte)
print("r2 score:", r2_score(yte, y_pred))
print("mean squared error:", mean_squared_error(yte, y_pred))
print("mean absolute error:", mean_absolute_error(yte, y_pred))
vif1 = pd.DataFrame()
vif1["Features"] = xtr.columns
vif1["VIF"] = [variance_inflation_factor(xtr.values, i) for i in range(xtr.shape[1])]
print(vif1.head())

## Residual Error Analysis
ypred = model.predict(xtr)
errortr = ypred-ytr
plt.hist(errortr)
plt.axvline(errortr.mean(), color = "red")
plt.title("Errors from Train Dataset")
plt.show()
errorte = y_pred - yte
plt.hist(errorte)
plt.axvline(errorte.mean(), color = "red")
plt.title("Errors from Test Dataset")
plt.show()

## Verify Homoscedasticity
plt.scatter(errortr, ytr)
plt.show()