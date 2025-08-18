`heapq` is a module in Python that provides an implementation of the heap queue algorithm, also known as the priority queue algorithm. Heaps are binary trees for which every parent node has a value less than or equal to any of its children. The `heapq` module provides functions to implement heaps based on regular lists.

### Key Functions of `heapq`

1. **heapq.heappush(heap, item)**
   - Pushes the `item` onto the `heap`, maintaining the heap invariant.
   
   ```python
   import heapq

   heap = []
   heapq.heappush(heap, 4)
   heapq.heappush(heap, 1)
   heapq.heappush(heap, 7)
   heapq.heappush(heap, 3)

   print(heap)  # Output: [1, 3, 7, 4]
   ```

2. **heapq.heappop(heap)**
   - Pops the smallest item off the `heap`, maintaining the heap invariant. If the heap is empty, `IndexError` is raised.
   
   ```python
   smallest = heapq.heappop(heap)
   print(smallest)  # Output: 1
   print(heap)      # Output: [3, 4, 7]
   ```

3. **heapq.heappushpop(heap, item)**
   - Pushes the `item` on the `heap`, then pops and returns the smallest item from the heap. The combined action runs more efficiently than `heappush()` followed by a separate call to `heappop()`.
   
   ```python
   result = heapq.heappushpop(heap, 2)
   print(result)  # Output: 2 (the smallest item)
   print(heap)    # Output: [3, 4, 7]
   ```

4. **heapq.heapreplace(heap, item)**
   - Pops and returns the smallest item from the `heap`, and then pushes the `item`. The heap size does not change. If the heap is empty, `IndexError` is raised.
   
   ```python
   result = heapq.heapreplace(heap, 5)
   print(result)  # Output: 3 (the smallest item)
   print(heap)    # Output: [4, 5, 7]
   ```

5. **heapq.heapify(x)**
   - Transforms list `x` into a heap, in-place, in linear time.
   
   ```python
   nums = [4, 1, 7, 3, 8, 5]
   heapq.heapify(nums)
   print(nums)  # Output: [1, 3, 5, 4, 8, 7]
   ```

6. **heapq.nlargest(n, iterable, key=None)**
   - Returns a list with the `n` largest elements from the dataset defined by `iterable`. `key` is a function that serves as a key for the comparisons (default is `None`).
   
   ```python
   nums = [4, 1, 7, 3, 8, 5]
   largest = heapq.nlargest(3, nums)
   print(largest)  # Output: [8, 7, 5]
   ```

7. **heapq.nsmallest(n, iterable, key=None)**
   - Returns a list with the `n` smallest elements from the dataset defined by `iterable`. `key` is a function that serves as a key for the comparisons (default is `None`).
   
   ```python
   smallest = heapq.nsmallest(3, nums)
   print(smallest)  # Output: [1, 3, 4]
   ```

### Example: Using `heapq` for a Priority Queue

Here is an example of using `heapq` to implement a simple priority queue:

```python
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        return heapq.heappop(self.heap)[1]

    def is_empty(self):
        return len(self.heap) == 0

# Example usage
pq = PriorityQueue()
pq.push("task1", 3)
pq.push("task2", 1)
pq.push("task3", 2)

while not pq.is_empty():
    print(pq.pop())

# Output:
# task2
# task3
# task1
```

In this example, the priority queue uses tuples where the first element is the priority and the second element is the task. This ensures that the queue always pops the task with the smallest priority first.