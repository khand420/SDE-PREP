# Group anagrams from a list of strings.
from collections import defaultdict
def group_anagrams(strs):
    anagrams = {}
    dfanagrams = defaultdict(list)

    for s in strs:
        key = ''.join(sorted(s))

        # if key in anagrams:
        #     anagrams[key].append(s)
        # else:
        #     anagrams[key] = [s]

        dfanagrams[key].append(s)



    return list(anagrams.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
grouped_anagrams = group_anagrams(words)

print(grouped_anagrams)
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]         



words = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']

# Create a defaultdict to count occurrences
word_count = defaultdict(int)
print(word_count)