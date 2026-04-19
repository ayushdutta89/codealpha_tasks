import pandas as pd

#Loading Dataset
df = pd.read_csv(r"C:\Users\dayus\CodeAlpha_Car_Price_Prediction\car data.csv")
print(df.head())

#Removing unnecessary features/columns
df = df.drop("Car_Name",axis=1)

#Converting Year colum into Age of the car
df["Age"] = 2026 - df["Year"]
df = df.drop("Year", axis =1)

#Conveting Categorical features (Fuel_Type, Seller_Type, Transmission)
df = pd.get_dummies(df, drop_first=True)

#Splitting features and target variable
x = df.drop("Selling_Price", axis=1)
y = df["Selling_Price"]

#Spliting Training set and Test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state = 42)

#Training the model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)

# Predict
y_pred = model.predict(x_test)

# Evaluate
from sklearn.metrics import r2_score, mean_absolute_error

print("R2 Score:", r2_score(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))