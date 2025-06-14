# 📊 Big O Notation – Quick Reference

Big O Notation is used to describe **how efficient an algorithm is** in terms of:

- **Time Complexity** – How fast it runs.
- **Space Complexity** – How much memory it uses.

It gives us an **upper bound** on performance as input size **n** grows.

---

## 🚀 Why It Matters

Big O helps you compare algorithms and understand how they scale.

For example:

- Sorting 10 numbers? Any algorithm works.
- Sorting 10 million? You need something efficient!

---

## 🧠 Common Time Complexities

| Big O     | Name           | Example                        | Notes                         |
|-----------|----------------|--------------------------------|-------------------------------|
| O(1)      | Constant        | Accessing an array index       | Fastest – doesn't grow        |
| O(log n)  | Logarithmic     | Binary search                  | Great for large data          |
| O(n)      | Linear          | Looping through an array       | Grows proportionally          |
| O(n log n)| Log-linear      | Merge sort, Quick sort         | Optimal for many algorithms   |
| O(n²)     | Quadratic       | Nested loops (e.g. bubble sort)| Gets slow quickly             |
| O(2ⁿ)     | Exponential     | Recursive Fibonacci            | Very inefficient              |
| O(n!)     | Factorial       | Traveling Salesman (brute)     | Impractical for large `n`     |

---

