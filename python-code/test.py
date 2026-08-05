# [4, 5, 6, 7, 0, 1, 2，3]
p = 3 mid = 7





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

class Solution {
public:
    int findMin(vector<int>& nums) {
        int n = nums.size();
        int left = 0, right = n - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            // 小于最后一个数，满足条件，向左收缩
            if (nums[mid] <= nums[n - 1]) {
                right = mid - 1;
            } else {        // 不满足条件，向右收缩
                left = mid + 1;
            }
        }
        return nums[left];
    }
};
