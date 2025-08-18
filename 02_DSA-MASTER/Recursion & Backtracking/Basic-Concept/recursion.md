Recursion is a powerful concept in programming, and it’s often used in problems that involve repetitive tasks, breaking down problems into smaller sub-problems. Below are common questions related to recursion, along with brief explanations for each one.

### 1. **Factorial of a Number**

* **Problem**: Find the factorial of a given number $n$, i.e., $n!$.

  * **Example**: $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$
* **Recursive Solution**:

  ```python
  def factorial(n):
      if n == 0:
          return 1
      return n * factorial(n-1)
  ```

---

### 2. **Fibonacci Sequence**

* **Problem**: Calculate the $n^{th}$ Fibonacci number. The Fibonacci sequence is defined as:

  $$
  F(0) = 0, \quad F(1) = 1, \quad F(n) = F(n-1) + F(n-2) \text{ for } n \geq 2
  $$

* **Recursive Solution**:

  ```python
  def fibonacci(n):
      if n == 0:
          return 0
      elif n == 1:
          return 1
      return fibonacci(n-1) + fibonacci(n-2)
  ```

---

### 3. **Sum of Natural Numbers**

* **Problem**: Find the sum of the first $n$ natural numbers.

  * **Formula**: $\text{Sum}(n) = n + (n-1) + (n-2) + \dots + 1$
* **Recursive Solution**:

  ```python
  def sum_of_n(n):
      if n == 0:
          return 0
      return n + sum_of_n(n-1)
  ```

---

### 4. **Power of a Number**

* **Problem**: Compute $x^n$ (x raised to the power of n) recursively.

  * **Example**: $2^3 = 8$
* **Recursive Solution**:

  ```python
  def power(x, n):
      if n == 0:
          return 1
      return x * power(x, n-1)
  ```

---

### 5. **Reverse a String**

* **Problem**: Reverse a string recursively.

  * **Example**: `"hello"` -> `"olleh"`
* **Recursive Solution**:

  ```python
  def reverse_string(s):
      if len(s) == 0:
          return s
      return reverse_string(s[1:]) + s[0]
  ```

---

### 6. **Check if a String is Palindrome**

* **Problem**: Check if a given string is a palindrome (reads the same backward as forward).

  * **Example**: `"madam"` -> True, `"hello"` -> False
* **Recursive Solution**:

  ```python
  def is_palindrome(s):
      if len(s) <= 1:
          return True
      if s[0] != s[-1]:
          return False
      return is_palindrome(s[1:-1])
  ```

---

### 7. **Tower of Hanoi**

* **Problem**: Solve the Tower of Hanoi puzzle. The goal is to move a set of disks from one rod to another, following these rules:

  * Only one disk can be moved at a time.
  * Each move consists of taking the upper disk from one stack and placing it on top of another stack.
  * A disk may only be placed on top of a larger disk.

* **Recursive Solution**:

  ```python
  def tower_of_hanoi(n, source, target, auxiliary):
      if n == 1:
          print(f"Move disk 1 from {source} to {target}")
          return
      tower_of_hanoi(n-1, source, auxiliary, target)
      print(f"Move disk {n} from {source} to {target}")
      tower_of_hanoi(n-1, auxiliary, target, source)
  ```

---

### 8. **Find the Greatest Common Divisor (GCD)**

