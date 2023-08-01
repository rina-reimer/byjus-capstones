## Olivetti Faces Case-Study
# The dataset contains a set of images taken between April 1992 and 1994 at AT&T Laboratories Cambridge.
# The data includes ten different images of each of 40 distinct people.
# The images were taken at a different time and with varying lights, with different facial expression (open/closed eyes, smiling/not smiling) and with/without glasses.
# All the images were taken against a dark background with the people in an upright, frontal position.
# The goal here is to train the SVM classification model to identify the recognise the labels (identifying the people) based on the images.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report
import warnings 
warnings.filterwarnings("ignore")

df = pd.read_csv("https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/olivetti_X.csv", header = None)
target = pd.read_csv("https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/olivetti_y.csv", header = None)
df["target"] = target
print(df.shape)
print(df.head())
# Check the distribution of the labels in the target column.
print(df["target"].value_counts()/4, len(df["target"].value_counts()/4))

## Visualizing the Images
df_group = df.groupby(by = "target")

# Define the function to visualise the images
def vis_img(x):  
    dg = df_group.get_group(x)
    y = list(dg.index)[0]
    y = np.array(df.iloc[y, :-1])
    y = y.reshape(64, 64)
    plt.imshow(y)
    plt.show()
df.iloc[(list(df_group.get_group(5).index)[0]), :-1]
for i in df["target"].unique():
    vis_img(i)
features = df.drop("target", axis = 1)
# Create the feature and target variables
xtr, xte, ytr, yte = train_test_split(features, df["target"], test_size = 0.33, random_state=42)

# 1. Create the SVC model and pass 'kernel=linear' as input.
svc = SVC(kernel = "linear")
# 2. Call the 'fit()' function with 'X_train' and 'y_train' as inputs.
svc = svc.fit(xtr, ytr)
# 3. Call the 'score()' function with 'X_train' and 'y_train' as inputs to check the accuracy score of the model.
print("SVC Score:", svc.score(xtr, ytr))
ypr_tr= svc.predict(xtr)
ypr = svc.predict(xte)
conf = confusion_matrix(ytr, ypr_tr)
sns.heatmap(conf, annot=True)
plt.show()
print(classification_report(ytr, ypr_tr))
conf = confusion_matrix(yte, ypr)
sns.heatmap(conf)
print(classification_report(yte, ypr))