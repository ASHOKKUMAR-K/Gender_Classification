# Importing the Dependency Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm

import pickle

# Importing the dataset
path = "weight-height.csv"
data = pd.read_csv(path)

# Splitting the dataset into Independent and Dependent Variables
X = data.iloc[:, 1:3].values
y = data.iloc[:, 0].values

# Splitting the data into Training and Testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)


# Defining the Classifier
classifier = svm.SVC(gamma = 'auto', random_state = 42, degree = 10)
classifier.fit(X_train, y_train)

# Predicting the Test results
y_pred = classifier.predict(X_test)

pickle.dump(classifier, open("gender_classifier.pkl", "wb"))

