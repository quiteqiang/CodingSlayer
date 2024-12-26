## Leetcode
- [数组循环](#array-loop)
- [二分搜索](#binary-search)

### Array Loop

```java
// from start to end
for (int i = 0; i < nums.length; i++){}

// from end to start
for (int i = nums.length-1; i >=0; i--){}
int i = nums.length-1
while (i>=0){
    i--;
}

//求长度
j - i + 1

//求距离
Math.abs(j-i)

```

### Binary Search

```java
// 求target
int l = 0;
int r = nums.length-1;
while (l < = r ) {
    int mid = l + (l+r) /2;
}
```


3. 滑动窗口

```java
int res = 0;
for (int i = 0; i<nums.length; i++) {
   // 处理零时变量的逻辑
   // 不要在这里计算ans
    while(slide_condition) {
        // 计算ans的逻辑
    }
     // 或者 计算ans的逻辑
}

Sample:
https://www.hackerrank.com/challenges/the-birthday-bar/problem
https://leetcode.cn/problems/move-zeroes/description/
https://leetcode.cn/problems/remove-duplicates-from-sorted-array/description/
https://leetcode.cn/problems/longest-substring-without-repeating-characters/
https://leetcode.cn/problems/search-insert-position/description/

HARD:
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii
```

4. HashMap去重，统计

```java
Map<String, Integer> map = new HashMap<>();

Integer val = map.get(key);

if (val != null) {
    // value not existing logic
} else {
   // value existing logic
}

```


5. IN place 删除字符
p-1

```java
while (left < right) {
    char tp = chs[left];
    chs[left++] = chs[right];
    chs[right--] = tp;
}
```

6. Check Char by using Char

```java
'a'<=chs[left] && chs[left] <= 'z' 
```

7.  Right Left Two Point
```java
int left = 0;
int right = nums.length-1;

https://leetcode.cn/problems/squares-of-a-sorted-array/
https://leetcode.cn/problems/container-with-most-water/
https://leetcode.cn/problems/valid-palindrome/
https://leetcode.cn/problems/reverse-only-letters/
https://leetcode.cn/problems/faulty-keyboard/description/
https://leetcode.cn/problems/merge-sorted-array/description/
https://www.hackerrank.com/challenges/sock-merchant/problem
https://www.hackerrank.com/challenges/migratory-birds/problem
```

8. Char Processing
```java
# 判断字母，数字
if ('0'<=chs[p] && chs[p]<'9')
if ('a'<=chs[p] && chs[p]<'z')
if ('A'<=chs[p] && chs[p]<'Z')
```

9. list 转换 Array
```java
Arrays.toString(Arrays.stream(array).toArray())
```


10. 3数之和， 4数之和
```java

```

11. 遍历数字
```java
while () {
    int temp = x % 10;
    
}

```

11. 贪婪算法
```java
找到循环不变量，找最多！
https://leetcode.cn/problems/jump-game/
```







