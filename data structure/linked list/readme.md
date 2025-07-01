# Singly Linked List Implementation in Python

This project contains a simple implementation of a **Singly Linked List** in Python. A linked list is a linear data structure where each element is a separate object (called a node) and contains a reference to the next node in the sequence.

---

## 📌 Features

- Add node at the beginning
- Add node at the end
- Insert node at a given position
- Delete node by value
- Search for a value
- Display the linked list

---

## 📁 File Structure

- `linked_list.py` – Contains the `Node` and `LinkedList` class implementation
- `main.py` – Sample usage of the linked list

---

## 📦 Getting Started

Clone this repository or copy the Python files into your project directory.

```bash
git clone https://github.com/your-username/linked-list-python.git
cd linked-list-python
```

---

## 🔧 Implementation

### `linked_list.py`

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_value(self, target, data):
        temp = self.head
        while temp and temp.data != target:
            temp = temp.next
        if temp:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node
        else:
            print("Value not found in the list.")

    def delete_by_value(self, value):
        if self.head is None:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next and temp.next.data != value:
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next
        else:
            print("Value not found in the list.")

    def search(self, value):
        temp = self.head
        while temp:
            if temp.data == value:
                return True
            temp = temp.next
        return False

    def display(self):
        temp = self.head
        elements = []
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(elements))
```

---

## 🧪 Sample Usage (`main.py`)

```python
from linked_list import LinkedList

ll = LinkedList()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_beginning(5)
ll.insert_after_value(10, 15)

ll.display()  # Output: 5 -> 10 -> 15 -> 20

ll.delete_by_value(15)
ll.display()  # Output: 5 -> 10 -> 20

print("Search 20:", ll.search(20))  # Output: True
print("Search 100:", ll.search(100))  # Output: False
```

---

## 🧠 Applications of Linked List

- Dynamic memory allocation
- Implementation of stacks and queues
- Symbol tables in compilers
- Navigation systems (next/previous)

---

## ✅ Requirements

- Python 3.x
- No external libraries needed

---

