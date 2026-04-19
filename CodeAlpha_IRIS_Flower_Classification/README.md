#  Iris Flower Classification

##  Project Overview

This project focuses on building a Machine Learning model to classify Iris flowers into three species:

* Setosa
* Versicolor
* Virginica

The classification is based on flower measurements such as sepal length, sepal width, petal length, and petal width.

---

##  Objective

To understand and implement basic classification techniques in Machine Learning using the Iris dataset.

---

##  Dataset

The dataset contains 150 samples with the following features:

* SepalLengthCm
* SepalWidthCm
* PetalLengthCm
* PetalWidthCm
* Species (Target Variable)

Note: The `Id` column was removed as it does not contribute to prediction.

---

##  Algorithm Used

K-Nearest Neighbors (KNN)

* The model classifies a flower based on the majority class of its nearest neighbors.
* In this project, K = 3 is used.

---

##  Steps Performed

1. Loaded dataset using Pandas
2. Removed unnecessary columns (Id)
3. Separated features (X) and target (y)
4. Converted categorical labels into numeric form
5. Split dataset into training and testing sets (70% training, 30% testing)
6. Trained KNN model
7. Evaluated model using accuracy, confusion matrix, and classification report

---

##  Results

* Accuracy: 100%
* The model correctly classified all test samples.

---

##  Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn

---


##  Conclusion

The KNN model performed exceptionally well on the Iris dataset due to its simplicity and well-separated classes. This project helps in understanding the fundamentals of classification in Machine Learning.

---

## 🙌 Acknowledgment

This project is part of the CodeAlpha internship tasks.

