"""
Prefix and postfix approach

Prefix = Start at first position and multiply each next array index by itself and the previous one, we only need to
multiply by the 1 right before it since it accounts for the compound previously and itself, so initial value is gonna
be the lowest number in the array

Postfix = Start at last index and multiply each next array by itself and next one, so we are going in descending order
of the list starting at the greatest value and multiplying until we hit the end, so initial value is gonna be the highest
number in the array

The product is going to be prefix * prefix, which is going to be our solution array

We start at the index 0, since nothing is before in the prefix we default to 1, then we look at index 1 in the postfix,
we multiply these 2 numbers and our result is the value in the final array

Essentially index 1 of main array = prefix[0] * postfix[2], index 2 = prefix[1] * postfix[3]

This solution takes up more memory if we were to use arrays to store the postfix and prefix

2 pass solution on the input array

Going to solve for prefix first, store it into the solution list, then going to solve for postfix and multiplying into
solution list accordingly

First pass solves for prefix and inserts into solution array, 2nd pass multiplies postfix into prefix

Go number by number, storing the prefix value, default is 1 so insert 1 at the start of list, then multiply 1
by the next number and insert that into list, update prefix value to the compounded number, multiply compounded number
by next number, and go until solution array is filled, but you are going to skip the final array since you
cant insert it anywhere in the list

Do this for postfix as well, multplying in descending order, index 0 will not get inserted with anything now

The reason why we skip the final index is since we start with the initial value of 1, which we multiply the first index by


1. Create a list with 1s in them, just as a base multiplier

2. Set the prefix value to 1

3. Loop through all the numbers in the array

4. Multiply the result[i] by the prefix, this is where we store our actual prefix

5. Update the prefix by multiplying by nums[i], this is essentially pushing us up one increment in the prefix, since
all values need the compounded multiplier, its going to end before the last index because you're using the 1 as the
initial multiplier when updating res, the initial prefix = 1 is being used

6. Loop through the list start at the last index, go backwards, stop at index 0. We use len(nums) - 1, since we cant
access the array since len will give us a value 1 digit too high, we stop at -1 since its non-inclusive

7. Multiply the result[i] by the postfix, this will give us the final solution for that index

8. multiply the postfix by nums[i]

9. return result
"""



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) # cant be empty list since need to multiply by something so fill with 1s
        prefix = 1 # prefix starts at 1, since its the base multiplier
        for i in range(len(nums)): # go through each number in list
            res[i] = prefix # sets the prefix index and moves it forward
            prefix *= nums[i] # multiply current index by compounded number
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): # start from last index of array,  go until before -1(just index 0), count backwards by 1
            res[i] *= postfix # multiplies postfix and prefix, pulls from the end of the result array and multiplies the by postfix value
            postfix *= nums[i] # adjusts postfix value to account for compounding from previous number
        return res

