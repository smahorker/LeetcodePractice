"""
Look at midway point and compare it to the target and compare it to the left pointer

If its smaller than the target then everything to the left will be smaller than the target

Then we shift the pointer to m + 1 or m - 1 based on what we need

O(logN) time, when we hit the midway point we find the target or eliminate half the possibilites, while loop runs
as many times as we can divide the input array by 2, log2n = x, how many times can we divide n by 2, since we are
splitting the array by half, it takes up logn time
--------
1. Declare trackers for left and right variables

2. Loop through until r >= l because left is approaching the right value, need the = for example if the value is at the
last index, then the code would exit since it 
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2 # can cause overflow error nearing integer limit in other languages
            # m = l + ((r-l) // 2) is more effective for other languages, you are essentially adding 1/4 + 1/4, since l = 1/4 and r - l // 2 = (1/2) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

