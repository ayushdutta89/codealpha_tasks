#Loading the dataset

import pandas as pd

df = pd.read_csv(r"C:\Users\dayus\CodeAlpha_IRIS_Flower_Classification\Iris.csv")
print(df.head())  #Species : virginica, versicolor, setosa

#Data Preprocessing

#Seperating features and target variable
x = df.drop(["Species","Id"], axis=1) #Features
y = df["Species"] #Target variable.

#Converting categorial data into numerical data(Species)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y) #0=setosa,1=versicolor,2=virginica

#Spliting data into training and test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size =0.3,random_state=42)

#Training the Model
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)
model.fit(x_train,y_train)

#Prediting the test set results
y_pred = model.predict(x_test)

#Evaluating the model
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
