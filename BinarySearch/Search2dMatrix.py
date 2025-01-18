"""
1. Declare rows, col, row to track total number of lists, cols has value of 1st list in the matrix

2. Going to search through to find the valid row now, so we have to search vertically, so we create 2 pointers
to track the top and bottom of the matrix

3. Still the same conditions as binary search where top has the lower values in the 2d matrix and bot has the higher
values so we keep the same conditional of top <= bot

4. Calculate mid-point, since thats what we are going to be comparing to initially to find whether to move it up
or down the row list

5. Check whether the target is greater than the last element in the middle row, if so our number is larger than any
value inside the middle row, since every value behind this is going to be less than the last element in the middle row,
so we need to shift our top down since the higher the rows the lower the values

6. Check whether the target is less than the first element in the middle row, if so all the values in this row and
any row above it are too large to contain our target, so we need to shift our bot down, since the lower the rows the
higher the values

7. else break since we are in our target row

8. Check whether bot is less than or equal to bot, that means that we've gone through every row and not
found a valid row with our number within the range

9. Use top and bot again to find the set row to what we're performing binary search on

10. Execute traditional binary search, so use L and R pointers, cols was set the len of any given matrix
and since every matrix is uniform in length, even if we moved to a different row its all still the same length
so we use that to calculate right, which is col - 1, which is basically len(arr) - 1, similar to reg binary search

11. Use while loop l <= r

12. Create a mid-point variable to track the middle of this row

13. Check whether the target > matrix[row][m], we need to use this accessing format since its a 2d array still
and we need to access a specific list and its specific value, if target > then we need to move left up, since
lower values are stored on left

14. Check whether target < matrix[row][m], then move right down since our mid-value is too high compared to the
target, so nothing on the right side of middle can have our target

15. The only other case is if we found our target, which we would return True

16. If we didnt find our target and the while loop exits since r < left, then we exit and it defaults to false
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0]) # rows has num of lists in matrix, cols has values in 1st list

        top, bot = 0, rows - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, cols - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]
                r = m - 1
            else:
                return True
        return False