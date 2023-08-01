## Pulsar Star Prediction
# Pulsar stars are a rare type of Neutron stars that produce radio emissions detectable on Earth. They are of considerable scientific interest as probes of space-time, the interstellar medium, and states of matter.
# As pulsars rotate, their emission beam sweeps across the sky, and when this crosses our line of sight, it produces a detectable pattern of broadband radio emission.
# As pulsars rotate rapidly, this pattern repeats periodically. Thus pulsar search involves looking for periodic radio signals using large radio telescopes.
# Machine learning tools are now being used to automatically label pulsar candidates to facilitate rapid analysis.

import pandas as pd
import xgboost as xg
from sklearn.metrics import confusion_matrix, classification_report

train = pd.read_csv('https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/project-5/pulsar-star-prediction-train.csv')
test = pd.read_csv('https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/project-5/pulsar-star-prediction-test.csv')
print("Train data null values:\n", train.isnull().sum())
print("Test data null values:\n", test.isnull().sum())
# Print the count of the '0' and '1' classes in the 'train_df' DataFrame.
print("Train data value counts:\n", train.iloc[:, 0].value_counts())
print("Test data value counts:\n", test.iloc[:, 0].value_counts())
# Feature variables
x_train = train.iloc[:, 1:]
x_test = test.iloc[:, 1:]
# Target variables
y_train = train.iloc[:, 0]
y_test = test.iloc[:, 0]

## Build A XGBoost Classifier model
# Predict the target variable based on the feature variables of the test dataframe.
model = xg.XGBClassifier()
model.fit(x_train,y_train)
y_predicted = model.predict(x_test)
print("Confusion Matrix:\n", confusion_matrix(y_test, y_predicted))
print("Classification Report:\n", print(classification_report(y_test, y_predicted)))

# Interpretation 1: It is more accurate in predicting the negative class, as the predcitions are closer to 1
# Interpretation 2: predictions of the negative class are almost 1, meaning they are highly accurate
# Interpretation 3: This is an accurate data process