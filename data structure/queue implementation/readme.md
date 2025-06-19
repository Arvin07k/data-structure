# Queue Implementation in Python

A **Queue** is a linear data structure that follows the **FIFO (First In, First Out)** principle. This project demonstrates a simple implementation of a queue using Python's list data structure.

## 📌 Features

- Enqueue (insert element at the rear)
- Dequeue (remove element from the front)
- Peek at the front element
- Check if the queue is empty
- Display all elements

## 🚀 Getting Started

Clone the repository or copy the `queue.py` file to your project directory.

```bash
git clone https://github.com/your-username/queue-implementation.git
cd queue-implementation
```

## 🧠 Queue Operations

### Class: `Queue`

#### Methods:

- `is_empty()` → `bool`: Returns `True` if the queue is empty.
- `enqueue(item)` → `None`: Adds an item to the rear of the queue.
- `dequeue()` → `item`: Removes and returns the item at the front of the queue.
- `peek()` → `item`: Returns the item at the front without removing it.
- `display()` → `None`: Prints all elements of the queue.

## 🧾 Example Code

```python
# queue.py

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "Queue is empty"

    def display(self):
        print("Queue:", self.items)
```

## 🔍 Sample Usage

```python
from queue import Queue

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()          # Queue: [10, 20, 30]

print(q.dequeue())   # 10
q.display()          # Queue: [20, 30]

print("Front:", q.peek())  # 20
```

## 🛠️ Requirements

- Python 3.x

No external libraries are required.

## 📚 Applications of Queue

- Printer queues
- CPU scheduling
- Handling requests in web servers
- Breadth-First Search (BFS) in graphs


