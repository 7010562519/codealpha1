import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

# Sample FAQ data
faq_data = [
    {"question": "What is your return policy?", "answer": "You can return any product within 30 days of purchase."},
    {"question": "How can I track my order?", "answer": "Use the tracking link sent to your email to track your order."},
    {"question": "Do you offer international shipping?", "answer": "Yes, we ship to most countries globally."},
    {"question": "What payment methods are accepted?", "answer": "We accept credit cards, debit cards, and PayPal."},
    {"question": "How do I contact customer support?", "answer": "You can contact support via email or our help center."}
]

# Text preprocessing function using SpaCy
def preprocess(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return " ".join(tokens)

# Preprocess all FAQ questions
for faq in faq_data:
    faq["processed_question"] = preprocess(faq["question"])

# Create TF-IDF matrix
vectorizer = TfidfVectorizer()
question_texts = [faq["processed_question"] for faq in faq_data]
tfidf_matrix = vectorizer.fit_transform(question_texts)

# Get response based on user input
def get_faq_response(user_input):
    user_input_processed = preprocess(user_input)
    user_vector = vectorizer.transform([user_input_processed])
    similarity_scores = cosine_similarity(user_vector, tfidf_matrix)
    best_match_index = similarity_scores.argmax()
    best_score = similarity_scores[0, best_match_index]

    if best_score > 0.3:
        return faq_data[best_match_index]["answer"]
    else:
        return "Sorry, I couldn't find a matching answer."

# Chat loop
print("🤖 Chatbot: Hi! Ask me something (type 'exit' to quit):")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("🤖 Chatbot: Goodbye!")
        break
    response = get_faq_response(user_input)
    print("🤖 Chatbot:", response)
