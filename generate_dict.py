'''Write a Python function which generates and returns a dictionary
    where the keys are numbers between 1 and n (both inclusive) and the values are square of keys.
    sample input:
    10
    expected Output:
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}'''
def generate_dict(number):
    new_dict={}
    for i in range(1,number+1):
        new_dict[i]=i*i
    return new_dict
number=int(input('enter the number'))
print(generate_dict(number))
