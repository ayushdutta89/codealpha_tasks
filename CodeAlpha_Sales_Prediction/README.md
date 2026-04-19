#  Sales Prediction using Machine Learning

##  Project Overview

This project focuses on predicting future sales based on advertising expenditure across different platforms such as TV, Radio, and Newspaper.

A regression model is used to understand how advertising impacts sales and to forecast future sales values.

---

##  Objective

* To analyze the relationship between advertising spend and sales
* To build a regression model for predicting sales
* To understand the impact of different marketing channels
* To gain insights for better business decision-making

---

##  Dataset

The dataset contains advertising data with the following features:

* TV (Advertising budget spent on TV)
* Radio (Advertising budget spent on Radio)
* Newspaper (Advertising budget spent on Newspaper)
* Sales (Target Variable)

###  Preprocessing Steps

* Removed unnecessary index column (`Unnamed: 0`)
* Checked for missing values
* Selected relevant features for training

---

##  Algorithm Used

**Linear Regression**

* A supervised learning algorithm used for predicting continuous values
* Models the relationship between advertising spend and sales

---

## ⚙️ Steps Performed

1. Loaded dataset using Pandas
2. Cleaned and preprocessed data
3. Selected features (TV, Radio, Newspaper) and target (Sales)
4. Split dataset into training and testing sets (80% training, 20% testing)
5. Trained Linear Regression model
6. Predicted sales values
7. Evaluated model performance
8. Visualized results using scatter plot

---

##  Results

* **R² Score:** 0.86
* **Mean Absolute Error (MAE):** 1.51

The model shows strong performance in predicting sales based on advertising expenditure.

---

##  Visualization

A scatter plot of Actual vs Predicted Sales was used to evaluate model performance.
Points lying close to the diagonal indicate good predictions.

---

##  Key Insights

* TV advertising has the highest impact on sales
* Radio has moderate influence
* Newspaper has the least impact
* Increasing advertising budget can significantly improve sales outcomes

---

##  Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib

---


## 📌 Conclusion

The project demonstrates how machine learning can be used to predict sales and analyze the effectiveness of advertising strategies. It provides useful insights for optimizing marketing budgets.

---

## 🔮 Future Improvements

* Use advanced models like Random Forest Regressor
* Perform hyperparameter tuning
* Include more features such as customer demographics
* Apply time-series forecasting techniques

---

##  Acknowledgment

This project is part of the CodeAlpha internship tasks.

