## Common Questions

```python
Easy

```
### 快排
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

### 回文数字
```python
def isPalindrome(self, x):
    if x < 0 or x>0 and x%10 == 0: 
        return False
    ans = 0
    old = x
    while x >0:
        tmp = x%10
        ans = ans*10 + tmp
        x//=10
    return ans == old
```

### 斐波那契数列
```python
def fib(self, n):
    if n == 0:
        return 0
    n1 = 0
    n2 = 1
    for i in range(n-1):
        temp = n2
        n2 = n1 + n2
        n1 = temp
    return n2
```
