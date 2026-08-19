class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNums = {} # num - index
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashNums:
                return [hashNums[diff], i]
            hashNums[nums[i]] = i