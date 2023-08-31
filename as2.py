import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Load your dataset
data = pd.read_csv('Data/HR_comma_sep.csv.txt')

# Data Wrangling - Explore the data
print(data.head())
print(data.describe())

# Data Visualization - Create insights graphs
plt.figure(figsize=(10, 6))
data['left'].value_counts().plot(kind='bar')
plt.title('Employee Exit (1) vs Retained (0)')
plt.xlabel('Exit Status')
plt.ylabel('Count')
plt.show()

# Preprocessing
X = data.drop('left', axis=1)
y = data['left']

# Encode categorical variables
label_encoder = LabelEncoder()
X['department'] = label_encoder.fit_transform(X['department'])
X['salary'] = label_encoder.fit_transform(X['salary'])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize the Random Forest Classifier model
model = RandomForestClassifier(random_state=42)

# Train the model
model.fit(X_train_scaled, y_train)

# Make predictions
y_pred = model.predict(X_test_scaled)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)