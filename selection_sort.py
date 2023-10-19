def selection_sort(my_list):
  list_length = len(my_list)
  for i in range(list_length - 1):
    # Set lowest to the element of the list located at index i
    lowest = my_list[i]
    index = i
    # Iterate again over the list starting on the next position of the i variable
    for  j in range(i+1, list_length):
      # Compare whether the element of the list located at index j is smaller than lowest
      if lowest>my_list[j]:
        index = j
        lowest = my_list[j]
    my_list[i] , my_list[index] = my_list[index] , my_list[i]
  return my_list

my_list = [6, 2, 9, 7, 4, 8]
selection_sort(my_list)
print(my_list)