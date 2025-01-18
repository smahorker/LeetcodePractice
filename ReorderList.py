"""
You are essentially alternating from one side of the list to the other side
1 - 2 - 3 - 4 - 5 = 1 - 5 - 2 - 4 - 3

1 - 2 - 3 - 4
s   f
    s       f

1 - 2 - 3 - 4 - 5
s   f
    s       f
        s       f
The approach is to split up the list into 2 parts using fast and slow pointers and reverse the 2nd half of the list
-------------
1. Create slow and fast pointers to find halfway point of list

2. Create a loop to go through to find the midpoint of the list, use slow and fast pointers, check for fast and
fast.next because we can encounter a null ptr error, if we try to do fast.next.next when we fast is at null or
right before it

3. Set second to slow.next, since thats the head of the 2nd list

4. Set prev to None, since its going to be treated as the head of our new list at the start, obviously as we go
through the list its not going to be the head anymore until we hit the end of the list again

5. slow.next = None to unlink both of these lists and treat them as 2 seperate lists, this is basically
taking the node that connects the nodes at the middle and disconnecting them

6. Regular reverse algorithm, where we store the next node in temp since its gonna be lost when we swapping
the directions of the nodes, since we are changing it from pointing forward to pointing backward, 1 -> 2 -> 3
to 1 <- 2 ---- 3(somewhere in memory), do the swapping of the pointers, update prev to curr, since we are
done with this iteration and need to indicate that we are done with dealing with reversing the previous node,
move curr to the node we saved, since thats the address of the node we unlinked at the start

7. Start the merging process, set first to head, which is the start of the first list, set second to prev, which
is the head of the 2nd list, 1 -> 2 --- 3 <- 4, 1 would be first, 4 would be second

8. Loop through second, since that will hit Null right after we link the final value in the 1st list

9. Store tmp1 and tmp2 since we are going to lose the link when linking between 2 different lists, this
is going to be the next node of the node we are about to move, so since we are shifting a node, we are going
to lose track of what it points to next, so we need to save that now

10. Links the value from the first list to the next available value in the 2nd list, then links the value
from the 2nd list to the value after what we just linked in the 1st list so we are inserting the value
from the 2nd tree between the value in the 1st list essentially

11. Update the values of first and 2nd, since we are done with inserting for this iteration
-----------------------------------
Finding mid-way point of list, disconnecting the lists to treat them seperately, reversing the 2nd list,
merging in a way that inserts the value from the 2nd list in between the values in the first list
"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find halfway point of list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast  = fast.next.next

        second = slow.next # start of 2nd half of list, its the head of the linked list
        prev = slow.next = None # slow.next is set to None, since we want to unlink the lists, so we are
        # unlinking the mid-points of the list, so its gonna be treated like 2 seperate lists 1 -> 2 -- 3 <- 4

        # reverse second
        while second: # works the same as usual reverse function
            tmp = second.next # store the tmp since we are unlinking
            second.next = prev # set the curr to point at the previous node
            prev = second # update prev to be curr
            second = tmp # move curr to the next node

        # merge two halves
        # 1 -> 2 -- 3 <- 4
        first, second = head, prev # beginning of the 2nd list, so it would be 4 in the example above
        while second:
            tmp1, tmp2 = first.next, second.next # need to store this since we are going to be modifying the links
            # and the links are going to be lost
            first.next = second # links first node to the available node in the 2nd list, so 1 -> 4
            second.next = tmp1 # links the value we just linked, so 4 to the next node in 1st, so 2, 1 -> 4 -> 2
            first, second = tmp1, tmp2 # need to shift forward in the list

