list_one = [10, 20, 30, 40, 50]
list_two = [5, 15, 25, 35, 45]
list_three = [1, 2, 3, 4, 5]
list_four = [100, 200, 300, 400, 500]
list_five = [-10, -20, -30, -40, -50]

mixed_list = [3, -1, 0, 7, -5, 12]
large_numbers = [1000, 2000, 3000, 4000, 5000]
small_numbers = [-100, -200, -300, -400, -500]

def get_all_lists():
    return {
        "list_one": list_one,
        "list_two": list_two,
        "list_three": list_three,
        "list_four": list_four,
        "list_five": list_five,
        "mixed_list": mixed_list,
        "large_numbers": large_numbers,
        "small_numbers": small_numbers,
    }

def find_two_smallest(lst):
    if len(lst) < 2:
        return None
    sorted_lst = sorted(lst)
    return sorted_lst[0], sorted_lst[1]