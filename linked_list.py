# Simple class that takes a list as input and returns a linked list

class ListNode:
  # [1,2,3]
  def __init__(self, x):
    self.val = x[0]
    if len(x)>1:
      self.next = ListNode(x[1:])
    else: self.next = None
  
  def to_string(self):
    while self:
      print(self.val),
      self = self.next


x = ListNode([2,4,6,1])
x.to_string()