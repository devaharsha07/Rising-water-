import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
data = pd.read_csv('dataset/flood.csv')
X = data.drop('FloodProbability', axis=1)
y = data['FloodProbability']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
model = DecisionTreeRegressor()
model.fit(X_train, y_train)
print("Model trained successfully.")
y_pred = model.predict(X_test)

print("First 10 Predictions:")
print(y_pred[:10])

print("\nFirst 10 Actual Values:")
print(y_test[:10])
from sklearn.metrics import mean_absolute_error, r2_score

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("Mean Absolute Error:", mae)
print("R2 Score:", r2)
from sklearn.ensemble import RandomForestRegressor
print("\n==============================")
print("RANDOM FOREST MODEL")
print("==============================")

rf_model = RandomForestRegressor(random_state=42)

rf_model.fit(X_train, y_train)

rf_predictions = rf_model.predict(X_test)

rf_mae = mean_absolute_error(y_test, rf_predictions)
rf_r2 = r2_score(y_test, rf_predictions)

print("Random Forest MAE:", rf_mae)
print("Random Forest R2 Score:", rf_r2)
print("\n==============================")
print("KNN MODEL")
print("==============================")

knn_model = KNeighborsRegressor(n_neighbors=5)

knn_model.fit(X_train, y_train)

knn_predictions = knn_model.predict(X_test)

knn_mae = mean_absolute_error(y_test, knn_predictions)
knn_r2 = r2_score(y_test, knn_predictions)

print("KNN MAE:", knn_mae)
print("KNN R2 Score:", knn_r2)
print("\n==============================")
print("XGBOOST MODEL")
print("==============================")

xgb_model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    random_state=42
)

xgb_model.fit(X_train, y_train)

xgb_predictions = xgb_model.predict(X_test)

xgb_mae = mean_absolute_error(y_test, xgb_predictions)
xgb_r2 = r2_score(y_test, xgb_predictions)

print("XGBoost MAE:", xgb_mae)
print("XGBoost R2 Score:", xgb_r2)
import joblib
joblib.dump(xgb_model, "floods.save")

print("\nBest model saved successfully as floods.save")
import pandas as pd

data = pd.read_csv("dataset/flood.csv")
print(data.columns)