"""
If middle value >= left most value, we are at the left sorted portion, meaning it will have values > start of the array,
 for example > 1, if 1 is the start since the array is rotated

If middle value <= left, we are in the right sorted portion, meaning  that we are in the portion of the array
that is near the starting value of the array, for example we are near 1
---------------------
1. Create a tracker for l and r

2. Loop through

3. Create a tracker for mid and check if mid is the target value

4. Check if nums[l] <= nums[mid], which means that the numbers from left to mid are in ascending order, so like
3, 4, 5, this means that left is the lowest value in the input array

5. Check whether target > nums[mid], which means that the value has to be in the right sorted portion since mid is not big enough
5.5. Check whether target < nums[l], which means that target is too small for any value on the right side, so we need to increment
the right pointer, since target is either too big or too small to be found in the left side of the array
5.5.5. Else we have verified our value in the left sorted portion, since its neither too big or too small compared
to the target, so it must be in the range, so we decrement right

6. use an else statement, since target can only be in left sorted portion(checked), mid(checked), or right sorted portion
where we then invert the signs of the statements we used above since its the right portion, then we decrement r, same rules
applied as far as too big, too small, but its flipped now we are dealing with right side
6.5 else verified value is in the right sorted array range

7. return -1 for default
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r: # <= is actually just for len 1 lists, like [1]
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            if nums[l] <= nums[mid]: # the equal to sign handles the case that both values are the same
                if target > nums[mid] or target < nums[l]: # when target is > middle value and left portion of array is sorted so that the mid value has something lower than it on the left, it means it must be to the right of mid
                    l = mid + 1 # its also possible that value at the left, is greater than the target, which means any value between it and mid cant contain the number, since thats portion is sorted
                    # the if statement is essentially saying the target is > mid, means its too big for values that are possibly between L and Mid OR its too small for values in the left side
                    # this is because for it to even be nums[l] nums[mid] it needs to be left sorted, so left is going to be the lowest value possible

                else: # this executes when its in the left sorted portion, so its between L and Mid for example in the first iteration
                    r = mid - 1

            else: #executes for right sorted portion
                if target < nums[mid] or target > nums[r]: # executes when the mid-value is too high compared to the target, so there might be values on the left that are lower than
                    r = mid - 1
                else:
                    l = mid + 1
        return -1