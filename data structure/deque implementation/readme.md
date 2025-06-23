# Deque (Double-Ended Queue) Implementation in Python

A **Deque (Double-Ended Queue)** is a linear data structure that allows insertion and deletion of elements from both ends — front and rear. This project provides a simple implementation of a deque using Python.

## 📌 Features

- Add elements to the front and rear
- Remove elements from the front and rear
- Check if deque is empty
- Get front and rear elements
- Display the entire deque

## 🚀 Getting Started

Clone the repository or copy the `deque.py` file to your project directory.

```bash
git clone https://github.com/your-username/deque-implementation.git
cd deque-implementation
```

## 🧠 Deque Operations

### Class: `Deque`

#### Methods:

- `is_empty()` → `bool`: Returns `True` if deque is empty.
- `add_front(item)` → `None`: Adds an item to the front of deque.
- `add_rear(item)` → `None`: Adds an item to the rear of deque.
- `remove_front()` → `item`: Removes and returns item from the front.
- `remove_rear()` → `item`: Removes and returns item from the rear.
- `peek_front()` → `item`: Returns item at the front without removing it.
- `peek_rear()` → `item`: Returns item at the rear without removing it.
- `display()` → `None`: Prints all elements of the deque.

## 🧾 Example Code

```python
# deque.py

class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Deque is empty"

    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Deque is empty"

    def peek_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "Deque is empty"

    def peek_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Deque is empty"

    def display(self):
        print("Deque:", self.items)
```

## 🔍 Sample Usage

```python
from deque import Deque

dq = Deque()

dq.add_rear(10)
dq.add_front(20)
dq.add_rear(30)
dq.display()            # Deque: [20, 10, 30]

print(dq.remove_front()) # 20
print(dq.remove_rear())  # 30
dq.display()             # Deque: [10]

print("Front:", dq.peek_front())  # 10
print("Rear:", dq.peek_rear())    # 10
```

## 🛠️ Requirements

- Python 3.x

No external libraries are required.

## 📚 Applications of Deque

- Palindrome checking
- Undo/Redo functionality in text editors
- Scheduling algorithms
- Sliding window problems in arrays


