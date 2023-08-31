import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load the SMS Spam Collection dataset
data = pd.read_csv('sms_spam_collection.csv', encoding='latin-1')

# Rename columns for clarity
data.columns = ['label', 'message']

# Convert labels to binary values (0 for ham, 1 for spam)
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# Split data into features (X) and target (y)
X = data['message']
y = data['label']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the CountVectorizer to convert text into numerical features
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Initialize the Multinomial Naïve Bayes model
model = MultinomialNB()

# Train the model
model.fit(X_train_vectorized, y_train)

# Make predictions
y_pred = model.predict(X_test_vectorized)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Print classification report for more detailed evaluation
class_report = classification_report(y_test, y_pred, target_names=['ham', 'spam'])

print("Accuracy:", accuracy)
print("Classification Report:\n", class_report)