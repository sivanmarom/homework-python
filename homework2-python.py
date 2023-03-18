# Q-1  Create a list with your identification information.
# For example my lists length will be 4. If I will reach the value of the list on index 0, list[0] I will receive the “Alex”. Run with for loop over the list and print its content.
identification_list = ["Sivan", "Marom", 28, "0542071277"]
for val in identification_list:
    print(val)

# Q-2 Create a program that receives two lists of the same length with integers as values, if the lists are not of the same length the program must return the relevant error. The program will create a new list that will contain the largest value between the two lists at a specific index.
def higher_value(_list1, _list2):
    higher_list = []
    assert len(_list1) == len(_list2), "Your list's length is not the same!"
    for i in range(len(_list1)):
        if _list1[i] < _list2[i]:
            higher_list.append(_list2[i])
        else:
            higher_list.append(_list1[i])
    return higher_list

print(higher_value([1,2,3,4,5], [5,4,3,2,1]))

#  Q-3  Create a python program that will count the number of appearances of odd and even values in a list. In case that the program encounters a string use break statement and return a print that says, “It’s a string!!!” and nullify the values of odd and even numbers counters.
def count_odds_and_even(input_list):
    odd_counter = 0
    even_counter = 0
    for val in input_list:
        if type(val) == str:
            print("It's a string!!!")
            even_counter = 0
            odd_counter = 0
            break
        else:
            if val % 2 == 0:
                even_counter += 1

            elif val % 2 == 1:
                 odd_counter += 1
    print("Numbers of even numbers:", even_counter)
    print("Numbers of odd numbers:", odd_counter)
count_odds_and_even( [1, 2, 3, 4, 5, 8, 9])

# Q-4  Build a function that will receive a list with integer values as its input. The function will calculate the sum of the integers in the list and will return the sum result.
def sum_list(input_list):
    sum_result = 0
    for val in input_list:
        sum_result += val
    return sum_result

print(sum_list([1,2,3,4]))

# Q-5  Build a function that will receive a list with integer values as its input. The function will multiply all values in the list and return the result.
def multiplication_list(input_list):
    multiply_result = 1
    for val in input_list:
        multiply_result *= val
    return multiply_result

print(multiplication_list([1,2,3,4]))

# Q-6  Build a function that will receive a list with integer values as its input. The function will find the minimal value in the list and return this value.
def find_min_value(input_list):
    min_value = input_list[0]
    for val in input_list:
        if val < min_value:
            min_value = val
    return min_value
print(find_min_value([6,2,3,4,5]))

# Q-7  Build a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def lower_and_upper(input_str):
    _upper_counter = 0
    _lower_counter = 0
    for char in input_str:
        if char == " ":
            _upper_counter += 0
            _lower_counter += 0
        elif char == char.lower():
            _lower_counter += 1
        elif char == char.upper():
            _upper_counter += 1
    print("No. of Upper case characters:", _upper_counter)
    print("No. of Lower case characters:", _lower_counter)

lower_and_upper("Alex Kuznetsov Hello")

# Q-8  Build a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_elem(input_list):
    unique_set = set(input_list)
    unique_list = list(unique_set)
    return unique_list

print(unique_elem([1, 2, 3, 3, 3, 3, 4, 5]))

# Q-9  Write a Python program to construct the following pattern, using a nested loop.
def pattern_1():
    for i in range(1,9):
        for j in range(1,i+1):
            print(j, end='')
        print()

pattern_1()

# Q-10  Write a Python program to print the following patterns
def pattern_2():
    for i in range(7):
        for j in range(5):
            if (i in [0,6] and j == 4) or (i in [1,2] and j in [1,2,3,4]) or (i == 3 and j in [0, 4]) or (i in [4, 5] and j in [0,1,2,3]):
                print(" ", end='')
            else:
                print("*", end='')
        print()

pattern_2()