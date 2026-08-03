from collections import defaultdict


def lengthOfLongestSubstring( s: str) -> int:
  counter = defaultdict(int)
  ans = left = 0

  for i, c in enumerate(s):
      print(counter)
      print(str(left) + "    " + str(i))
      counter[c] += 1
      
      while counter[c] >1:
          counter[s[left]]-=1
          left+=1
          
      anx = max(ans, i - left + 1)
  return ans

print(lengthOfLongestSubstring("abcabcbb"))