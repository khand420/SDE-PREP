class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # optional: for O(1) tail insert

    # Insert at Head (O(1))
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    # Insert at Tail (O(n) without tail pointer, O(1) with tail)
    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    # Insert at Position (0-based index) (O(n))
    def insert_at_position(self, pos, data):
        if pos == 0:
            self.insert_at_head(data)
            return

        new_node = Node(data)
        curr = self.head
        for _ in range(pos - 1):
            if not curr:
                print("Position out of bounds")
                return
            curr = curr.next

        new_node.next = curr.next
        curr.next = new_node
        if new_node.next is None:
            self.tail = new_node

    # Delete Head (O(1))
    def delete_head(self):
        if self.head:
            self.head = self.head.next
            if self.head is None:
                self.tail = None

    # Delete by Value (O(n))
    def delete_by_value(self, value):
        if not self.head:
            return

        if self.head.data == value:
            self.delete_head()
            return

        curr = self.head
        while curr.next and curr.next.data != value:
            curr = curr.next

        if curr.next:
            curr.next = curr.next.next
            if curr.next is None:
                self.tail = curr

    # Search by Value (O(n))
    def search(self, value):
        curr = self.head
        while curr:
            if curr.data == value:
                return True
            curr = curr.next
        return False

    # Traverse / Print (O(n))
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

    # Reverse Linked List (O(n))
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev


if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.insert_at_head(10)
    ll.insert_at_tail(20)
    ll.insert_at_tail(30)
    ll.insert_at_position(1, 15)
    ll.print_list()           # 10 -> 15 -> 20 -> 30 -> None

    ll.delete_head()
    ll.print_list()           # 15 -> 20 -> 30 -> None

    ll.delete_by_value(20)
    ll.print_list()           # 15 -> 30 -> None

    print("Search 30:", ll.search(30))  # True
    print("Search 100:", ll.search(100))  # False

    ll.reverse()
    ll.print_list()           # 30 -> 15 -> None
