(mport pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load the weather dataset
data = pd.read_csv('weather_dataset.csv')

# Convert categorical variables to numerical using one-hot encoding
data_encoded = pd.get_dummies(data, columns=['Outlook', 'Temperature', 'Humidity', 'Wind'])

# Split data into features (X) and target (y)
X = data_encoded.drop('Play', axis=1)
y = data_encoded['Play']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Gaussian Naïve Bayes model
model = GaussianNB()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)