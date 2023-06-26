def two_sum(nums, target):
    ans = []
    mp = {}
    for i in range(len(nums)):
        if target - nums[i] not in mp:
            mp[nums[i]] = i
        else:
            ans.append(target - nums[i])
            ans.append(nums[i])
            break
    return ans

input_str = input("Enter the array elements: ")
elements = input_str.split()
array = [int(element) for element in elements]
target = int(input("enter target sum:"))
result = two_sum(array, target)
print(result)
