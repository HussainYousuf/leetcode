class Solution:

    def dfs(self, image, row, col, oldColor, newColor):
        if (
            row < 0
            or col < 0
            or row >= len(image)
            or col >= len(image[0])
            or image[row][col] != oldColor
        ):
            return
        image[row][col] = newColor
        self.dfs(image, row - 1, col, oldColor, newColor)
        self.dfs(image, row + 1, col, oldColor, newColor)
        self.dfs(image, row, col - 1, oldColor, newColor)
        self.dfs(image, row, col + 1, oldColor, newColor)

    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        if image[sr][sc] != color:
            self.dfs(image, sr, sc, image[sr][sc], color)
        return image
