class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        expectedNums = []
        i = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] == nums[-1]:
                expectedNums.append(nums[i])
                break
            elif nums[i] < nums[i+1]:
                expectedNums.append(nums[i])
            elif nums[i] == nums[i+1]:
                continue
        nums[:] = expectedNums
