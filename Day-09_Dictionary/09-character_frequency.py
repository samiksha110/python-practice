# Character Frequency

# Given:
# text = "apple"

# Print:
# a : 1
# p : 2
# l : 1
# e : 1

text = "apple"
freq = {}

for ch in text:
    if ch not in freq:
        freq[ch] = 1
    else:
        freq[ch] += 1

print(freq)

