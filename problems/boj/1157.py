from collections import Counter

def most_common_letter():
    word = input().upper()
    counter = Counter(word)
    most_common = counter.most_common()
    max_common = most_common[0][1]
    most_freq = [char for char, count in most_common if count == max_common]

    if len(most_freq) > 1:
        return '?'
    else:
        return most_freq[0]

print(most_common_letter())
