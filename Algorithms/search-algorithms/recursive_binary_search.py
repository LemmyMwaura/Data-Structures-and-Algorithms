def recursive_binary_search(list, target):
  if len(list) == 0:
    return False

  midpoint = len(list) // 2
  
  if list[midpoint] == target:
    return True
  elif list[midpoint] < target:
    new_list = list[midpoint+1:]
    return recursive_binary_search(new_list, target)
  else:
    new_list = list[:midpoint]
    return recursive_binary_search(new_list, target)

def verify(result):
    print("Target found: ", result)

numbers = [1,2,3,4,5,6,7,8]
result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 4)
verify(result)
