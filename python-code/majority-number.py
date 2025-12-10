#多数元素
#核心思路：majority number数量大于一般nums 的长度，用vote来统计出现的次数，即使一开始的major选择错误，
#major也会被纠正为占多数的数字

def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    vote = 0
    major = 0
    for n in nums:
        if vote==0:
            major = n

        if major == n:
            vote +=1
        else:
            vote -= 1
    return major
nums = [2,2,1,1,1,2,2]
majorityElement(nums)