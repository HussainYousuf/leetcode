# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


# we cud have used genPerms to get rid of duplicates


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            left = i + 1
            right = len(nums) - 1

            prevLeft = None
            prevRight = None

            while left < right:
                if nums[left] == prevLeft:
                    left += 1
                    continue
                if nums[right] == prevRight:
                    right -= 1
                    continue

                _sum = nums[left] + nums[right] + nums[i]
                if _sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    prevLeft = nums[left]
                    prevRight = nums[right]
                    left += 1
                    right -= 1
                if _sum > 0:
                    right -= 1
                if _sum < 0:
                    left += 1

        return res
