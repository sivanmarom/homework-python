# Q-1 Create a program that will print your identifications.
name = "Sivan"
last_name = "Marom"
age = 28
phone_number = "0542071277"
print("Name:", name)
print("Last name:", last_name)
print("Age:", age)
print("Phone number:", phone_number)

# Q-2  For a string that you created please check if:
# The character at index 7 equals ‘a’.
# The character at index 8 equals ‘b’.
# The character at index 9 equals ‘c’.
# If all conditions exists please print “True”,
# Else print False.
# Pay attention for edge cases like the length of the string and so on.
# Your program must not crash for any string.
def check_string(input_str):
    if len(input_str) >= 9:
        if input_str[7].lower() == 'a' and input_str[8].lower() == 'b' and input_str[9].lower() == 'c':
            print("True")
        else:
            print("False")
    else:
        print("Your string is too short")

check_string("blabaaaaaaa")

# Q-3 Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
def swap_string(str1, str2):
    new_str1 = str2[:2] + str1[2]
    new_str2 = str1[:2] + str2[2]
    final_str = new_str1 + " " +new_str2
    print(final_str)

swap_string("abc", "xyz")

# Q-4  Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
def change_str(input_str):
    if len(input_str) >= 3:
        if input_str[-3:] == "ing":
            input_str += "ly"
            print(input_str)
        else:
            input_str += "ing"
            print(input_str)
    else:
        print(input_str)

change_str("abing")

# # Q-5  For a string (three characters and more) that you have created please create a new string that follows the next rules:
# The first character of the new string is the middle character of the original string.
# The middle character of the new string is the last character of the original string.
# The last character of the new string is the first character of the original string.
def creating_new_str(input_str):
    middle_index = int(len(input_str)/2)
    new_str = input_str[middle_index] + input_str[1:middle_index] + input_str[-1] + input_str[middle_index+1:-1] + input_str[0]
    print(new_str)

creating_new_str("axxxbyyc")

# Q-6  Write a Python function to insert a string in the space of the original string.
# You can assume that there is just one space in your string.
def insert_string(input_str):
    insert_str = "Tutorial "
    space_index = input_str.find(" ")
    new_str = input_str[:space_index + 1] + insert_str + input_str[space_index + 1:]
    print(new_str)

insert_string("Python 3.0")

# Q-7  Write a Python program to sort a string lexicographically. Look For relevant method.
def sort_string(input_str):
    new_str ="".join(sorted(input_str))
    print(new_str)

sort_string("w3resource")

# Q-8  Write a Python program to print the following floating numbers upto 2 decimal places.
def rounded_float(_floating_numbers):
    print(round(_floating_numbers, 2))

rounded_float(3.1415926)
rounded_float(12.9999)

# Q-9 Write a Python program to count occurrences of a substring in a string. Look for a relevant method.
def count_substring(input_string):
    print("Occurs: ", input_string.count("w3resource.com"))

count_substring("Welcome to w3resource.com")