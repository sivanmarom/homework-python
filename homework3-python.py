# Q-1
identification_dict ={("name", "last_name"): "sivan marom", "age": 28, "phone number": "0542071277"}
print(identification_dict)

# Q-2
def change_list(input_list):
    try:
        input_list[5] = "@"
    except IndexError as msg:
        print(msg)
    else:
        input_list[5] = '@'
        return input_list

print(change_list([1,2,3,4,5,5]))

# Q-3
def change_list(input_list):
    try:
        assert len(input_list) > 4, "There is no fifth index in this list!"
    except AssertionError as msg:
        print(msg)
    else:
        input_list[5] = "@"
        return input_list

print(change_list([1,2,3,4]))

# Q-4
def update_dict(input_dict, _key, _value):
    input_dict[_key] = _value
    return input_dict

print(update_dict({1:"hello",2:"goodbye",3:"world"}, 4,"sivan"))

# Q-5
def sum_dict(n):
    final_dict = {}
    for i in range(1, n+1):
        final_dict[i] = i + 3
    return final_dict

print((sum_dict(5)))

# Q-6
def concatenate_dict(first_dict,second_dict, third_dict):
    final_dict = dict(first_dict.items())
    final_dict.update(second_dict)
    final_dict.update(third_dict)
    return final_dict

print(concatenate_dict({1:10, 2:20}, {3:30, 4:40}, {5:50, 6:60} ))

# Q-7
def count_str(input_str):
    final_dict = {}
    for char in input_str:
        final_dict[char] = input_str.count(char)
    return final_dict
print(count_str("HANNA"))

# Q-8
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

# Q-9
def fact(n):
    assert n >= 0, "cant calculate factory of negative int"
    if n == 0:
        return 1
    return n * fact(n-1)
print(fact(-1))

# Q-10-- couldn't solve this question


# Q-11
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)
print(power(3,2))
