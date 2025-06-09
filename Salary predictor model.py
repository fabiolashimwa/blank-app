# 1.Data loading
import pandas as pd
# We import pandas to load our data
df = pd.read_csv("salaryData.csv")
# We read our csvfile
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import joblib
df.fillna(method="ffill")
df = pd.get_dummies(df, colums=[""])
x = df.drop("Salary", axis=1)
y = df["Salary"]
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)
model = LinearRegression
model.fit(x_train, y_train)
model = RandomForestRegressor()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
print(r2_score(y_test, y_pred))
print(mean_squared_error(y_test, y_pred, squared=False))
joblib.dump(model, 'salary_predictor_model.pkl')