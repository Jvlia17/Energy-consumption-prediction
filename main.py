import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import numpy as np

df = pd.read_csv("Energy_consumption.csv")

print(df.head())
print(df.info())
print(df.describe())

plt.figure(figsize=(8,6))

sns.scatterplot(
    x=df["Temperature"],
    y=df["EnergyConsumption"],
    hue=df["EnergyConsumption"], 
    palette="inferno",
    s=50,
    alpha=0.7,
    edgecolor="k"
)

plt.title("Temperature vs Energy Consumption")

plt.show()

plt.figure(figsize=(10,8))

corr = df.corr(numeric_only=True)

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)

plt.title("Feature Correlation Heatmap")

plt.show()

df["HVACUsage"] = df["HVACUsage"].map({"On":1,"Off":0})
df["LightingUsage"] = df["LightingUsage"].map({"On":1,"Off":0})
df["Holiday"] = df["Holiday"].map({"Yes":1,"No":0})

df = pd.get_dummies(df, columns=["DayOfWeek"], drop_first=True)

df = df.drop(columns=["Timestamp"])

X = df.drop("EnergyConsumption", axis=1)
y = df["EnergyConsumption"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

mae = mean_absolute_error(y_test, pred)

print("MAE:", mae)

importance = model.feature_importances_
feat_imp = pd.Series(importance, index=X.columns)

feat_imp_sorted = feat_imp.sort_values()

colors = plt.cm.inferno(np.linspace(0, 1, len(feat_imp_sorted)))

feat_imp_sorted.plot(kind="barh", figsize=(8,6), color=colors)

plt.title("Feature Importance", fontsize=14)
plt.xlabel("Importance")
plt.ylabel("Features")
plt.tight_layout()
plt.show()
