## Common Questions

```java
Easy
https://leetcode.cn/problems/maximum-average-subarray-i/
https://leetcode.cn/problems/defuse-the-bomb/submissions/
https://leetcode.cn/problems/substrings-of-size-three-with-distinct-characters
https://leetcode.cn/problems/minimum-recolors-to-get-k-consecutive-black-blocks
https://leetcode.cn/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
https://leetcode.cn/problems/longest-even-odd-subarray-with-threshold/
```

```java
https://leetcode.cn/problems/longest-nice-substring
思路：
1. 递归扫描： s.substring() s.toCharArray() 
2. 分治

class Solution {
    public String longestNiceSubstring(String s) {
        if(s.length() < 2)
            return "";
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if((c <= 'Z' && !s.contains(String.valueOf((char)((int)c + 32)))) 
                || 
               (c >= 'a' && !s.contains(String.valueOf((char)((int)c - 32))))){
                String s1 = longestNiceSubstring(s.substring(0, i))；
                String s2 = longestNiceSubstring(s.substring(i+1));
                if(s1.length() >= s2.length())
                    return s1;
                return s2;
            }
        }
        return s;
    }
}


https://leetcode.cn/problems/longest-even-odd-subarray-with-threshold/

分组处理思想：数组会被分割成若干组，且每一组的判断/处理逻辑是一样的。
核心思想：
1. 外层循环负责遍历组之前的准备工作（记录开始位置），和遍历组之后的统计工作（更新答案最大值）。
2. 内层循环负责遍历组，找出这一组最远在哪结束。
```