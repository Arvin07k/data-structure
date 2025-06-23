# Stack Implementation in Python

A **Stack** is a linear data structure that follows the **LIFO (Last In, First Out)** principle. This project demonstrates a simple implementation of a stack using Python's list data structure.

## 📌 Features

- Push (insert element at the top)
- Pop (remove element from the top)
- Peek at the top element
- Check if the stack is empty
- Display all elements

## 🚀 Getting Started

Clone the repository or copy the `stack.py` file to your project directory.

```bash
git clone https://github.com/your-username/stack-implementation.git
cd stack-implementation
```

## 🧠 Stack Operations

### Class: `Stack`

#### Methods:

- `is_empty()` → `bool`: Returns `True` if the stack is empty.
- `push(item)` → `None`: Adds an item to the top of the stack.
- `pop()` → `item`: Removes and returns the item from the top of the stack.
- `peek()` → `item`: Returns the item at the top without removing it.
- `display()` → `None`: Prints all elements of the stack.

## 🧾 Example Code

```python
# stack.py

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def display(self):
        print("Stack:", self.items)
```

## 🔍 Sample Usage

```python
from stack import Stack

s = Stack()

s.push(5)
s.push(10)
s.push(15)
s.display()           # Stack: [5, 10, 15]

print(s.pop())        # 15
s.display()           # Stack: [5, 10]

print("Top:", s.peek())  # 10
```

## 🛠️ Requirements

- Python 3.x

No external libraries are required.

## 📚 Applications of Stack

- Function call stack in recursion
- Undo/Redo operations in editors
- Syntax parsing (e.g., parentheses matching)
- Expression evaluation (e.g., postfix notation)

## 📄 License

This project is open-source and free to use under the [MIT License](LICENSE).
