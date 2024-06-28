from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib


model_path = 'path/to/your/model.pkl'
model = joblib.load(model_path)

def classify_report(report_text):
    preprocessed_text = preprocessed_text(report_text)
    #load pre trained data (if available)
    #this section omitted for brevity. you might load pre trained TF-IDF vectors and a trained model.

    #train the model (if no pre trained data)
    #this section omitted for brevity. train a model on your bug report datausing TF-IDF and MultinomialNB.

    #CLASSIFY NEW REPORT
    vectorizer = TfidfVectorizer()
    X_new = vectorizer.fit_transform([preprocessed_text])
    predicted_class = model.predict(X_new)[0]
    probability = model.predict_proba(X_new)[0][predicted_class]

#RETURN CLASSIFICATION RESULTS
    return{"type":predicted_class,
           "probability": probability}
#HELPER FUNC TO PREPROCESS TEXT
#(implementation omitted for brevity)
def preprocess_text(text):
    #... (add preprocssing steps like tokenization, stop word removal)
    pass