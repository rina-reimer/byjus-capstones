## House Price Prediction
# You are willing to sell your house. You are not sure about the price of your house and want to estimate its price. 
# You are provided with the dataset and need to make a prediction model which will help you to get a good estimate of your house for selling it.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.feature_selection import RFE

df = pd.read_csv("https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/house-prices.csv")
print("Check for null values:\n", df.isnull().sum())

## Exploratory Data Analysis
cate = list(df.columns[5:])
cate.remove("parking")
for i in cate:
    plt.figure()
    sns.boxplot(df[i], df["price"])
    plt.show()
sns.scatterplot(df["area"], df["price"])
plt.show()
sns.scatterplot(df["bedrooms"], df["price"])
plt.show()
sns.scatterplot(df["bathrooms"], df["price"])
plt.show()
sns.scatterplot(df["stories"], df["price"])
plt.show()

# Create a normal distribution curve for the 'price'.
import numpy as np
def prob_den(x):
  pt1 = 1 / (x.std() * np.sqrt(2*np.pi))
  pt2 = np.exp( - (x - x.mean())**2 / (2 * x.var()))
  return pt1*pt2
z = prob_den(df["price"])
plt.scatter(df["price"], z)
plt.show()

## Feature Encoding
# Replace yes with 1 and no with 0 for all the values in features 
obj = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']
for i in obj:
    df[i].replace({"yes": 1, "no":0}, inplace = True)
# Perform one hot encoding for furnishingstatus feature.
dummy = pd.get_dummies(df["furnishingstatus"], dtype = int, drop_first = False)
df = df.drop("furnishingstatus", axis = 1)
df = pd.concat([df, dummy], axis = 1)

## Model Building
features = df.drop("price", axis = 1)
xtr, xte, ytr, yte = train_test_split(features, df["price"], test_size = 0.33, random_state=384628)
xtr_sm = sm.add_constant(xtr)
model = sm.OLS(ytr, xtr_sm)
results = model.fit()
print(results.summary())

## Model Evaluation
lr = LinearRegression().fit(xtr, ytr)
y_pred = lr.predict(xte)
print("r2_score", r2_score(yte, y_pred))
print("mean_squared_error", mean_squared_error(yte, y_pred))
print("mean_absolute_error", mean_absolute_error(yte, y_pred))

## Recursive Feature Elimination
rfe = RFE(lr, n_features_to_select=7)
rfe.fit(xtr[features.keys()], ytr)
sel_features = xtr[features.keys()].columns[rfe.support_]
features = df[sel_features]
xtr, xte, ytr, yte = train_test_split(features, df["price"], test_size = 0.33, random_state = 23532)
lr1 = LinearRegression().fit(xtr, ytr)
print("Intercept:", lr.intercept_)
for i in range(len(features.columns)):
    print(features.columns[i], lr1.coef_[i]) 
    ypr = lr1.predict(xte)
print("r2_score", r2_score(yte, ypr))
print("mean_squared_error", mean_squared_error(yte, ypr))
print("mean_absolute_error", mean_absolute_error(yte, ypr))

## Residual Error Analysis
ypred = lr1.predict(xtr)
errortr = ypred-ytr
plt.hist(errortr)
plt.axvline(errortr.mean(), color = "red")
plt.show()
errorte = ypr-yte
plt.hist(errorte)
plt.axvline(errorte.mean(), color = "red")
plt.show()

## Verify Homoscedasticity
plt.scatter(errortr, ytr)