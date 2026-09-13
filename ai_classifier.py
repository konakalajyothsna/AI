from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

message = input("Enter an issue:")

categories = {
    "Billing issue": "refund payment charge card invoice billing money transaction",
    "Login issue": "login password sign in account access authentication",
    "General issue": "general help question support request other problem",
    "Delivery issue": "delivery shipment package tracking order arrived shipping"
}

message_vector = model.encode(message)
category_vectors = model.encode(list(categories.values()))

scores = model.similarity(message_vector, category_vectors)[0]

for category, score in zip(categories.keys(), scores):
    print(category, round(score.item(), 3))

best_index = scores.argmax().item()
best_category = list(categories.keys())[best_index]

print("Message:", message)
print("Prediction:", best_category)
print("Score:", round(scores[best_index].item(), 3))