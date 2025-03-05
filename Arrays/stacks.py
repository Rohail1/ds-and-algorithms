# Using the Array class we created earlier we will create Stacks (this is by default available in python lists)

from dynamic_arrays import Array


class Stack:
  
  def __init__(self):
    self.stack = Array()
    
  
  def push(self, val):
    self.stack.push(val=val)
    
  def pop(self):
    return self.stack.pop()
  
if __name__ == '__main__':
  my_stack = Stack()
  my_stack.push(2)
  my_stack.push(1)
  my_stack.push(12)
  my_stack.push(7)
  print(my_stack.stack.list)
  my_stack.pop()
  print(my_stack.stack.list)