* **Problem**: Find the greatest common divisor of two numbers $a$ and $b$ using recursion (Euclid's algorithm).

  * **Example**: $\text{gcd}(48, 18) = 6$
* **Recursive Solution**:

  ```python
  def gcd(a, b):
      if b == 0:
          return a
      return gcd(b, a % b)
  ```

---

### 9. **Count the Number of Digits in a Number**

* **Problem**: Count the number of digits in a given number $n$.

  * **Example**: $12345$ has 5 digits.
* **Recursive Solution**:

  ```python
  def count_digits(n):
      if n == 0:
          return 0
      return 1 + count_digits(n // 10)
  ```

---

### 10. **Find All Permutations of a String**

* **Problem**: Find all the permutations of a given string.

  * **Example**: `"abc"` -> `["abc", "acb", "bac", "bca", "cab", "cba"]`
* **Recursive Solution**:

  ```python
  def permute(s):
      if len(s) == 0:
          return ['']
      result = []
      for i in range(len(s)):
          char = s[i]
          remaining = s[:i] + s[i+1:]
          for perm in permute(remaining):
              result.append(char + perm)
      return result
  ```

---

### 11. **Print All Subsets of a Set**

* **Problem**: Print all subsets of a set (including the empty set).

  * **Example**: Set `{1, 2, 3}` -> `[[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]`
* **Recursive Solution**:

  ```python
  def subsets(s):
      if len(s) == 0:
          return [[]]
      first = s[0]
      rest_subsets = subsets(s[1:])
      return rest_subsets + [[first] + subset for subset in rest_subsets]
  ```

---

### 12. **Find the Length of a List**

* **Problem**: Find the length of a given list using recursion.

  * **Example**: `[1, 2, 3, 4]` has length 4.
* **Recursive Solution**:

  ```python
  def list_length(lst):
      if not lst:
          return 0
      return 1 + list_length(lst[1:])
  ```

---

### 13. **Merge Sort**

* **Problem**: Sort an array using the Merge Sort algorithm, which uses recursion to divide the array into smaller sub-arrays and then merge them back in sorted order.

* **Recursive Solution**:

  ```python
  def merge_sort(arr):
      if len(arr) <= 1:
          return arr
      mid = len(arr) // 2
      left = merge_sort(arr[:mid])
      right = merge_sort(arr[mid:])
      return merge(left, right)

  def merge(left, right):
      result = []
      while left and right:
          if left[0] < right[0]:
              result.append(left.pop(0))
          else:
              result.append(right.pop(0))
      result.extend(left or right)
      return result
  ```

---

### 14. **Quick Sort**

* **Problem**: Sort an array using the Quick Sort algorithm.

* **Recursive Solution**:

  ```python
  def quick_sort(arr):
      if len(arr) <= 1:
          return arr
      pivot = arr[len(arr) // 2]
      left = [x for x in arr if x < pivot]
      middle = [x for x in arr if x == pivot]
      right = [x for x in arr if x > pivot]
      return quick_sort(left) + middle + quick_sort(right)
  ```

---

### 15. **Flatten a Nested List**

* **Problem**: Flatten a list that may contain nested lists into a single list.

  * **Example**: `[[1, 2], 3, [4, [5, 6]], 7]` -> `[1, 2, 3, 4, 5, 6, 7]`
* **Recursive Solution**:

  ```python
  def flatten(lst):
      result = []
      for item in lst:
          if isinstance(item, list):
              result.extend(flatten(item))
          else:
              result.append(item)
      return result
  ```

---

### 16. **Find the Maximum Element in a List**

* **Problem**: Find the largest element in a list using recursion.

* **Recursive Solution**:

  ```python
  def find_max(lst):
      if len(lst) == 1:
          return lst[0]
      max_in_rest = find_max(lst[1:])
      return max(lst[0], max_in_rest)
  ```

---

### 17. **Generate All Binary Strings of Length N**

* **Problem**: Generate all binary strings of length $n$, where each digit can either be `0` or `1`.

* **Recursive Solution**:


```python
 def generate_binary_strings(n):
     if n == 0:
         return ['']
     smaller_strings = generate_binary_strings(n-1)
     return ['0' + s for s in smaller_strings] + ['1' + s for s in smaller_strings]
```


---

### 18. **Find All Subsequences of a String**

* **Problem**: Find all subsequences of a string (subsets without reordering).

  * **Example**: For `"abc"`, the subsequences are `["", "a", "b", "c", "ab", "ac", "bc", "abc"]`.
* **Recursive Solution**:

  ```python
  def subsequences(s):
      if len(s) == 0:
          return ['']
      first = s[0]
      rest = s[1:]
      subseq_rest = subsequences(rest)
      return subseq_rest + [first + sub for sub in subseq_rest]
  ```

---

### 19. **Power Set of a Set (All Possible Subsets)**

* **Problem**: Given a set of numbers, return all possible subsets (also called the power set).

  * **Example**: `{1, 2}` → `[[], [1], [2], [1, 2]]`
* **Recursive Solution**:

  ```python
  def power_set(s):
      if len(s) == 0:
          return [[]]
      first = s[0]
      rest = s[1:]
      rest_subsets = power_set(rest)
      return rest_subsets + [[first] + subset for subset in rest_subsets]
  ```

---

### 20. **Find the Path from Root to Leaf in a Binary Tree**

* **Problem**: Given a binary tree, find the path from the root to all the leaf nodes.

  * **Example**: For a tree with root `1` and children `2` and `3`, leaf paths would be `[1 -> 2]`, `[1 -> 3]`.
* **Recursive Solution**:

  ```python
  class TreeNode:
      def __init__(self, value=0, left=None, right=None):
          self.value = value
          self.left = left
          self.right = right

  def root_to_leaf_paths(root):
      if root is None:
          return []
      if root.left is None and root.right is None:
          return [[root.value]]
      paths = []
      if root.left:
          left_paths = root_to_leaf_paths(root.left)
          for path in left_paths:
              paths.append([root.value] + path)
      if root.right:
          right_paths = root_to_leaf_paths(root.right)
          for path in right_paths:
              paths.append([root.value] + path)
      return paths
  ```

---

### 21. **Find the Lowest Common Ancestor (LCA) in a Binary Tree**

* **Problem**: Find the lowest common ancestor of two nodes in a binary tree.

  * **Example**: In the binary tree:

    ```
        3
       / \
      5   1
     / \ / \
    6  2 0  8
       / \
      7   4
    ```

    LCA of nodes 5 and 1 is `3`, and LCA of nodes 5 and 4 is `5`.
* **Recursive Solution**:

  ```python
  class TreeNode:
      def __init__(self, value=0, left=None, right=None):
          self.value = value
          self.left = left
          self.right = right

  def lowest_common_ancestor(root, p, q):
      if not root or root == p or root == q:
          return root
      left = lowest_common_ancestor(root.left, p, q)
      right = lowest_common_ancestor(root.right, p, q)
      if left and right:
          return root
      return left if left else right
  ```

---

### 22. **Merge Two Sorted Linked Lists**

* **Problem**: Given two sorted linked lists, merge them into one sorted linked list.

* **Recursive Solution**:

  ```python
  class ListNode:
      def __init__(self, val=0, next=None):
          self.val = val
          self.next = next

  def merge_two_lists(l1, l2):
      if not l1:
          return l2
      if not l2:
          return l1
      if l1.val < l2.val:
          l1.next = merge_two_lists(l1.next, l2)
          return l1
      else:
          l2.next = merge_two_lists(l1, l2.next)
          return l2
  ```

---

### 23. **Permutations of a String with Duplicates**

* **Problem**: Find all unique permutations of a string that may contain duplicates.

  * **Example**: For `"aab"`, the output should be `["aab", "aba", "baa"]`.
* **Recursive Solution**:

  ```python
  def permutations_with_duplicates(s):
      if len(s) == 0:
          return [""]
      res = []
      for i in range(len(s)):
          if i > 0 and s[i] == s[i-1]:
              continue
          rest = s[:i] + s[i+1:]
          for perm in permutations_with_duplicates(rest):
              res.append(s[i] + perm)
      return res
  ```

---

### 24. **Flatten a Binary Tree to a Linked List**

* **Problem**: Flatten a binary tree to a linked list in place using preorder traversal.

  * **Example**: A tree:

    ```
        1
       / \
      2   5
     / \   \
    3   4   6
    ```

    Should be flattened to:

    ```
    1 -> 2 -> 3 -> 4 -> 5 -> 6
    ```

* **Recursive Solution**:

  ```python
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

  def flatten(root):
      if not root:
          return None
      if not root.left and not root.right:
          return root
      left_tail = flatten(root.left)
      right_tail = flatten(root.right)
      if root.left:
          left_tail.right = root.right
          root.right = root.left
          root.left = None
      return right_tail if right_tail else left_tail
  ```

---

### 25. **Longest Common Subsequence (LCS)**

* **Problem**: Given two strings, find the length of the longest common subsequence (LCS). LCS is the longest subsequence that appears in both strings in the same order.

* **Recursive Solution**:

  ```python
  def longest_common_subsequence(s1, s2, m, n):
      if m == 0 or n == 0:
          return 0
      if s1[m-1] == s2[n-1]:
          return 1 + longest_common_subsequence(s1, s2, m-1, n-1)
      else:
          return max(longest_common_subsequence(s1, s2, m-1, n), longest_common_subsequence(s1, s2, m, n-1))
  ```

---

### 26. **K-th Smallest Element in a BST**

* **Problem**: Find the K-th smallest element in a Binary Search Tree (BST).

* **Recursive Solution**:

  ```python
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

  def kth_smallest(root, k):
      stack = []
      while True:
          while root:
              stack.append(root)
              root = root.left
          root = stack.pop()
          k -= 1
          if k == 0:
              return root.val
          root = root.right
  ```

---

### 27. **Combinations**

* **Problem**: Given two integers $n$ and $k$, return all possible combinations of $k$ numbers chosen from 1 to $n$.

  * **Example**: For $n = 4$ and $k = 2$, the output should be `[[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]`.
* **Recursive Solution**:

  ```python
  def combine(n, k):
      res = []
      def backtrack(start, path):
          if len(path) == k:
              res.append(path[:])
              return
          for i in range(start, n + 1):
              path.append(i)
              backtrack(i + 1, path)
              path.pop()
      backtrack(1, [])
      return res
  ```

---

### 28. **N-Queens Problem**

* **Problem**: Place N queens on an N×N chessboard so that no two queens attack each other. Return all distinct solutions.

* **Recursive Solution**:

  ```python
  def solve_n_queens(n):
      def is_safe(board, row, col):
          for i in range(row):
              if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                  return False
          return True

      def solve(board, row):
          if row == n:
              result
  ```


.append(\['.' \* i + 'Q' + '.' \* (n - i - 1) for i in board])
return
for col in range(n):
if is\_safe(board, row, col):
board\[row] = col
solve(board, row + 1)
board\[row] = -1

```
  result = []
  solve([-1] * n, 0)
  return result
```

```

---


Absolutely! Here are **more important recursion-based problems**, some of which are commonly asked in technical interviews and coding challenges. These problems will test your ability to use recursion effectively and understand how to break down complex problems into simpler sub-problems.

---

### 18. **Find All Subsequences of a String**

* **Problem**: Find all subsequences of a string (subsets without reordering).

  * **Example**: For `"abc"`, the subsequences are `["", "a", "b", "c", "ab", "ac", "bc", "abc"]`.
* **Recursive Solution**:

  ```python
  def subsequences(s):
      if len(s) == 0:
          return ['']
      first = s[0]
      rest = s[1:]
      subseq_rest = subsequences(rest)
      return subseq_rest + [first + sub for sub in subseq_rest]
  ```

---

### 19. **Power Set of a Set (All Possible Subsets)**

* **Problem**: Given a set of numbers, return all possible subsets (also called the power set).

  * **Example**: `{1, 2}` → `[[], [1], [2], [1, 2]]`
* **Recursive Solution**:

  ```python
  def power_set(s):
      if len(s) == 0:
          return [[]]
      first = s[0]
      rest = s[1:]
      rest_subsets = power_set(rest)
      return rest_subsets + [[first] + subset for subset in rest_subsets]
  ```

---

### 20. **Find the Path from Root to Leaf in a Binary Tree**

* **Problem**: Given a binary tree, find the path from the root to all the leaf nodes.

  * **Example**: For a tree with root `1` and children `2` and `3`, leaf paths would be `[1 -> 2]`, `[1 -> 3]`.
* **Recursive Solution**:

  ```python
  class TreeNode:
      def __init__(self, value=0, left=None, right=None):
          self.value = value
          self.left = left
          self.right = right

  def root_to_leaf_paths(root):
      if root is None:
          return []
      if root.left is None and root.right is None:
          return [[root.value]]
      paths = []
      if root.left:
          left_paths = root_to_leaf_paths(root.left)
          for path in left_paths:
              paths.append([root.value] + path)
      if root.right:
          right_paths = root_to_leaf_paths(root.right)
          for path in right_paths:
              paths.append([root.value] + path)
      return paths
  ```

---

### 21. **Find the Lowest Common Ancestor (LCA) in a Binary Tree**

* **Problem**: Find the lowest common ancestor of two nodes in a binary tree.

  * **Example**: In the binary tree:

    ```
        3
       / \
      5   1
     / \ / \
    6  2 0  8
       / \
      7   4
    ```

    LCA of nodes 5 and 1 is `3`, and LCA of nodes 5 and 4 is `5`.
* **Recursive Solution**:

  ```python
  class TreeNode:
      def __init__(self, value=0, left=None, right=None):
          self.value = value
          self.left = left
          self.right = right

  def lowest_common_ancestor(root, p, q):
      if not root or root == p or root == q:
          return root
      left = lowest_common_ancestor(root.left, p, q)
      right = lowest_common_ancestor(root.right, p, q)
      if left and right:
          return root
      return left if left else right
  ```

---

### 22. **Merge Two Sorted Linked Lists**

* **Problem**: Given two sorted linked lists, merge them into one sorted linked list.

* **Recursive Solution**:

  ```python
  class ListNode:
      def __init__(self, val=0, next=None):
          self.val = val
          self.next = next

  def merge_two_lists(l1, l2):
      if not l1:
          return l2
      if not l2:
          return l1
      if l1.val < l2.val:
          l1.next = merge_two_lists(l1.next, l2)
          return l1
      else:
          l2.next = merge_two_lists(l1, l2.next)
          return l2
  ```

---

### 23. **Permutations of a String with Duplicates**

* **Problem**: Find all unique permutations of a string that may contain duplicates.

  * **Example**: For `"aab"`, the output should be `["aab", "aba", "baa"]`.
* **Recursive Solution**:

  ```python
  def permutations_with_duplicates(s):
      if len(s) == 0:
          return [""]
      res = []
      for i in range(len(s)):
          if i > 0 and s[i] == s[i-1]:
              continue
          rest = s[:i] + s[i+1:]
          for perm in permutations_with_duplicates(rest):
              res.append(s[i] + perm)
      return res
  ```

---

### 24. **Flatten a Binary Tree to a Linked List**

* **Problem**: Flatten a binary tree to a linked list in place using preorder traversal.

  * **Example**: A tree:

    ```
        1
       / \
      2   5
     / \   \
    3   4   6
    ```

    Should be flattened to:

    ```
    1 -> 2 -> 3 -> 4 -> 5 -> 6
    ```

* **Recursive Solution**:

  ```python
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

  def flatten(root):
      if not root:
          return None
      if not root.left and not root.right:
          return root
      left_tail = flatten(root.left)
      right_tail = flatten(root.right)
      if root.left:
          left_tail.right = root.right
          root.right = root.left
          root.left = None
      return right_tail if right_tail else left_tail
  ```

---

### 25. **Longest Common Subsequence (LCS)**

* **Problem**: Given two strings, find the length of the longest common subsequence (LCS). LCS is the longest subsequence that appears in both strings in the same order.

* **Recursive Solution**:

  ```python
  def longest_common_subsequence(s1, s2, m, n):
      if m == 0 or n == 0:
          return 0
      if s1[m-1] == s2[n-1]:
          return 1 + longest_common_subsequence(s1, s2, m-1, n-1)
      else:
          return max(longest_common_subsequence(s1, s2, m-1, n), longest_common_subsequence(s1, s2, m, n-1))
  ```

---

### 26. **K-th Smallest Element in a BST**

* **Problem**: Find the K-th smallest element in a Binary Search Tree (BST).

* **Recursive Solution**:

  ```python
  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

  def kth_smallest(root, k):
      stack = []
      while True:
          while root:
              stack.append(root)
              root = root.left
          root = stack.pop()
          k -= 1
          if k == 0:
              return root.val
          root = root.right
  ```

---

### 27. **Combinations**

* **Problem**: Given two integers $n$ and $k$, return all possible combinations of $k$ numbers chosen from 1 to $n$.

  * **Example**: For $n = 4$ and $k = 2$, the output should be `[[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]`.
* **Recursive Solution**:

  ```python
  def combine(n, k):
      res = []
      def backtrack(start, path):
          if len(path) == k:
              res.append(path[:])
              return
          for i in range(start, n + 1):
              path.append(i)
              backtrack(i + 1, path)
              path.pop()
      backtrack(1, [])
      return res
  ```

---

### 28. **N-Queens Problem**

* **Problem**: Place N queens on an N×N chessboard so that no two queens attack each other. Return all distinct solutions.

* **Recursive Solution**:

  ```python
  def solve_n_queens(n):
      def is_safe(board, row, col):
          for i in range(row):
              if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                  return False
          return True

      def solve(board, row):
          if row == n:
            result.append(\['.' \* i + 'Q' + '.' \* (n - i - 1) for i in board])
            return
            for col in range(n):
                if is\_safe(board, row, col):
                    board\[row] = col
                    solve(board, row + 1)
                    board\[row] = -1

    result = []
    solve([-1] * n, 0)
    return result
  ```



---

### 29. **Balanced Parentheses**

* **Problem**: Given a number `n`, generate all combinations of valid parentheses that can be formed with `n` pairs.

  * **Example**: For `n = 3`, the output should be `["((()))", "(()())", "(())()", "()(())", "()()()"]`.
* **Recursive Solution**:

 ```python
  def generate_parentheses(n):
      def backtrack(current, open_count, close_count):
          if len(current) == 2 * n:
              res.append(current)
              return
          if open_count < n:
              backtrack(current + "(", open_count + 1, close_count)
          if close_count < open_count:
              backtrack(current + ")", open_count, close_count + 1)

      res = []
      backtrack("", 0, 0)
      return res

 ```

---

### 30. **Sudoku Solver**

* **Problem**: Solve a 9x9 Sudoku puzzle using recursion. You need to fill the board such that every row, every column, and every 3x3 subgrid contain digits from 1 to 9.

* **Recursive Solution**:

  ```python
  def solve_sudoku(board):
      def is_valid(board, row, col, num):
          for i in range(9):
              if board[row][i] == num or board[i][col] == num:
                  return False
          start_row, start_col = 3 * (row // 3), 3 * (col // 3)
          for i in range(start_row, start_row + 3):
              for j in range(start_col, start_col + 3):
                  if board[i][j] == num:
                      return False
          return True

      def solve(board):
          for i in range(9):
              for j in range(9):
                  if board[i][j] == '.':
                      for num in '123456789':
                          if is_valid(board, i, j, num):
                              board[i][j] = num
                              if solve(board):
                                  return True
                              board[i][j] = '.'
                      return False
          return True

      solve(board)
  ```

---

### 31. **Climbing Stairs**

* **Problem**: You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb 1 or 2 steps. How many distinct ways can you reach the top?

  * **Example**: For `n = 3`, the output should be `3`, because there are 3 ways to climb the stairs: `1+1+1`, `1+2`, and `2+1`.
* **Recursive Solution**:

  ```python
  def climb_stairs(n):
      if n <= 2:
          return n
      return climb_stairs(n - 1) + climb_stairs(n - 2)
  ```

---

### 32. **Nth Ugly Number**

* **Problem**: Ugly numbers are numbers whose prime factors only include `2, 3, or 5`. Find the `n`-th ugly number.

* **Recursive Solution**:

  ```python
  def nth_ugly_number(n):
      ugly_numbers = [1]
      i2, i3, i5 = 0, 0, 0
      next_2, next_3, next_5 = 2, 3, 5
      for i in range(1, n):
          next_ugly = min(next_2, next_3, next_5)
          ugly_numbers.append(next_ugly)
          if next_ugly == next_2:
              i2 += 1
              next_2 = ugly_numbers[i2] * 2
          if next_ugly == next_3:
              i3 += 1
              next_3 = ugly_numbers[i3] * 3
          if next_ugly == next_5:
              i5 += 1
              next_5 = ugly_numbers[i5] * 5
      return ugly_numbers[-1]
  ```

---

### 33. **Permutations of an Array**

* **Problem**: Given an array of integers, return all possible permutations.

* **Recursive Solution**:

  ```python
  def permute(nums):
      def backtrack(start, end):
          if start == end:
              res.append(nums[:])
          for i in range(start, end):
              nums[start], nums[i] = nums[i], nums[start]
              backtrack(start + 1, end)
              nums[start], nums[i] = nums[i], nums[start]

      res = []
      backtrack(0, len(nums))
      return res
  ```

---

### 34. **Find All Anagrams in a String**

* **Problem**: Given a string, find all the start indices of the substrings that are anagrams of a given pattern.

* **Recursive Solution**:

  ```python
  from collections import Counter

  def find_anagrams(s, p):
      res = []
      p_count = Counter(p)
      s_count = Counter()
      for i in range(len(s)):
          s_count[s[i]] += 1
          if i >= len(p):
              if s_count[s[i - len(p)]] == 1:
                  del s_count[s[i - len(p)]]
              else:
                  s_count[s[i - len(p)]] -= 1
          if s_count == p_count:
              res.append(i - len(p) + 1)
      return res
  ```

---

### 35. **Longest Palindromic Substring**

* **Problem**: Given a string, find the longest palindromic substring.

* **Recursive Solution**:

  ```python
  def longest_palindromic_substring(s):
      def expand_around_center(left, right):
          while left >= 0 and right < len(s) and s[left] == s[right]:
              left -= 1
              right += 1
          return s[left + 1:right]

      result = ""
      for i in range(len(s)):
          odd_palindrome = expand_around_center(i, i)
          even_palindrome = expand_around_center(i, i + 1)
          result = max(result, odd_palindrome, even_palindrome, key=len)
      return result
  ```

---

### 36. **Count the Number of Islands**

* **Problem**: Given a 2D grid map of `'1'`s (land) and `'0'`s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

* **Recursive Solution**:

  ```python
  def num_islands(grid):
      def dfs(i, j):
          if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
              return
          grid[i][j] = '0'  # Mark as visited
          dfs(i + 1, j)
          dfs(i - 1, j)
          dfs(i, j + 1)
          dfs(i, j - 1)

      if not grid:
          return 0

      count = 0
      for i in range(len(grid)):
          for j in range(len(grid[0])):
              if grid[i][j] == '1':
                  count += 1
                  dfs(i, j)
      return count
  ```

---

### 37. **Word Search in a Board**

* **Problem**: Given a 2D board of characters and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.

* **Recursive Solution**:

  ```python
  def exist(board, word):
      def backtrack(i, j, index):
          if index == len(word):
              return True
          if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
              return False
          temp, board[i][j] = board[i][j], '#'
          res = (backtrack(i + 1, j, index + 1) or
                 backtrack(i - 1, j, index + 1) or
                 backtrack(i, j + 1, index + 1) or
                 backtrack(i, j - 1, index + 1))
          board[i][j] = temp
          return res

      for i in range(len(board)):
          for j in range(len(board[0])):
              if backtrack(i, j, 0):
                  return True
      return False
  ```

---

### 38. **Matrix Multiplication**

* **Problem**: Multiply two matrices using recursion. This is typically done through divide and conquer or recursive matrix multiplication algorithms like Strassen's algorithm.

* **Recursive Solution**:
  (Note: Full recursive matrix multiplication is advanced and often involves breaking the matrix into smaller submatrices)

  ```python
  def matrix_multiply(A, B):
      def add_matrices(A, B):
          return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range
  ```


(len(A))]

```python
  def multiply(A, B):
      # Base case: 1x1 matrices
      if len(A) == 1 and len(A[0]) == 1:
          return [[A[0][0] * B[0][0]]]

      # Divide matrices into quadrants and recurse
      mid = len(A) // 2
      A11, A12, A21, A22 = A[:mid][:mid], A[:mid][mid:], A[mid:][:mid], A[mid:][mid:]
      B11, B12, B21, B22 = B[:mid][:mid], B[:mid][mid:], B[mid:][:mid], B[mid:][mid:]

      # Recursive calls and combining
      C11 = add_matrices(multiply(A11, B11), multiply(A12, B21))
      C12 = add_matrices(multiply(A11, B12), multiply(A12, B22))
      C21 = add_matrices(multiply(A21, B11), multiply(A22, B21))
      C22 = add_matrices(multiply(A21, B12), multiply(A22, B22))

      return C11 + C12 + C21 + C22
```


---

### 39. **Largest Sum Contiguous Subarray (Kadane's Algorithm)**
- **Problem**: Find the contiguous subarray within a 1D array of numbers that has the largest sum.

- **Recursive Solution**:
```python
def max_subarray_sum(nums):
    def helper(index, current_sum, max_sum):
        if index == len(nums):
            return max_sum
        current_sum = max(nums[index], current_sum + nums[index])
        max_sum = max(max_sum, current_sum)
        return helper(index + 1, current_sum, max_sum)
    
    return helper(0, 0, float('-inf'))
```


Here are **more recursion problems** that span a range of difficulty levels, focusing on both common algorithms and more unique problem-solving scenarios:

---

### 40. **Jump Game**

* **Problem**: You are given an array `nums` where `nums[i]` represents your maximum jump length from that position. Determine if you can reach the last index.

* **Recursive Solution**:

  ```python
  def can_jump(nums):
      def jump(index):
          if index >= len(nums) - 1:
              return True
          max_jump = nums[index]
          for i in range(1, max_jump + 1):
              if jump(index + i):
                  return True
          return False
      
      return jump(0)
  ```

---

### 41. **Reverse a Linked List**

* **Problem**: Reverse a singly linked list using recursion.

* **Recursive Solution**:

  ```python
  class ListNode:
      def __init__(self, val=0, next=None):
          self.val = val
          self.next = next

  def reverse_linked_list(head):
      if not head or not head.next:
          return head
      reversed_list = reverse_linked_list(head.next)
      head.next.next = head
      head.next = None
      return reversed_list
  ```

---

### 42. **Find the Missing Number**

* **Problem**: Given an array of numbers from 1 to n with one number missing, find the missing number.

* **Recursive Solution**:

  ```python
  def find_missing_number(nums, n, index=0):
      if index == n:
          return n
      if nums[index] != index + 1:
          return index + 1
      return find_missing_number(nums, n, index + 1)
  ```

---

### 43. **Merge Sort**

* **Problem**: Implement merge sort using recursion. The algorithm should split the array into halves, recursively sort each half, and merge them back together.

* **Recursive Solution**:

  ```python
  def merge_sort(arr):
      if len(arr) <= 1:
          return arr
      mid = len(arr) // 2
      left = merge_sort(arr[:mid])
      right = merge_sort(arr[mid:])
      return merge(left, right)

  def merge(left, right):
      result = []
      i = j = 0
      while i < len(left) and j < len(right):
          if left[i] < right[j]:
              result.append(left[i])
              i += 1
          else:
              result.append(right[j])
              j += 1
      result.extend(left[i:])
      result.extend(right[j:])
      return result
  ```

---

### 44. **Quick Sort**

* **Problem**: Implement quick sort using recursion. The algorithm should choose a pivot element and recursively sort the left and right parts of the list.

* **Recursive Solution**:

  ```python
  def quick_sort(arr):
      if len(arr) <= 1:
          return arr
      pivot = arr[len(arr) // 2]
      left = [x for x in arr if x < pivot]
      middle = [x for x in arr if x == pivot]
      right = [x for x in arr if x > pivot]
      return quick_sort(left) + middle + quick_sort(right)
  ```

---

### 45. **Count Total Paths in a Grid**

* **Problem**: Given an `m x n` grid, find the total number of unique paths from the top-left corner to the bottom-right corner, only moving down or right.

* **Recursive Solution**:

  ```python
  def unique_paths(m, n):
      if m == 1 or n == 1:
          return 1
      return unique_paths(m - 1, n) + unique_paths(m, n - 1)
  ```

---

### 46. **Subset Sum Problem**

* **Problem**: Given a set of numbers, determine if there is a subset whose sum is equal to a given number `target`.

* **Recursive Solution**:

  ```python
  def subset_sum(nums, target, index=0):
      if target == 0:
          return True
      if index == len(nums) or target < 0:
          return False
      return subset_sum(nums, target - nums[index], index + 1) or subset_sum(nums, target, index + 1)
  ```

---

### 47. **N-Queens II (Count All Solutions)**

* **Problem**: Solve the N-Queens problem but only return the number of distinct solutions, rather than the solutions themselves.

* **Recursive Solution**:

  ```python
  def total_n_queens(n):
      def solve(board, row):
          if row == n:
              return 1
          count = 0
          for col in range(n):
              if is_safe(board, row, col):
                  board[row] = col
                  count += solve(board, row + 1)
                  board[row] = -1
          return count

      def is_safe(board, row, col):
          for i in range(row):
              if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                  return False
          return True

      board = [-1] * n
      return solve(board, 0)
  ```

---

### 48. **Find All Unique Combinations**

* **Problem**: Given a set of candidate numbers (which may contain duplicates) and a target number, find all unique combinations of candidates that sum to the target.

* **Recursive Solution**:

  ```python
  def combination_sum2(candidates, target):
      def backtrack(start, path, target):
          if target == 0:
              res.append(path[:])
              return
          for i in range(start, len(candidates)):
              if i > start and candidates[i] == candidates[i - 1]:
                  continue
              if candidates[i] > target:
                  break
              path.append(candidates[i])
              backtrack(i + 1, path, target - candidates[i])
              path.pop()

      res = []
      candidates.sort()
      backtrack(0, [], target)
      return res
  ```

---

### 49. **Word Ladder**

* **Problem**: Given two words (beginWord and endWord) and a dictionary, find the length of the shortest transformation sequence from beginWord to endWord, such that only one letter can be changed at a time and each transformed word must exist in the dictionary.

* **Recursive Solution**:

  ```python
  from collections import deque

  def word_ladder(beginWord, endWord, wordList):
      if endWord not in wordList:
          return 0
      wordList = set(wordList)
      queue = deque([(beginWord, 1)])

      def can_transform(word1, word2):
          diff = 0
          for a, b in zip(word1, word2):
              if a != b:
                  diff += 1
              if diff > 1:
                  return False
          return diff == 1

      while queue:
          word, length = queue.popleft()
          if word == endWord:
              return length
          for next_word in list(wordList):
              if can_transform(word, next_word):
                  wordList.remove(next_word)
                  queue.append((next_word, length + 1))
      return 0
  ```

---

### 50. **Count Palindromic Substrings**

* **Problem**: Given a string, return the count of palindromic substrings in the string. A substring is palindromic if it reads the same forwards and backwards.

* **Recursive Solution**:

  ```python
  def count_palindromic_substrings(s):
      def expand_around_center(left, right):
          count = 0
          while left >= 0 and right < len(s) and s[left] == s[right]:
              count += 1
              left -= 1
              right += 1
          return count

      result = 0
      for i in range(len(s)):
          result += expand_around_center(i, i)   # Odd-length palindromes
          result += expand_around_center(i, i + 1) # Even-length palindromes
      return result
  ```

---

### 51. **Remove Duplicates from Sorted Array**

* **Problem**: Given a sorted array, remove duplicates in-place such that each element appears only once and return the new length of the array.

* **Recursive Solution**:

  ```python
  def remove_duplicates(nums):
      def helper(index):
          if index == len(nums) - 1:
              return
          if nums[index] == nums[index + 1]:
              nums.pop(index + 1)
              helper(index)
          else:
              helper(index + 1)
      
      helper(0)
      return len(nums)
  ```

---

### 52. **Sum of All Subsets**

* **Problem**: Given a set of numbers, find the sum of all possible subsets.

* **Recursive Solution**:

  ```python
  def subset_sum(nums):
      def helper(index, current_sum):
          if index == len(nums):
              return current_sum
          return helper(index + 1, current_sum) + helper(index + 1, current_sum + nums[index])

      return helper(0, 0)
  ```

---

### 53. **Zigzag Level Order Traversal (Binary Tree)**

* **Problem**: Given a binary tree, return the zigzag level order traversal of


its nodes' values (from left to right, then right to left for the next level and alternate between).

* **Recursive Solution**:

  ```python
  def zigzag_level_order(root):
      def dfs(node, level):
          if not node:
              return
          if len(res) <= level:
              res.append([])
          if level % 2 == 0:
              res[level].append(node.val)
          else:
              res[level].insert(0, node.val)
          dfs(node.left, level + 1)
          dfs(node.right, level + 1)

      res = []
      dfs(root, 0)
      return res
  ```

---

These **advanced recursion problems** provide great opportunities to practice and improve your problem-solving skills, especially when dealing with backtracking, dynamic programming, and recursion in complex scenarios. Let me know if you need further explanations, solutions, or help with any of these!


### Conclusion:

Recursion is an incredibly useful technique for solving problems that involve repetitive tasks or breaking problems into smaller sub-problems. Understanding the base case, recursive case, and how the function calls itself are key to using recursion effectively.
