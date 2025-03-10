# Python By default has dynamic Arrays. Below is just a class to represent dynamic array structure



class Array:
  
  def __init__(self):
    self.size = 2 
    self.counter = 0
    self.list = [None]* self.size
    
  
  def resize(self):
      self.size = 2* self.size
      arr = [None] * self.size
      for i in range(0, len(self.list)):
        arr[i] = self.list[i]
      self.list = arr    

  def push(self, val):
    if self.counter == self.size - 1:
        self.resize()
    
    self.list[self.counter] = val
    self.counter += 1
    
  
  def pop(self):
    val = self.list[self.counter - 1]
    self.list[self.counter - 1] = None
    self.counter -= 1
    return val
    
  
  def add_nth(self, index, val):
    if index < self.counter:
      if self.counter == self.size - 1:
          self.resize()
      for i in range(self.counter, index, -1):
        self.list[i+1] = self.list[i]
        
      self.list[index] = val
      self.counter += 1
    else:
      print('index outside the range of continuous memory')
    
  def remove_nth(self, index):
     for i in range(index, self.counter):
      self.list[i] = self.list[i+1]
      
      self.list[self.counter - 1] =  None
      
  def get_nth(self, index):
      return self.list[index]


if __name__ == '__main__':
  my_list = Array()

  my_list.push(2)
  print(my_list.list)
  my_list.push(4)
  my_list.push(5)
  print(my_list.list)
  my_list.pop()
  print(my_list.list)
  my_list.add_nth(4, 7)
  print(my_list.list)    
  my_list.push(3)
  print(my_list.list)
  my_list.remove_nth(1)
  print(my_list.list)