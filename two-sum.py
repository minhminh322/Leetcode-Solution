class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numDict:
                return [numDict[complement], i]
            numDict[nums[i]] = i

        return []  # No solution found