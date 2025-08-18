-defaultdict is a subclass of the built-in dict class. It overrides one method to provide a default value for a nonexistent key, which makes it particularly useful for grouping or counting items.


-frozenset is an immutable version of a set. Once created, its elements cannot be changed, which makes it useful for creating sets of items that should not be modified.


### Example of `defaultdict`

**Scenario**: Counting the occurrences of words in a list.

```python
from collections import defaultdict

# Sample list of words
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']

# Create a defaultdict to count occurrences
word_count = defaultdict(int)

# Count each word
for word in words:
    word_count[word] += 1

# Display the word counts
print(word_count)
# Output: defaultdict(<class 'int'>, {'apple': 2, 'banana': 3, 'orange': 1})
```

### Example of `frozenset`

**Scenario**: Using `frozenset` to represent unique combinations of items in a shopping cart.

```python
# Sample shopping carts
cart1 = frozenset(['apple', 'banana', 'orange'])
cart2 = frozenset(['banana', 'orange', 'grape'])
cart3 = frozenset(['apple', 'grape'])

# Store carts in a set to avoid duplicates
unique_carts = {cart1, cart2, cart3}

# Display unique shopping carts
for cart in unique_carts:
    print(cart)
# Output:
# frozenset({'banana', 'orange', 'apple'})
# frozenset({'grape', 'banana', 'orange'})
# frozenset({'grape', 'apple'})
```

### Summary

- In the first example, `defaultdict` simplifies counting words by automatically initializing counts.
- In the second example, `frozenset` allows us to create immutable sets of shopping carts, ensuring that each combination is unique and cannot be modified.