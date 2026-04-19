#  Car Price Prediction using Machine Learning

##  Project Overview

This project aims to train a regresion model and predict the selling price of cars based on various features such as mileage, engine specifications, fuel type, and more.

The model uses regression techniques to estimate car prices accurately.

---

##  Objective

* To understand regression in machine learning
* To preprocess real-world data
* To train a model for predicting continuous values (car prices)
* To evaluate model performance using appropriate metrics

---

##  Dataset

The dataset contains information about different cars with features such as:

* Car_Name
* Year
* Selling_Price (Target Variable)
* Present_Price
* Driven_kms
* Fuel_Type
* Selling_type
* Transmission
* Owner

###  Preprocessing Steps

* Removed **Car_Name** column (not useful for prediction)
* Converted **Year → Age** of the car
* Converted categorical variables using **one-hot encoding**
* Checked and handled missing values

---

##  Algorithm Used

**Linear Regression**

* A regression algorithm used to predict continuous values
* Learns relationship between features and target variable

---

##  Steps Performed

1. Loaded dataset using Pandas
2. Performed data preprocessing and feature engineering
3. Converted categorical variables into numeric form
4. Split dataset into training and testing sets (80% training, 20% testing)
5. Trained Linear Regression model
6. Predicted car prices on test data
7. Evaluated model performance

---

##  Results

* **R² Score:** 0.87
* **Mean Absolute Error (MAE):** 1.27

The model shows strong predictive performance with reasonably low error.

---

##  Visualization

A scatter plot of Actual vs Predicted prices can be used to visualize model performance.

---

##  Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib

---


##  Conclusion

The Linear Regression model successfully predicts car prices with good accuracy. The project demonstrates how machine learning can be applied to real-world problems like price estimation.

---


##  Acknowledgment

This project is part of the CodeAlpha internship tasks.

