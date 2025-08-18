class CircularQueue:
    def __init__(self, k):
        self.size = k
        self.queue = [None] * k
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, value):
        if self.isFull():
            return "Queue is full"

        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = value
        return "Enqueued " + str(value)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"

        removed = self.queue[self.front]
        if self.front == self.rear:
            # Last element removed
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return "Dequeued " + str(removed)

    def Front(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[self.front]

    def Rear(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[self.rear]

    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return

        print("Circular Queue:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()



q = CircularQueue(5)
print(q.enqueue(10))
print(q.enqueue(20))
print(q.enqueue(30))
print(q.enqueue(40))
print(q.enqueue(50))  # Full now
print(q.enqueue(60))  # Should say "full"

q.display()
print(q.dequeue())
print(q.dequeue())
q.display()

print("Front:", q.Front())
print("Rear:", q.Rear())







# Sure! Here's a **step-by-step approach** to understand and implement a **Circular Queue** using an array.

# ---

# ## 🔄 **Circular Queue: Step-by-Step Approach**

# A **circular queue** is a **fixed-size** data structure where the last position is connected back to the first, forming a **circle**.

# ### 🎯 Goal:

# Use a **fixed-size array** efficiently to implement a queue with constant time `enqueue()` and `dequeue()` operations.

# ---

# ## 🔢 Step 1: Initialize the Queue

# * Create an array of size `k`.
# * Initialize two pointers:

#   * `front = -1`
#   * `rear = -1`

# ```python
# queue = [None] * k
# front = -1
# rear = -1
# ```

# ---

# ## 🧩 Step 2: Enqueue Operation (`enqueue(x)`)

# * **Check if full:**

#   * A circular queue is full if `(rear + 1) % size == front`
# * **If empty:**

#   * Set both `front` and `rear` to `0`
# * **Otherwise:**

#   * Move `rear` forward by `(rear + 1) % size`
# * Insert the new element at `queue[rear]`

# ---

# ### ✅ Enqueue Conditions

# | Condition             | Action                     |
# | --------------------- | -------------------------- |
# | Queue is full         | Return error/False         |
# | Queue is empty        | `front = rear = 0`         |
# | Else (normal enqueue) | `rear = (rear + 1) % size` |

# ---

# ## ❌ Step 3: Dequeue Operation (`dequeue()`)

# * **Check if empty:**

#   * If `front == -1`, queue is empty.
# * **Get value at `queue[front]`**
# * **If only one element:**

#   * Set `front = rear = -1` (queue becomes empty)
# * **Otherwise:**

#   * Move `front` forward: `front = (front + 1) % size`

# ---

# ### ❌ Dequeue Conditions

# | Condition             | Action                         |
# | --------------------- | ------------------------------ |
# | Queue is empty        | Return error                   |
# | Only one element      | Reset `front` and `rear` to -1 |
# | Else (normal dequeue) | `front = (front + 1) % size`   |

# ---

# ## 👀 Step 4: Front and Rear Operations

# * `Front`: return `queue[front]` if not empty
# * `Rear`: return `queue[rear]` if not empty

# ---

# ## 🤔 Step 5: isFull and isEmpty

# ```python
# def isFull():
#     return (rear + 1) % size == front

# def isEmpty():
#     return front == -1
# ```

# ---

# ## 🔁 Visualization

# For a queue of size `5`:

# ### Enqueue 10 → 20 → 30 → 40 → 50

# ```text
# Index:  [0] [1] [2] [3] [4]
# Queue: [10, 20, 30, 40, 50]
# front = 0
# rear  = 4
# ```

# ### Dequeue Twice (10 and 20):

# ```text
# front = 2
# rear  = 4
# Queue still has [30, 40, 50]
# ```

# ### Enqueue 60 → 70 (wraps around!):

# ```text
# rear = (4 + 1) % 5 = 0 → insert at index 0
# rear = (0 + 1) % 5 = 1 → insert at index 1

# Index:  [0] [1] [2] [3] [4]
# Queue: [60, 70, 30, 40, 50]
# front = 2
# rear  = 1
# ```

# Now it's **full again**, even though we’ve used earlier slots. That's the power of circular queues!

# ---

# ## 🧠 Summary

# | Step           | Key Logic                      |
# | -------------- | ------------------------------ |
# | Initialization | `front = -1, rear = -1`        |
# | Enqueue        | Update `rear` with wraparound  |
# | Dequeue        | Update `front` with wraparound |
# | isFull         | `(rear + 1) % size == front`   |
# | isEmpty        | `front == -1`                  |

# ---

# Let me know if you’d like to see:

# * Full code again
# * Circular queue with linked list
# * Visual trace with an example input
 