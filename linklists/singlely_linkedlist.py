class Node:
    
  def __init__(self, data):
    self.data = data
    self.next = None
  
class SingleLinkedList:
  
  
  head: Node
  tail: Node | None
  
  def __init__(self, node: Node):
    self.head = node
    self.tail = node


  def add_node_end(self, node: Node):
      current_node: Node = self.head
      while current_node.next:
        current_node = current_node.next

      current_node.next = node


  def push_node(self, node: Node):
    self.tail.next = node
    self.tail = node

  def print_list(self):
    current_node = self.head
    while current_node.next:
      print(current_node.data)
      current_node = current_node.next


