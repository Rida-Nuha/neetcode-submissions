class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        n = len(nums)

        for i in range (n):
            complement = target - nums[i]

            if complement in mp:
                return [mp[complement], i]

            mp[nums[i]] = i
