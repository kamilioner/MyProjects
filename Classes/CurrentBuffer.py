class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        a = Node(data)
        if head is None:
            head = a
        else:
            start = head
            while start.next is not None:
                start = start.next
            start.next = a
        return head

# Complete this method




mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)
