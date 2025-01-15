"""
brute force

check every combination and check if they can go through every number
starting at 1st index
"""

"""
Hash map

Mapping value to the index, 4 : 0, 3 : 1, etc, that way we can access the index when
we compare by the value

The hashmap is storing the previous values we have visited, then we are looking if the 
complement exists in the hashmap, if it exists in the hashmap that means we found a 
solution

So we are just taking each value in one at a time until we find a matching complement,
and we add to list the hashmap until we find the complement


Iterating through array once and adding procedurally through array
Time: O(n)
Hashmap consumes space
Space: O(n) 

generally we dont need to print the key since the way we organize it is because 
we are accessing the values associated with the key
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index storage

        for i, n in enumerate(nums): # i : index n : number
            diff = target - n # finds the complement of the given number
                return [prevMap[diff], i] #accesses the index of the already indexed number and current index
            prevMap[n] = i # new value like this and it doesnt exist in the dictionary a new value gets created


