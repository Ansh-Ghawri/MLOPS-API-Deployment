import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib # Used for saving the model

print("Starting training...")

# 1. Load Data
df = pd.read_csv('data.csv')
X = df['text']
y = df['sentiment']
print(f"Loaded {len(df)} data points.")

# 2. Create a model pipeline
#    - CountVectorizer: Converts text into numerical features (word counts)
#    - MultinomialNB: A simple text classification algorithm
model_pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])
print("Defined model pipeline.")

# 3. Train the model
model_pipeline.fit(X, y)
print("Training complete.")

# 4. Save the trained model pipeline
#    We save the entire pipeline so it includes the vectorizer
joblib.dump(model_pipeline, 'sentiment_model.joblib')
print("Model saved to sentiment_model.joblib")