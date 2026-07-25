class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        sum = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[sum] = nums[i]
                sum+=1
        return sum
            