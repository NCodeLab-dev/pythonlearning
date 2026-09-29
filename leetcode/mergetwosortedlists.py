# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        list3 = ListNode()
        head = list3
        while list1.next != None or list2.next != None:
            
            if list1.val > list2.val:
                list3.val = list1.val
                list1 = list1.next
                list3.val = None
            else:
                list3.val = list2.val
                list2 = list2.next
                list3.val = None
            list3 = list3.next;
def add(first : int = 5,second : int = 6) -> None :
    print("addition is",first+second)

def main():
    print();
    add(3,4);
    
if __name__ == "__main__":
    main();