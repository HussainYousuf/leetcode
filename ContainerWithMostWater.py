class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxA = 0
        while left < right:
            width = right - left
            minHeight = 0
            if height[left] < height[right]:
                minHeight = height[left]
                left += 1
            else:
                minHeight = height[right]
                right -= 1
            area = minHeight * width
            if area > maxA:
                maxA = area

        return maxA
