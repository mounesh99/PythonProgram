'''Write a Python function to rotate the list of elements by N positions.
    The function should return the rotated list.
    testCase 1:
    Input list: [1, 2, 3, 4, 5, 6]
    Number of positions to be rotated = 2
    Expected Output:[5, 6, 1, 2, 3, 4]
    testCase 2:
    Input list: [1, 2, 3, 4, 5, 6]
    Number of positions to be rotated = 4
    Expected Output:[3,4,5, 6, 1, 2]'''
    

def rotate_list(input_list,n):
    l=len(input_list)
    m=l-n
    return input_list[:m]+input_list[m:]
input_list=[1,2,3,4,5,6]
output_list=rotate_list(input_list,4)
print(output_list)
