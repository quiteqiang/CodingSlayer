## Leetcode
- [二分搜索](#binary-search)

### Binary Search
```python
# l = 0/1 r=n target
# 解题框架
while l <= r: # 这个是循环不变量
  mid = l + (r-l)//2
  if mid<target:
    l+=1
  else:
    r-=1
return l
"""
https://leetcode.com/problems/first-bad-version
"""
```
