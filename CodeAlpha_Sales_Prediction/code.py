import pandas as pd

#Loading dataset
df = pd.read_csv(r"C:\Users\dayus\CodeAlpha_Sales_Prediction\Advertising.csv")
print(df.head())

#Dropping the first column(Just index column)
df.drop("Unnamed: 0", axis=1, inplace=True)

#Splitting the dataset into features and target variable
x = df.drop("Sales",axis=1)
y = df["Sales"]

#Splitting the dataset into training and testing sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test= train_test_split(x,y,test_size=0.3,random_state=42)

#Training the model using Linear Regression
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)

# Predict
y_pred = model.predict(x_test)

# Evaluate
from sklearn.metrics import r2_score, mean_absolute_error
print("R2 Score:", r2_score(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))

# Visualization
import matplotlib.pyplot as plt
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.show()