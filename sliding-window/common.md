## Common Questions

```java
Easy
https://leetcode.cn/problems/maximum-average-subarray-i/
https://leetcode.cn/problems/defuse-the-bomb/submissions/


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
```