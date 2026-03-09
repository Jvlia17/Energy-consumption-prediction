**Energy Consumption Analysis & Prediction**<br />
Analysis and prediction of building energy consumption based on weather data, HVAC and lighting usage, and time features.

*Project Goals*<br />
We analyze how external factors influence energy consumption by exploring the data with visualizations, building a regression model to make predictions, and evaluating the model to identify the most important features.

*Dataset*<br />
The dataset used in this project comes from Kaggle and contains information for predicting energy consumption: https://www.kaggle.com/datasets/mrsimple07/energy-consumption-prediction/data

*Modeling*<br />
Model: Random Forest Regressor<br />
Train/test split: 80/20<br />
Evaluation metrics: Mean Absolute Error (MAE), R² score

*Results*<br />
MAE: e.g., 12 (average absolute error in energy units)<br />
R²: e.g., 0.85 (proportion of variance explained by the model)

The results show that temperature is the most important factor influencing energy consumption, with a feature importance of around 0.58. This is consistent with the correlation heatmap, where temperature has a strong positive correlation (≈0.7) with energy consumption, indicating that higher temperatures are associated with higher energy usage.
The scatter plot confirms the relationship between temperature and energy consumption, showing a clear upward trend: as temperature increases, energy consumption generally increases as well.
Overall, the analysis suggests that temperature is the dominant driver of energy consumption in the dataset, while the other factors play a relatively minor role.

*Visualizations*

<img width="738" height="568" alt="plot1" src="https://github.com/user-attachments/assets/efe9daa0-d769-4764-9ee5-70de8ffa1703" />

<img width="1537" height="931" alt="plot2" src="https://github.com/user-attachments/assets/6326c841-fa02-475c-8ff3-cdff28cc1bc2" />

<img width="786" height="588" alt="plot3" src="https://github.com/user-attachments/assets/72a67a23-8689-4ec3-8c98-2205392fa896" />
