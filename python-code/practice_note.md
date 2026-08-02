# Practice note at July-2026

## Two sum
1. just use the for loop and good enouhgh

## Palindrome Numer
1. Use two pointers. left and right to shift the positions at the same time.

## Roman to Integer.
1. Use function zip() to have the words to pair with each other
```python
a = "123"
b = "456" 
for i, j in zip(a, b):
  print(a + " " + b)

# 1 4
# 2 5
# 3 6
```

## Longest Common Prefix.
1. Use function enumerate
```python
s = "qwerty"
for i, j in enemerate(s):
  print(str(i) + "  " j)

# 0  q
# 1  w
# 2  e
# 3  r
# 4  t
# 5  y
```

## Merge two sorted list
```python
大问题是否可以拆成同样的小问题

1 2 null
1 3 4
```

