"""
Visualize the code like its a sequence, view the numbers on a number line where each sequence is set

Start of sequence doesnt have a left neighbor, this indiciates the start of a sequence

Take the initial array and convert it into a set for efficient checking

When visiting a number check if the starting index has a left neighbor, if it doesnt its a unique sequence, so its
a new possible combination, check in the set if the value + 1 exists, if it does continue checking the sequence

Do this for all elements until the max len sequence is found

---------------

1. Create a set using the current list

2. Create a counter to track the longest sequence

3. Loop through the set

4. Check whether each number has a left neighbor, since thats the unique pattern for identifying whether the number
is unique in the sequence

5. Set the length to 1, since at this point we've identified that there is a unique sequence and need to account for it

6. Loop until num+length doesnt exist in the set and increment length by 1, the length is just used as a tracker
for the next numbers, and since its incrementing by 1 every time we dont need to use a seperate tracker and
it will end when we dont find any adjacent number

7. Set longest to the max of length compared to longest, as we need to compare the longest recorded sequence thus far
to the unique sequence we just found

8. The while loop will execute till all numbers in the set have been gone through, even executing if longest reaches
a point where the max sequence is at its max length
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # converts the list into a set
        longest = 0 #tracks current longest sequence

        for num in numSet: # go through each number in the set
            if (num - 1) not in numSet: # check if its a unique sequence
                length = 1 # set the length of the sequence to 1, since its a unique sequence its starting len is 1
                while (num + length) in numSet: # checks the adjacent number and loops until sequence ends
                    length += 1 # incrementing 1 number at a time
                longest = max(length, longest) # compares the current unique set to the recorded max
        return longest # returns the longest found set