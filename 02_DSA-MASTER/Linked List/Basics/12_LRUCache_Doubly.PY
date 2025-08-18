# Doubly Linked List Node
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

# LRU Cache Implementation
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node

        # Dummy head and tail nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove node from the list"""
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert_at_front(self, node):
        """Insert node right after head (MRU)"""
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        # Move the accessed node to the front
        self._remove(node)
        self._insert_at_front(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove the old node
            self._remove(self.cache[key])

        # Add new node at front
        new_node = Node(key, value)
        self._insert_at_front(new_node)
        self.cache[key] = new_node

        # Check if over capacity
        if len(self.cache) > self.capacity:
            # Remove LRU node
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]


# === 🧪 Test the LRU Cache ===
if __name__ == "__main__":
    print("Testing LRU Cache...")

    lru = LRUCache(2)

    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))   # ➜ 1

    lru.put(3, 3)       # Evicts key 2
    print(lru.get(2))   # ➜ -1 (not found)

    lru.put(4, 4)       # Evicts key 1
    print(lru.get(1))   # ➜ -1 (not found)
    print(lru.get(3))   # ➜ 3
    print(lru.get(4))   # ➜ 4







# Absolutely! Here's the **step-by-step approach** to solving **LeetCode 146: LRU Cache** using a **doubly linked list + hashmap**.

# ---

# ## 🧠 Step-by-Step Approach

# ---

# ### 🔹 **Step 1: Understand the Requirements**

# * Implement an LRU (Least Recently Used) Cache
# * Must support two operations in **O(1) time**:

#   * `get(key)` – returns the value if the key exists; otherwise, return `-1`
#   * `put(key, value)` – insert or update the key; evict LRU if over capacity

# ---

# ### 🔹 **Step 2: Choose the Right Data Structures**

# To achieve **O(1)** time complexity for both operations:

# 1. **HashMap (Dictionary)**

#    * Key → reference to the node in the doubly linked list
#    * Allows fast lookup in `get()` and `put()`

# 2. **Doubly Linked List**

#    * Stores nodes in the order of usage
#    * Most recently used (MRU) → **front (head)**
#    * Least recently used (LRU) → **back (tail)**
#    * Allows O(1) removal and insertion

# ---

# ### 🔹 **Step 3: Set Up the Doubly Linked List with Dummy Nodes**

# Use **dummy head and tail** nodes to simplify insert/remove logic:

# ```
# head <-> node1 <-> node2 <-> tail
# ```

# * This makes insertions and deletions at both ends easier with fewer null checks.

# ---

# ### 🔹 **Step 4: Implement `get(key)`**

# 1. Check if key exists in the hashmap:

#    * ❌ If not: return `-1`
#    * ✅ If yes:

#      * Get the node from the hashmap
#      * **Move node to the front** of the list (mark it as recently used)
#      * Return the value

# ---

# ### 🔹 **Step 5: Implement `put(key, value)`**

# 1. If the key already exists:

#    * Remove the existing node from the list
#    * Remove it from the hashmap

# 2. Create a new node with the key and value

# 3. Insert the node at the **front** of the list

# 4. Add it to the hashmap

# 5. If the cache exceeds capacity:

#    * Remove the **last node (LRU)**: `tail.prev`
#    * Remove it from the hashmap

# ---

# ### 🔹 **Step 6: Helper Functions**

# * `_remove(node)`: Unlinks a node from the doubly linked list
# * `_insert_at_front(node)`: Inserts a node right after the dummy head

# These help keep `get` and `put` clean and modular.

# ---

# ## ✅ Example

# **Capacity = 2**

# ```python
# cache.put(1, 1)   # Cache: 1
# cache.put(2, 2)   # Cache: 2 -> 1
# cache.get(1)      # Access 1 → move to front → Cache: 1 -> 2
# cache.put(3, 3)   # Evict 2 → Cache: 3 -> 1
# ```

# ---

# ## ✅ Final Notes

# * This approach ensures both `get` and `put` work in **O(1)** time
# * The hashmap gives fast access
# * The doubly linked list keeps track of usage order

# ---

# Would you like a **visual diagram** of the linked list movement or a **dry-run walkthrough** of a test case?
