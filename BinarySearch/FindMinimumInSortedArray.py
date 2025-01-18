"""
Find mid point of sorted array, then check if the midpoint is greater than far left section, if it is greater than
far left section that confirms that the number is on the right side of the array because only lower end values can be
on the right shifted side of the array

This is because the more rotates that the list has, the lower and lower the value of the mid-point is going to be,
[5, 1, 2, 3, 4] compared to [2, 3, 4, 5, 1]

[1, 2, 3, 4, 5] 3
[5, 1, 2, 3, 4] 2
[4, 5, 1, 2, 3] 1
[3, 4, 5, 1, 2] 5
[2, 3, 4, 5, 1] 4

So we would compare 2 and 5, and see that 2 < 5, so we know that the value must be on the left side, since any
value on the right will just be greater than the mid-point

We compare 4 with 2 and we see that any value on the left side will

Find mid-point and compare it to the current res, since mid can possibly be the lowest min

Check if the middle is > than the left most index, if its > than the left most index that means the minimum value has
to be to the right of it since the pivot value(value right before min, so the max in a list)
is always greater than anything on the left of it

So even if we find a value thats close to the pivot but greater than anything on the far left index,
say 1 index behind, its going to be greater than anything to the left of it since its rotated, so we can remove
any value there since it cant be the min due to it being in the greater sorted portion of the array

Basically if mid > far left, that means we havent found the pivot on the left side of the list and the pivot
is on the right side of the list, since mid > far left implies that the pivot point has to be on the right side
of the list, since the list is rotated and far left is not greater than mid so the left side of the array cant
contain the pivot

---------------------------------------
1. Store the result

2. Set l, r to track the indicies

3. Start the binary search

4. Check whether we are at a sorted portion of the list, nums[l] < nums[r], this will only return true if we are at
a sorted portion since if it was at a rotated portion the right section of the list would always be less than the left
section of the list

5. Compare the min of res to nums[l], since nums[l] represents the lowest value that a sorted list can go to since its
the furthest left value, then break since we found our solution if we are at the sorted portion of the list

5.5. The binary search is fundementally to search through the array, locate the pivot value, move one index past
the pivot value, then complete this if check

6. Calculate the mid-point, and check whether its lower than the current result, since the mid-point could possibly
be the minimum value, so we need to validate that here, since the only other time that we update res is when we break

7. Compare mid to the left of the list, if mid > left, that means the pivot cant be on the left side, since there must
be greater values to the right if we already arent currently on the pivot, if we are currently on the pivot, say mid was
5, then we still move forward one, since we want to move one index past the pivot to find the sorted section of the list

8. else statement, but essentially comparing mid to the right of the lift, when we do this we get rid of the right side
since we know the pivot cant be there, since the larger values are on the left, while any values on the right are
not the pivot and lower than it, since the values on the left side at this point are greater than anything that
can be on the right side, while the right side doesnt contain the min, but the left side contains the min and the pivot

9. return result
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0] # arbitrary value
        l, r = 0, len(nums) - 1 # index trackers

        while l <= r:
            if nums[l] < nums[r]: # reached a sorted section where the array is sorted
                res = min(res, nums[l]) # only occurs after at least an iteration of the binary search
                break # since array is sorted, we can just pull the left most value of the sorted array and thats the min

            m = (l + r) // 2 # find mid pointer
            res = min(res, nums[m]) # mid value could be the result
            if nums[m] >= nums[l]: # if the value at mid > far left, that means that we are in the greater side portion of the rotated array
                l = m + 1 # the array is rotated so nothing on the left can be the pivot since the array has to be rotated at least once, so the pivot would be on the right side of the array since any value to the left of the greater side of the pivot would be lower than it
            else: # essentially since the array is rotated, we can tell if we are at pivot value or some value below it(besides min), based on it being greater than the left most side of the array
                r = m - 1 # since any value on the high value side of the pivot must be less than the pivot
        return res