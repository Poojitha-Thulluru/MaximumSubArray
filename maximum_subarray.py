def get_max_sub_array_sum(num_array: list, length: int, target_sum_val: int):
    if length == 0:
        return "The array is Empty"
    start, end, current_sum, max_sum = 0, 0, num_array[0], 0
    while end < size:
        if current_sum <= target_sum_val:
            max_sum = max(max_sum, current_sum)
            end += 1
            if end < size:
                current_sum += num_array[end]
            if current_sum == target_sum:
                return current_sum
        else:
            current_sum -= num_array[start]
            start += 1
    return max_sum


try:
    size = int(input("Enter the size of an array : "))
    nums_array = list(map(int, input(f"Enter {size} integers separated by space : ").split()))
    target_sum = int(input("Enter the target sum : "))
    if size == len(nums_array):
        print("The maximum sub array sum is : ", get_max_sub_array_sum(nums_array, size, target_sum))
    else:
        print(f"Enter only {size} integers separated by space")
except ValueError:
    print("Invalid Input. Please enter only integers")
