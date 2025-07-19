import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Load and clean dataset
df = pd.read_csv("teen_phone_addiction_dataset.csv")
df.drop(columns=['ID', 'Name'], inplace=True)

# Bin addiction levels into 3 categories
df['Addiction_Level_Category'] = pd.cut(df['Addiction_Level'],
    bins=[-np.inf, 3.5, 7.5, np.inf],
    labels=[0, 1, 2]
)
df.drop(columns=['Addiction_Level'], inplace=True)
df.rename(columns={'Addiction_Level_Category': 'Addiction_Level'}, inplace=True)

# Drop rare target classes with fewer than 2 samples
target_col = 'Addiction_Level'
valid_classes = df[target_col].value_counts()[lambda x: x >= 2].index
df = df[df[target_col].isin(valid_classes)]

# Encode categorical columns manually
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
df['Phone_Usage_Purpose'] = df['Phone_Usage_Purpose'].map({
    'Social Media': 0,
    'Gaming': 1,
    'Education': 2,
    'Browsing': 3,
    'Other': 4
})

# Define top 8 impactful features
features_to_use = [
    'Gender', 'Daily_Usage_Hours', 'Sleep_Hours',
    'Phone_Checks_Per_Day', 'Apps_Used_Daily',
    'Time_on_Social_Media', 'Time_on_Gaming', 'Phone_Usage_Purpose'
]

# Subset data and drop rows with missing values in selected features
X = df[features_to_use]
y = df[target_col].astype(int)

valid_rows = X.dropna().index
X = X.loc[valid_rows]
y = y.loc[valid_rows]

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_scaled, y)

# Save model and scaler
joblib.dump(model, "logistic_regression_addiction_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("✅ Final training data shape:", X.shape)
print("✅ Model and scaler trained and saved successfully!")
