# 只出现一次的数字
# 核心思路：^ 操作，同样的数字操作等于0， 不同数字操作等于1
def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = 0
    for n in nums:
        ans ^= n
    return ans
nums = [4,1,2,1,2]
singleNumber(nums)