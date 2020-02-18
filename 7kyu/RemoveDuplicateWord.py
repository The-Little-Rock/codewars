# Your task is to remove all duplicate words from a string, leaving only single (first) words entries.

# Example:
# Input:
# 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

# Output:
# 'alpha beta gamma delta'

# This is tricky because you need to preserve order even though the prompt doesn't tell you too.
# My implementation uses a dict to see if the word has already been seen in O(1) time, but adds them
# to an order list to preserve the order. Space is doubled though.
def remove_duplicate_words(s):
  wordsSeen = {}
  wordsSeenInOrder = []

  # Iterate each word, check if its been seen, if not, add it to seen, and append to ordered list
  for word in s.split(' '):
    if word not in wordsSeen:
      wordsSeen[word] = 1
      wordsSeenInOrder.append(word)

  return ' '.join(wordsSeenInOrder)

print(remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"), "alpha beta gamma delta")
print(remove_duplicate_words("my cat is my cat fat"), "my cat is fat")
