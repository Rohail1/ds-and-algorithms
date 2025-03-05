# Create Array of fixed Size

from typing import Any


def create_array(size: int) -> list:
    return [None] * size
  


# Print entire Array

def print_arr(arr: list, size: int) -> None:
  for i in range(size):
    print(arr[i])
    

def push(arr:list, val: Any) -> list:
      arr[len(arr) - 1] = val


def pop(arr:list) -> int:
  
    last_element = arr[len(arr) - 1]
    arr[len(arr) - 1] = None
    return last_element
  
  
def insert_middle(arr:list, size: int, val: Any, index: int):
  
    if index < len(arr) and arr[size-1] == None:
      for i in range(size-1, index, -1):
        arr[i] = arr[i-1]
      
      arr[index] = val;
    else:
      print('Array full or index out of range')     
      
      
def remove_middle(arr:list, index: int):
  
    if index < len(arr):
      for i in range(index, len(arr) - 1):
        arr[i] = arr[i+1]
      arr[len(arr)- 1] = None;
    else:
      print('Array full or index out of range')      
   
      
if __name__ == '__main__':
  my_list = create_array(8)  
  print(my_list)
  arr_size = len(my_list)
  push(my_list, 2)
  print(my_list)
  pop(my_list)
  print(my_list)
  insert_middle(my_list, arr_size, 4, 3)
  print(my_list)
  insert_middle(my_list, arr_size, 6, 3)
  print(my_list)
  remove_middle(my_list,3)
  print(my_list)