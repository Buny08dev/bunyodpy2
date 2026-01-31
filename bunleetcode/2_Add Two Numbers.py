# 2. Add Two Numbers
# def addTwoNumbers(l1:list, l2:list):
#     answer=int("".join(list(map(lambda x:str(x),l1))[::-1]))+int("".join(list(map(lambda x:str(x),l2))[::-1]))
#     return [int(i) for i in str(answer)][::-1]
# print(Solution([9,9,9,9,9,9,9],[9,9,9,9]).addTwoNumbers())

# class ListNode:
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next
 
# # instantiate the nodes
# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node4 = ListNode(4)
 
# # link the nodes
# node1.next = node2
# node2.next = node3
# node3.next = node4
 
# # traverse the linked list and print each node's value
# current_node = node1
# while current_node is not None:
#     print(current_node.val)
#     current_node = current_node.next