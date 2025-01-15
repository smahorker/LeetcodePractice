"""
Rearraging strings = anagram

Brute Force
Sort each of the strings and then compare them, since it will sort by ascii value and
then you can compare them

Hashmap

Count the characters of each string and assign a key to the amt of letters

Time complexity
O(m*n) = m is num of strings in input list and n is letters we go through in each string
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # deals with case where count doesnt exist yet

        for s in strs: # going through each string in the list
            count = [0] * 26 # creates a list for every string, 26 letters

        for c in s: # going through each character of the string
            count[ord(c) - ord("a")] += 1 # maps the character to ascii value of 0-25, ex: a = 80, a cmp a = 80-80 = 0, which we map to
            # increments count at the index by 1, since that associated index letter has been seen
            # all anagrams have the same array
        res[tuple(count)].append(s) # creates new key if no similar count array exists
                                    # adds to the value section of the corresponding
    return list(res.values())