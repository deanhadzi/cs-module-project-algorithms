'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Step 1 - create an empty answer array.
    answer_arr = []
    # Step 2 - create an array with one item at the current index being dropped.
    for i in range(len(arr)):
        arr2 = arr[:]
        del arr2[i]
        # Step 3 - multipy the numbers in the array created in step 2.
        result = 1
        for x in arr2:
            result = result * x
        # Step 4 - add the result to the answer array.
        answer_arr.append(result)

    return answer_arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

