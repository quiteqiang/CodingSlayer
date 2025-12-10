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

### 递归 合并两个有序链表
```python
核心思路： 从下一个节点开始递归
def mergeTwoLists(self, l1, l2):
    if not l1:
        return l2
    elif not l2:
        return l1

    if l1.val <= l2.val:
        l1.next = self.mergeTwoLists(l1.next,l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2
```

### 双指针
```python
#Easy:
# https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
def removeDuplicates(self, nums):
    p = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[p] = nums[i]
            p+=1
    return p
```

### Binary Searc
# https://leetcode.cn/problems/search-insert-position/description/  
```python
  def searchInsert(self, nums, target):
      l, r = 0, len(nums)
      while l < r:
          mid = l + (r - l) // 2
          if nums[mid]<target: 
              l = mid+1
          else:
              r = mid
      return l
```