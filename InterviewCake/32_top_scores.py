def sort_scores(scores, high_score):
    counter = [0] * (high_score + 1)
    sorted_scores = []
    for score in scores:
        counter[score] += 1
    for score, occurances in enumerate(counter):
        for _ in range(occurances):
            sorted_scores.append(score)
    return sorted_scores

scores = [2, 12, 21, 12, 4, 42, 1, 24, 12, 21, 12, 3, 1, 32, 13, 2, 3, 21, 3, 21]
high_score = 100
print(sort_scores(scores, high_score))
