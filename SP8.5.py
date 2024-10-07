from SP8 import get_all_lists, find_two_smallest

lists = get_all_lists()

with open("result.txt", "w") as result_file:
    for list_name, lst in lists.items():
        smallest_numbers = find_two_smallest(lst)
        result_file.write(f"{list_name}: {smallest_numbers}\n")

print("Results saved to result.txt")