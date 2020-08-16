'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Step 1 - Create an answer array.
    answer_arr = []
    # Step 2 - Create array slice coordinates.
    slice_start = 0
    slice_end = k
    # Step 3 - Move through the array and find local maximums.
    while slice_end <= len(nums):
        sliding_window = nums[slice_start:slice_end]
        # Step 4 - Append the local maximum to the answer array.
        answer_arr.append(max(sliding_window))
        # Step 5 - Increment the coordinates.
        slice_start += 1
        slice_end += 1
        
    return answer_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")