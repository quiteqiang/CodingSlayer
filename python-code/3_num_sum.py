### 3数之和
### 核心思路：外层循环循环处理第一个数字，对于重复的数字，直接continue;
### 内层循环，处理第2，3个数字，对于重复的数字，直接continue
#### https://leetcode.cn/problems/3sum/?envType=problem-list-v2&envId=array
def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    n = len(nums)
    ans = []
    for i in range(n-2):
        cur = nums[i]
        if i>0 and nums[i-1] == cur:
            continue
        l = i+1
        r = n-1
        while l<r:
            s = cur + nums[l] + nums[r]
            if s > 0:
                r-=1
            elif s<0:
                l+=1
            else:
                ans.append([cur,nums[l], nums[r]])
                l+=1
                while l<r and nums[l] == nums[l-1]:
                    l+=1
                r-=1
                while l<r and nums[r] ==nums[r+1]:
                    r-=1
    return ans
