#Importing the Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Loading the dataset
dataset = pd.read_csv("diabetes.csv")

#Taking the 20 samples only to show
dataset.sample(20)

#Finding out if the dataset contains any null value.Thus we don't get any missing values.
dataset.info()

#Showing the information of the name of the columns with their meanings
info = ["Number of times pregnant",
"Plasma glucose concentration a 2 hours in an oral glucose tolerance test",
"Diastolic blood pressure (mm Hg)",
"Triceps skin fold thickness (mm)",
"2-Hour serum insulin (mu U/ml)",
"Body mass index (weight in kg/(height in m)^2)",
"Diabetes pedigree function",
"Age (years)",
"Class variable (0 or 1) 268 of 768 are 1, the others are 0"]
for i in range (len(info)):
    print(dataset.columns[i],"-->",info[i])
    
#Dividing dataset into X(independent parameters) and Y(dependent parameter)
X = dataset.drop('outcome', axis = 'columns')
Y = dataset.outcome

#Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20, random_state = 0)

#Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, Y_train)
Y_pred = classifier.predict(X_test)

#Calculating Accuracy
from sklearn import metrics
print(metrics.accuracy_score(Y_test, Y_pred))

#Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_pred)

#Plotting graph of confusion matrix
plt.figure()
plt.matshow(cm, cmap='Pastel2')

for x in range(0, 2):
    for y in range(0, 2):
        plt.text(x, y, cm[x, y])
        
plt.ylabel('expected label')
plt.xlabel('predicted label')
plt.show()

import pickle
with open('diabetes_prediction.pickle','wb') as f:
    pickle.dump(classifier,f)

print(X.columns)

import json
columns = {
        'data_columns' : [col.lower() for col in X.columns]
}
with open('columns.json','w') as f:
    f.write(json.dumps(columns))
        
def predict_price(pregnancies,glucose,bloodpressure,skinthickness,insulin,bodymassindex,diabetespedigreefunction,age):
    X1 = np.zeros(len(X.columns))
    X1[0] = pregnancies
    X1[1] = glucose
    X1[2] = bloodpressure
    X1[3] = skinthickness
    X1[4] = insulin
    X1[5] = bodymassindex
    X1[6] = diabetespedigreefunction
    X1[7] = age
    
    return classifier.predict([X1])[0]

predict_price(6,148,72,35,0,33.6,0.627,50)
predict_price(1,85,66,29,0,26.6,0.351,31)

