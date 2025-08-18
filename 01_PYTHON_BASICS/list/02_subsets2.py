from itertools import chain, combinations

def all_subsets(lst):
    # out = list(chain.from_iterable(combinations(lst, r) for r in range(len(lst)+1)))

    # out = [list(x) for x in out]    
    # print(out)
    return list(chain.from_iterable(combinations(lst, r) for r in range(len(lst)+1)))

# Example
lst = [1, 2, 3, 3]
print(all_subsets(lst))  # Output: [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]




# To calculate combinations from the list \([1, 2, 2]\) step by step using a systematic approach, we can follow these steps:

# ### Step 1: Identify Unique Elements and Their Frequencies

# From the list \([1, 2, 2]\):
# - Unique elements: 
#   - 1 (occurs 1 time)
#   - 2 (occurs 2 times)

# ### Step 2: Use the Multiset Combination Formula

# When dealing with combinations of a multiset (a set with repeated elements), we can use a combinatorial approach. The formula for combinations of a multiset is:

# \[
# C(n; k_1, k_2, \ldots, k_m) = \frac{n!}{k_1! \cdot k_2! \cdots k_m!}
# \]

# Where:
# - \( n \) is the total number of items,
# - \( k_1, k_2, \ldots, k_m \) are the frequencies of the unique items.

# ### Step 3: Calculate Combinations for Different Sizes

# Let's calculate for different sizes of combinations \( r \) (1, 2, and 3).

# #### 1. **1-element Combinations** (\( r = 1 \))

# Choosing 1 element from \([1, 2, 2]\):
# - Unique combinations: \([1]\), \([2]\)

# Total unique combinations: **2**

# #### 2. **2-element Combinations** (\( r = 2 \))

# Choosing 2 elements:
# - Possible selections:
#   - From 1 and 2: \([1, 2]\)
#   - From 2 and 2: \([2, 2]\)

# Total unique combinations: **2** (i.e., \([1, 2]\) and \([2, 2]\))

# #### 3. **3-element Combination** (\( r = 3 \))

# Choosing all 3 elements:
# - Only combination: \([1, 2, 2]\)

# Total unique combinations: **1**

# ### Step 4: Summarize All Unique Combinations

# Now, we summarize the results:
# - 1-element combinations: \([1]\), \([2]\) → **2 combinations**
# - 2-element combinations: \([1, 2]\), \([2, 2]\) → **2 combinations**
# - 3-element combination: \([1, 2, 2]\) → **1 combination**

# ### Final Count of Unique Combinations

# Combining all the unique combinations:
# - Total unique combinations = \( 2 + 2 + 1 = 5 \)

# ### Summary of Unique Combinations
# The unique combinations from the list \([1, 2, 2]\) are:
# 1. \([1]\)
# 2. \([2]\)
# 3. \([1, 2]\)
# 4. \([2, 2]\)
# 5. \([1, 2, 2]\)

# Thus, the final answer is **5 unique combinations**.