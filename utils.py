def find_max(list_of_num):
    maximum_num = list_of_num[0]
    for num in list_of_num:
        if num > maximum_num:
           maximum_num = num
    return maximum_num