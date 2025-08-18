import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, item))


# Accessing the Item:
# The tuple returned by heapq.heappop(self.heap) is of the form (priority, item).
#  The [1] accesses the second element of the tuple, which is the item
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
