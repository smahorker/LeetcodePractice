"""
Array between [1, max value of piles], perform binary search on the array, since its faster sort than going
1 by 1, since the array is sorted, go through each index with the found element from binary search, consume each
pile, and calculate the hours it takes, then take the hours it takes and see if there is anyway it can be shorter
with other values in the list

1. Create a left and right pointer to track our array, going from 1 to max of array, [1, max(arr)], since thats
the range our values can be in, 1 to max value of piles

2. Create a variable to store result and set it to r, since thats the max possible eat rate, so its a valid solution
to check over 0

3. Start binary search loop

4. Calculate the midway point of r and l

5. Create a temp variable to track the hours of each iteration of rate, its going to change in every iteration
of the binary search

6. Go through each value in the pile, divide the pile by the rate, use ceiling to round up since even .1 bananas
will cause another hour to be consumed, add this value to hours

7. Compare whether the found hours is <= the hours provided by the question, if so then set res to the minimum
between res and k, since we are trying to find the minimum integer

8. Decrement the right side by 1, since we know that any value to the right will be too high to yield a lower
rate

9. else decrement left, since in this case it means we found a rate which goes too fast compared to the alloted hours,
so no rate left of this value can fit the problem specs

10. return result after binary search
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # represents the array we are searching through, 1 to max value in array
        res = r # its the max eat rate our array can have, so its a possible valid solution over choosing 0

        while l <= r:
            k = (l + r) // 2 # mid-point
            hours = 0 # tracker per iteration of rate, how many hours it takes at said rate
            for p in piles:
                hours += math.ceil(p / k) # round up since you cant eat partial bananas, so will need to push up even if .1

            if hours <= h: # found a solution within the bounds of hours provided
                res = min(res, k)  # compare which rate of eating is smaller, since we are looking for min time
                r = k - 1 # since its a valid time we need to look for a smaller k, so reduce r
            else: # rate at which bananas are ate is too high
                l = k + 1
        return res
