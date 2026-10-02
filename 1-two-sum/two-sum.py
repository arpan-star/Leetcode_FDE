class Solution:
    #arpan-star
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                elif target == nums[i] + nums[j]:
                    return [i,j]
                    break
            