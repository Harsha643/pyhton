# 1)  Problem Statement: Given N integers separated with space, print the unique numbers followed by underscores, the number of underscores should be equal to the number of duplicate occurrences.
# Input:
#  1 1 2 2 2 3 3 
# Output:
# [1,2,3,,,,]



# def format_unique_numbers(input_str1):
#     numbers = list(map(int, input_str1.split()))
#     count_dict = {}
#     for num in numbers:
#         if num in count_dict:
#             count_dict[num] += 1
#         else:
#             count_dict[num] = 1
#     unique_numbers = sorted(count_dict.keys())
#     total_duplicates = sum(count - 1 for count in count_dict.values())
#     output = '[' + ','.join(map(str, unique_numbers)) + ',' * total_duplicates + ']'
#     return output

# input_str1= "1 1 2 2 2 3 3"
# print(format_unique_numbers(input_str1))



# 2)  Problem Statement: Given N integers separated with space, print the count of unique numbers in the given N integers
# Input:
#  1 11 2 20 2 3 3 
# Output:
# 3


def count_unique_numbers(input_str):
    numbers = list(map(int, input_str.split()))
    count_dict = {}
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    unique_count = sum(1 for count in count_dict.values() if count == 1)
    return unique_count

input_str = "1 11 2 20 2 3 3"
print(count_unique_numbers(input_str))