def format_scores(names, scores):
    
    # create an empty list to collect formatted strings
    formatted = []
    for idx, (name, score) in enumerate(zip(names, scores), start=1):
        formatted.append(f"{idx}. {name} scored {score}")
    return formatted

# Example call (for testing)
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
result = format_scores(names, scores)
print(result)