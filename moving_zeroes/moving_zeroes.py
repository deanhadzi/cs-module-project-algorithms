'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Step 1 - create a copy of the original array.
    arr_copy = arr[:]
    # Step 2 - create a counter to get number of zeros in array.
    counter = 0
    # Step 3 - loop through the array copy and remove all zeros.
    # Increase counter.
    # If the array is made of all zeros, break once the counter matches length of original array.
    while 0 in arr_copy:
        arr_copy.remove(0)
        counter += 1
        if counter == len(arr):
            break

    # Step 4 - create a all zero array.
    zeros = [0] * counter
    # Step 5 - overwrite the original array.
    arr = arr_copy + zeros

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

