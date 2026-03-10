# ⚡ CPU Scheduling Algorithms

## 📖 Overview

This repository contains **Python** implementations of two classic process scheduling algorithms studied in **Operating Systems**. Both are fundamental for understanding how an OS decides which process runs next.

---

## 🧩 Algorithms

### 🥇 FCFS — First Come, First Served

> *Processes are executed in the exact order they arrive.*

| Property | Detail |
|----------|--------|
| 📦 Type | Non-preemptive |
| ⚡ Complexity | O(n) |
| ⏱️ Avg. Wait Time | Can be high |
| 💡 Best for | Simple batch systems |

**Key traits:**
- ✅ Extremely simple to implement
- ✅ Fair — no process is skipped
- ⚠️ Can cause the **convoy effect** (long waiting times)
- ❌ Does not consider process priority or burst time

```bash
python fcfs.py
```

---

### 🥈 SJF — Shortest Job First

> *The process with the shortest burst time runs next.*

| Property | Detail |
|----------|--------|
| 📦 Type | Non-preemptive |
| ⚡ Complexity | O(n log n) |
| ⏱️ Avg. Wait Time | Optimal (minimum) |
| 💡 Best for | Systems where burst times are known |

**Key traits:**
- ✅ Minimizes average waiting time
- ✅ Optimal scheduling strategy (theoretically)
- ⚠️ Requires knowing each process's burst time in advance
- ❌ Can cause **starvation** for long processes

```bash
python sjf.py
```

---

## ⚖️ Algorithm Comparison

| Feature | FCFS | SJF |
|--------|------|-----|
| Strategy | Arrival order | Shortest burst first |
| Avg. wait time | Higher | Lower (optimal) |
| Starvation risk | ❌ None | ⚠️ Yes (long jobs) |
| Implementation | ⭐ Very easy | ⭐⭐ Moderate |
| Preemptive version | ❌ No | ✅ Yes (SRTF) |

---

## ⚙️ Requirements

All you need is **Python 3** — no external libraries required.

```bash
# Check your Python version
python --version
```

---

## ▶️ How to Run

Run either script directly:

```bash
# Run FCFS
python fcfs.py

# Run SJF
python sjf.py
```

---

## 📂 Project Structure

```
cpu-scheduling/
│
├── fcfs.py          # First Come, First Served
├── sjf.py           # Shortest Job First
└── README.md        # You are here
```

---

## 🎓 Academic Context

These algorithms are a core topic in any **Operating Systems** course. Understanding them builds the foundation for more advanced schedulers like:

- 🔄 **Round Robin** — time-slice based
- 🎯 **Priority Scheduling** — weighted execution
- ⚡ **SRTF** — preemptive version of SJF
- 🧮 **Multilevel Queue** — multiple ready queues

---

## 👨‍💻 Author

**Alan Hiram**
