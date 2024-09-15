import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = {
    'Height': [5.5, 6.0, 5.8, 5.7, 6.1, 5.9, 6.2, 5.6, 5.8, 5.7],
    'Weight': [150, 180, 160, 170, 190, 165, 200, 155, 165, 175],
    'Gender': [0, 1, 0, 0, 1, 0, 1, 0, 0, 0]  # 0 = Female, 1 = Male
}

df = pd.DataFrame(data)

X = df.drop('Gender', axis=1)  # Features: 'Height' and 'Weight'
y = df['Gender']  # Target: 'Gender'

X_train_70, X_test_30, y_train_70, y_test_30 = train_test_split(X, y, test_size=0.3, random_state=42)
X_train_80, X_test_20, y_train_80, y_test_20 = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()

model.fit(X_train_70, y_train_70)
predictions_70 = model.predict(X_test_30)
accuracy_70 = accuracy_score(y_test_30, predictions_70)

model.fit(X_train_80, y_train_80)
predictions_80 = model.predict(X_test_20)
accuracy_80 = accuracy_score(y_test_20, predictions_80)

print(f"Accuracy with 60-40 split: {accuracy_70:.2f}")
print(f"Accuracy with 90-10 split: {accuracy_80:.2f}")
