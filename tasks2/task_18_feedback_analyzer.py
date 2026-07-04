# Task 18: Customer Feedback Analyzer
# Topics: String functions, dictionaries, branching

POSITIVE_WORDS = ["good", "excellent", "nice", "happy", "satisfied", "great", "wonderful", "love", "best", "perfect"]
NEGATIVE_WORDS = ["bad", "poor", "late", "unhappy", "worst", "terrible", "awful", "horrible", "slow", "rude"]

def analyze_feedback(comment):
    comment_lower = comment.lower()
    pos_count = 0
    neg_count = 0

    for word in POSITIVE_WORDS:
        if word in comment_lower:
            pos_count += 1
    for word in NEGATIVE_WORDS:
        if word in comment_lower:
            neg_count += 1

    if pos_count > neg_count:
        sentiment = "Positive"
    elif neg_count > pos_count:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, pos_count, neg_count

def analyze_all_feedback(feedbacks):
    results   = []
    pos_total = 0
    neg_total = 0
    neu_total = 0

    for comment in feedbacks:
        sentiment, pos, neg = analyze_feedback(comment)
        results.append({"comment": comment, "sentiment": sentiment})
        if sentiment == "Positive":
            pos_total += 1
        elif sentiment == "Negative":
            neg_total += 1
        else:
            neu_total += 1

    return results, pos_total, neg_total, neu_total

def print_feedback_report(feedbacks):
    results, pos, neg, neu = analyze_all_feedback(feedbacks)
    print("=" * 55)
    print("    CUSTOMER FEEDBACK ANALYSIS REPORT")
    print("=" * 55)
    for i, r in enumerate(results, 1):
        print(f"  [{i}] {r['comment'][:40]:<42} -> {r['sentiment']}")
    print("-" * 55)
    print(f"  Positive: {pos}   Negative: {neg}   Neutral: {neu}")
    print("=" * 55)

# Test Section
if __name__ == "__main__":
    feedbacks = [
        "The service was excellent and staff was very nice!",
        "Very bad experience, delivery was late and poor quality.",
        "It was okay, nothing special.",
        "I am happy and satisfied with the product.",
        "Worst experience ever, terrible customer service.",
        "Good product and great value for money.",
        "The food was cold and the staff was rude.",
        "Delivery was quick and the item was perfect.",
    ]

    print("Test Case 1: Full Feedback Analysis")
    print_feedback_report(feedbacks)
    print()

    # Test Case 2: Single positive feedback
    s, p, n = analyze_feedback("Great service, very happy!")
    print(f"Test Case 2: Sentiment = {s} (pos={p}, neg={n})")

    # Test Case 3: Single neutral feedback
    s, p, n = analyze_feedback("The item arrived.")
    print(f"Test Case 3: Sentiment = {s} (pos={p}, neg={n})")
