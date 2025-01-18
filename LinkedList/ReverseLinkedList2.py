"""
Dummy node handles edge cases of need to access behind the first element, as well as the first element
changing making it hard to track head, but you can just call dummy node which always points to head

Need to iterate L - 1 times for our us to go from node 1 to L, since its indexed starting at 1

-------------------------
"""


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
            dummy = prev = ListNode(0, head)

            # getting to the left node and storing node right before it, since we need to link back to that
            leftPrev, cur = dummy, head
            for i in range(left - 1):
                leftPrev, cur = cur, cur.next # every iteration we want to move them forward

            prev = None # we want to point to None rather than pointing back to LP

            # reversing the linked list from L to R, and setting the tail of the list to None
            for i in range(right - left + 1): # distance = r - l + 1, r 4 l 2 = 4 - 2 + 1 = 3 dist
                tmpNext = cur.next # store value since we're cutting link
                cur.next = prev # point backward
                prev, cur = cur, tmpNext # move up 1 node in the list for both var

            # We have the reversed linked list at this point, now we want our left node to be pointing to
            # the value right after right, and we want our right node to be pointing to LP

            #ptr update
            leftPrev.next.next = cur
            leftPrev.next = prev

            return dummy.next

            # going to use lp.next.next, since this will go from 1 -> 2 -> NULL, since 2 is pointing at Null right
            # now, .next.next fetches us whatever the node after LP is pointing to and we can set that cur because
            # cur is now at the node after right

            # Need to make LP point to prev now






