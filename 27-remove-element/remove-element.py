class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        expectedNums = []
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            else:
                expectedNums.append(nums[i])
                print(expectedNums)
        nums[:] = expectedNums