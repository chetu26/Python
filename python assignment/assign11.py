def move_integer_to_end(lst, to_move):
    count = lst.count(to_move)  
    lst = [x for x in lst if x != to_move] 
    lst.extend([to_move] * count)  
    return lst


input_str = input("Enter the array elements: ")
elements = input_str.split()
array = [int(element) for element in elements]
to_move = int(input("enter element to move:"))
result = move_integer_to_end(array, to_move)
print(result)
