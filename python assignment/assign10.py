def square_sorted_array(arr):
    squared_arr = [num ** 2 for num in arr]  
    sorted_arr = sorted(squared_arr) 
    return sorted_arr

input_str = input("Enter the array elements: ")
elements = input_str.split()
array = [int(element) for element in elements]
result = square_sorted_array(array)
print(result)

