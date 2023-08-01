## Gender Voices Classification
# In this project, you are provided with a dataset which contains some statistical information about the audio frequencies of different male and female voices. 
# Based on the information provided, you have to find out which voice belongs to which gender using the RandomForestClassifier algorithm.
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
train = pd.read_csv("https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/project-4/gender-voice-train.csv")
test = pd.read_csv("https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/project-4/gender-voice-test.csv")
# Check for the missing values in the 'train_df' DataFrame.
print(train.isna().sum())
# Print count of 'male' & 'female' classes in the datasets
print(train.iloc[:, 0].value_counts())
print(test.iloc[:, 0].value_counts())
# Get the feature variables from the DataFrames.
x_train = train.iloc[:, 1:]
x_test = test.iloc[:, 1:]
# Get the target variable from the DataFrames.
y_train = train.iloc[:, 0] 
y_test = test.iloc[:, 0] 

# Build a Random Forest Classifier model.
rfc = RandomForestClassifier(n_jobs = -1, n_estimators = 100)
rfc.fit(x_train, y_train)
y_predicted = rfc.predict(x_test)
print(confusion_matrix(y_test,y_predicted))
print(classification_report(y_test,y_predicted))

# Interpretation 1: It's very accurate because the numbers are close to 1
# Interpretation 2: Based on the confusion matrix, there were far more true negatives and positives rather than false ones.
# Interpretation 3: The recall was slightly less accurate for predicting females.