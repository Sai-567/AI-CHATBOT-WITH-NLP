import spacy

nlp = spacy.load("en_core_web_sm")
def chatbot_response(user_input):
    doc = nlp(user_input.lower())
    if any(token.lemma_ in ["hello", "hi", "hey"] for token in doc):
        return "Hello! How can I help you?"
    elif any(token.lemma_ in ["bye", "goodbye"] for token in doc):
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that."
    
print("🤖 AI Chatbot: Type 'exit' to stop.")
while True:
    user_input = input("👤 You: ")
    if user_input.lower() == "exit":
        print("🤖 Chatbot: Goodbye! 👋")
        break
    response = chatbot_response(user_input)
    print("🤖 Chatbot:", response)
