from transformers import pipeline

print("   Text Recognition / Sentiment AI")

# Load pre-trained sentiment analysis model
classifier = pipeline("sentiment-analysis")

while True:
    text = input("\nEnter text (or type 'exit' to quit): ")

    if text.lower() == "exit":
        print("Program terminated.")
        break

    result = classifier(text)
    label = result[0]["label"]
    score = result[0]["score"]

    print("\nResult:")
    print(f"Sentiment : {label}")
    print(f"Confidence: {score * 100:.2f}%")