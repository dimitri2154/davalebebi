def group_elements(list1, list2):

  return list(zip(list1, list2))

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

result = group_elements(list1, list2)
print(result)