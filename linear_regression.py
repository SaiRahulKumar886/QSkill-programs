import pandas as pd

df = pd.read_csv("train.csv")
print(df.head())
print(df.info())
features = [
    'OverallQual',     # overall material and finish quality
    'GrLivArea',       # above ground living area (size)
    'GarageCars',      # garage capacity
    'TotalBsmtSF',     # basement area
    'FullBath',        # number of bathrooms
    'YearBuilt',       # age of house
    'Neighborhood'     # location
]

target = 'SalePrice'

df = df[features + [target]]
df = df.dropna()
df = pd.get_dummies(df, columns=['Neighborhood'], drop_first=True)
from sklearn.model_selection import train_test_split

X = df.drop('SalePrice', axis=1)
y = df['SalePrice']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
from sklearn.metrics import mean_absolute_error, r2_score

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error:", mae)
print("R2 Score:", r2)
import matplotlib.pyplot as plt

plt.scatter(y_test, y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")
plt.show()
