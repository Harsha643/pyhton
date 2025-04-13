def format_unique_numbers(input_str1):
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
