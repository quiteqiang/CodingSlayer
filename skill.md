### Leetcode

1. 数组循环
```java
// from start to end
for (int i=0; i<nums.length; i++) {}

// from end to start
for (int i=nums.length-1; i>=0; i--){}

int i = nums.length -1;
while (i>0){
  i--;
}
```

2. 求长度
```java
j - i + 1
```

3. 求距离
```java
Math.abs(i-j);
```

4. 二分搜索
```java
// 求target
int l = 0;
int r = nums.length-1;
while ( l<= r ){
  int mid = l + (l + r) /2;
}
```

4.  滑动窗口
```java
int res = 0;
for (int i=0; i<nums.length; i++) {
  //处理临时变量的逻辑
  //不要在这里计算ans
  while (slide_conditino) {
    // 计算ans的逻辑
  }
  // 计算ans的逻辑
}
```
Sample:
https://www.hackerrank.com/challenges/the-birthday-bar/problem

5. HashMap去重，统计
```java
Map<String, Integer> map = new HashMap<>();

Integer val = map.get(key);

if (val != null) {
  // value not existing logic
} else {
  // value existing logic
}
```