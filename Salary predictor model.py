import pandas as pd
# We import pandas to load our data

df = pd.read_csv("C:\Users\nafis\salaryData.csv")
# We read our csvfile

df.dropna(inplace = True)
# We remove rows with missing values
df_converted = pd.get_dummies(df, columns=["Gender", "Education Level", "Job Title"], drop_first=True)
# We converte categorical features into numbers
# This line of code looks at the original dataframe(df) then finds the listed colums and replace them with numeric columns(0 or 1)
x = df_converted.drop("Salary", axis=1)
# x takes the new dataframe with all features in our dataset except salary 
# axis=1 specify that we drop a column
y = df_converted["Salary"]
# y represent the value that we want to predict which is the 

from sklearn.model_selection import train_test_split
# Split our dataset into two sets (one for training and another one for testing)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state=20)
# 70% of our dataset is used for training and 30% used for testing
# Setting random_state to a fixed constant helps us get the same sets every time the dataset is shuffled

from sklearn.ensemble import RandomForestRegressor
# import a machine learning model (RandomForestRegressor that creates decision trees to make prediction)
model = RandomForestRegressor(n_estimators=75, random_state=20)
# The model create 75 trees 
# Setting random_state to 20 helps get the same result every time
model.fit(x_train,y_train)
# The model learns how x_train (features in our dataset except salary) relates to y_train(salary)
y_predictor = model.predict(x_test)
# The model predicts salaries (y_salaries) for the testing set (x_test)

from sklearn.metrics import r2_score, mean_squared_error
# Metrics are used to evaluate model performance
print(r2_score(y_test, y_predictor))
# Determine the quality of prediction 
print(mean_squared_error(y_test, y_predictor, squared=False))
# Check the differneces between predicted salaries and actual salaries

import joblib
joblib.dump((model, x.columns), 'Salary predictor model.py')