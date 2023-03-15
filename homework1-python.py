# Q-1
name = "Sivan"
last_name = "Marom"
age = 28
phone_number = "0542071277"
print("Name:", name)
print("Last name:", last_name)
print("Age:", age)
print("Phone number:", phone_number)

# Q-2
def check_string(input_str):
    if len(input_str) >= 9:
        if input_str[7].lower() == 'a' and input_str[8].lower() == 'b' and input_str[9].lower() == 'c':
            print("True")
        else:
            print("False")
    else:
        print("Your string is too short")

check_string("blabaaaaaaa")

# Q-3
def swap_string(str1, str2):
    new_str1 = str2[:2] + str1[2]
    new_str2 = str1[:2] + str2[2]
    final_str = new_str1 + " " +new_str2
    print(final_str)

swap_string("abc", "xyz")

# Q-4
def change_str(input_str):
    if len(input_str) > 2:
        if input_str[-3:] == "ing":
            input_str += "ly"
            print(input_str)
        else:
            input_str += "ing"
            print(input_str)
    else:
        print(input_str)

change_str("ab")

# # Q-5
def creating_new_str(input_str):
    middle_index = int(len(input_str)/2)
    new_str = input_str[middle_index] + input_str[1:middle_index] + input_str[-1] + input_str[middle_index+1:-1] + input_str[0]
    print(new_str)

creating_new_str("axxxbyyc")

# Q-6
def insert_string(input_str):
    insert_str = "Tutorial "
    space_index = input_str.find(" ")
    new_str = input_str[:space_index + 1] + insert_str + input_str[space_index + 1:]
    print(new_str)

insert_string("Python 3.0")

# Q-7
def sort_string(input_str):
    new_str ="".join(sorted(input_str))
    print(new_str)

sort_string("w3resource")

# Q-8
def rounded_float(_floating_numbers):
    print(round(_floating_numbers, 2))

rounded_float(3.1415926)
rounded_float(12.9999)

# Q-9
def count_substring(input_string):
    print("Occurs: ", input_string.count("w3resource.com"))

count_substring("Welcome to w3resource.com")