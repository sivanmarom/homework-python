# Q-1  Create a dictionary that will include your identification information. Use relevant keys for each field. Use the tuple key for relevant declarations.
identification_dict ={("name", "last_name"): "sivan marom", "age": 28, "phone number": "0542071277"}
print(identification_dict)

# Q-2  Build a function that will receive a list as an input, the function will replace the fifth index character with the character ‘@’ if the fifth index doesn’t exist in the list please return a relevant exception. If there is no exception please return the updated list.
def change_list(input_list):
    try:
        input_list[5] = "@"
    except IndexError as msg:
        print(msg)
    else:
        input_list[5] = '@'
        return input_list

print(change_list([1,2,3,4,5,5]))

# Q-3  Build a function that will receive a list as an input, the function will replace the fifth index character with the character ‘@’ if the fifth index doesn’t exist in the list please return a relevant assertion. If there is no assertion please return the updated list.
def change_list(input_list):
    try:
        assert len(input_list) > 4, "There is no fifth index in this list!"
    except AssertionError as msg:
        print(msg)
    else:
        input_list[5] = "@"
        return input_list

print(change_list([1,2,3,4]))

# Q-4  Build a function that will receive a dictionary a new key and a new key value. The function will add the new key value to the dictionary and will return the updated dictionary.
def update_dict(input_dict, _key, _value):
    input_dict[_key] = _value
    return input_dict

print(update_dict({1:"hello",2:"goodbye",3:"world"}, 4,"sivan"))

# Q-5  Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x+3).
def sum_dict(n):
    final_dict = {}
    for i in range(1, n+1):
        final_dict[i] = i + 3
    return final_dict

print((sum_dict(5)))

# Q-6 Write a Python script to concatenate following dictionaries to create a new one.
def concatenate_dict(first_dict,second_dict, third_dict):
    final_dict = dict(first_dict.items())
    final_dict.update(second_dict)
    final_dict.update(third_dict)
    return final_dict

print(concatenate_dict({1:10, 2:20}, {3:30, 4:40}, {5:50, 6:60} ))

# Q-7  Build a function that will count appearances of each character in the string and will return a dictionary with string characters as keys and the frequency of each character as key value.
def count_str(input_str):
    final_dict = {}
    for char in input_str:
        final_dict[char] = input_str.count(char)
    return final_dict
print(count_str("HANNA"))

# Q-8  Write a Python program to combine two dictionary adding values for common keys.
def combined_dict(d1,d2):
    final_dict = {}
    d1_keys = list(d1.keys())
    d2_keys = list(d2.keys())
    for key in d1_keys:
        if key in d2_keys:
            final_dict[key] = d1[key] + d2[key]
            d2_keys.remove(key)
        else:
            final_dict[key] = d1[key]
    for key in d2_keys:
        final_dict[key] = d2[key]
    return final_dict

print(combined_dict( {'a': 100, 'b': 200, 'c':300},{'a': 300, 'b': 200, 'd':400} ))

# Q-9  Build a Python function to calculate the factorial of a number (a positive integer). The function accepts the number as an argument. Please use recursion. In case that your input is negative integer please return an assertion.
def fact(n):
    assert n >= 0, "cant calculate factory of negative int"
    if n == 0:
        return 1
    return n * fact(n-1)
print(fact(-1))

# Q-10  Create a recursive function to calculate the sum of the positive integers of n+ (n-1) + (n-3)... (Until n-x <= 0). The n value is the function input the summary result is the output of the function.
#
#
# -- couldn't solve this question


# Q-11  Create a recursive function to calculate the value of 'a' to the power 'b'.
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)
print(power(3,2))
