def binary_search(list, target):
  startpoint = 0
  endpoint = len(list) - 1
  count = 0

  while startpoint <= endpoint:
    count = count + 1
    midpoint = (startpoint + endpoint) // 2

    if list[midpoint] == target:
      return midpoint
    elif list[midpoint] < target:
      startpoint = midpoint + 1
    else:
      endpoint = midpoint - 1

  return f'{None}: Target does not exist'


def verify(index):
  if index is not None:
    print("Target found at index: ", index)
  else:
    print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]
result = binary_search(numbers, 16)
verify(result)
