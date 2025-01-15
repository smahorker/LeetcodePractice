"""
Hashmap is going to be count : value represented, and will be the length of the list
since the count can be at most the length of the list

The value section of hashmap will store a list of numbers that have said count, since
that way we can check what has highest count and accoutn for overlaps

count = {
    1: 3,  # number 1 appears 3 times
    2: 2,  # number 2 appears 2 times
    3: 1   # number 3 appears 1 time
}

freq[c].append(n)

Flips the hashmap, so that you have count : value, so freq[3].append(1), makes it so that
index 3(appears 3 times), contains [1], since now you can pull directly from the list
in descending order and its organized with what appears the most

--------
1.Create count hashmap, which is used to store values initially based on num : count

2.Create a frequency list, which is filled with empty lists, handles case
of where frequency doesnt exist and there is a gap

3.Go through all numbers and insert the values into hashmap if seen, then increment
count by 1

4. Loop through count.items(), which gives key and value pair, flipping the count and value
positions and inserting it into list since now you will have an ordered list of values
which are organized in ascending order of count, since higher appearance means its
index where it was inserted is further along, 1 : 3, freq[3].append(1)

5. Create result list, which we'll append the numbers at the end

6. Go through list in descending order

7. Append the values at index i of frequency, until len of list == k, which means
the list is full, then we return result list

8. The loop for n in freq[i] handles nested lists with multiple values, since it
goes through each element regardless

O(n) + O(n), have to iterate through the count and have to iterate through all values
in value position

We are going to go from the end of the array and check one by one whether it exists,
since we are looking for the highest frequency
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freq = [[] for i in range(len(nums) + 1)] # +1 since you need to account for 0 and all numbers could be unique
        # this line also handles the case of empty lists where the frequency doesnt exist
        for n in nums:
            count[n] = 1 + count.get(n, 0) # finding the specific number, if it is found again then it gets incremented by 1
        for n, c in count.items(): # n is number, c is count
            freq[c].append(n) # you have the count of each number at this point,

        res = []
        for i in range(len(freq)) - 1, 0, -1): # iterating through array in descending order, since looking for highest count
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
