# Find the Most Frequent Character

text = "banana"

freq = {}

for ch in text:
    if ch not in freq:
        freq[ch] = 1
    else:
        freq[ch] += 1

# Initialize using the first item
for key, value in freq.items():
    max_char = key
    max_count = value
    break

# Find the maximum
for key, value in freq.items():
    if value > max_count:
        max_count = value
        max_char = key

print(max_char)
