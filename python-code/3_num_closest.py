### 最接近的三数之和
### 核心思路： 类似于三数之和，如果三数之和大于target 并且 min_diff最小， right -1；
###                        如果三叔之和小于target，并且 min_diff最小， left +1；


def threeSumClosest(self, nums, target):
  """
  :type nums: List[int]
  :type target: int
  :rtype: int
  """
  nums.sort()
  n = len(nums)
  ans = 0
  min_diff = 1000
  for i in range(n-2):
      cur = nums[i]
      if nums[i-1] == nums[i]:
          continue
      l = i+1
      r = n-1
      while l<r:
          s = cur + nums[l] + nums[r]
          if s == target:
              return s
          if s > target:
              if s-target < min_diff:
                  min_diff = s-target
                  ans = s
              r-=1
          else: # s<target
              if target - s < min_diff:
                  min_diff = target -s
                  ans = s
              l+=1
  return ans
  