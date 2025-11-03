class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:  # empty array
            return 0

        i = 0  # pointer for the last unique element prthom ta sobsomoy unique number dhore neao hbe
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1
