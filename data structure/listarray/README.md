# 📚 List vs Array in Data Structures

This document gives a simple and clear explanation of **Lists** and **Arrays** in the context of data structures. It includes definitions, differences, examples, and use cases.

---

## 📌 What is an Array?

An **Array** is a **fixed-size**, **homogeneous** data structure that stores elements in **contiguous memory locations**.

### ✅ Characteristics:
- Stores elements of **same data type**
- Fixed size (cannot grow/shrink dynamically)
- Fast access via index: `O(1)`
- Insert/Delete is costly (`O(n)`)


📌 What is a List?
A List (in high-level languages like Python or Java) is a dynamic, flexible collection of elements. It can grow or shrink as needed.

✅ Characteristics:
Can store different data types (in some languages)

Dynamic size

Access time: O(1) for index access (Python)

Insert/Delete is easier than arrays

| Feature          | Array                          | List                         |
| ---------------- | ------------------------------ | ---------------------------- |
| Size             | Fixed                          | Dynamic                      |
| Data Type        | Same (Homogeneous)             | Can be Mixed (Heterogeneous) |
| Memory           | Contiguous                     | Not always contiguous        |
| Performance      | Fast access, costly insertions | Slower access, flexible      |
| Language Support | Low-level (C, C++)             | High-level (Python, Java)    |
