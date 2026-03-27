# DPK02 - List Reversal Implementations

This project compares five different Python implementations of a list reversal algorithm, measured against a list of **10,000,000 elements**.

## Implementations

| File | Approach | Description |
|---|---|---|
| `DPK02_impl_1.py` | `lst[::-1]` | Python slice notation |
| `DPK02_impl_2.py` | `for` loop + `append` | Pure Python for loop |
| `DPK02_impl_3.py` | `while` loop + `append` | Pure Python while loop |
| `DPK02_impl_4.py` | `while True` + `append` | Pure Python while loop with break |
| `DPK02_impl_5.py` | `list(reversed(lst))` | Built-in `reversed()` iterator |

## Benchmark Results

Measured using the `time` command (`time python <file> > /dev/null`):

| Implementation | Total time |
|---|---|
| `impl_1` (slice `[::-1]`) | **9.758s** |
| `impl_5` (`reversed()`) | 9.867s |
| `impl_2` (`for` loop) | 9.946s |
| `impl_4` (`while True`) | 10.447s |
| `impl_3` (`while` loop) | 10.934s |

## Why is `impl_1` the fastest?

### Native C operations vs. Python interpreter overhead

- **`lst[::-1]` (impl_1)** and **`list(reversed(lst))` (impl_5)** are implemented natively in CPython (written in C). They operate directly on memory without going through the Python interpreter loop on each element, making them significantly faster.

- **Pure Python loops (impl_2, impl_3, impl_4)** execute interpreter bytecode on every iteration. Each loop step involves Python object creation, reference counting, and method calls (`append`), adding considerable overhead at scale.

### Why the times look close?

The wall clock times are dominated by the `print()` of 10 million elements to the terminal (I/O bound). To isolate the algorithm, redirect output:

```bash
time python DPK02_impl_1.py > /dev/null
```

## Key Takeaways

- Prefer built-in Python operations (`[::-1]`, `reversed()`) over manual loops — they are faster and more readable.
- When benchmarking, always eliminate I/O side effects (like printing large outputs) that can mask the actual algorithm performance.
- Among pure Python loop approaches, the difference is small — the main bottleneck is the interpreter overhead per iteration, not the specific loop construct used.
