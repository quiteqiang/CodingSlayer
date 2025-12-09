## Common Questions

```python
Easy

```

```python
核心思路： 对每个subset进行分治


def quick_sort(nlst):
    if len(nlst) <= 1:
        return nlst
    left = []
    right = []
    piv = []
    pivot = nlst[0]
    for val in nlst:
        if val == pivot:
            piv.append(val)
        elif val < pivot:
            left.append(val)
        else:
            right.append(val)
    return quick_sort(left) + piv + quick_sort(right)
```