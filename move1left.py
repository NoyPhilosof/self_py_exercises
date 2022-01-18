def move_one_left(my_list):
    current_list = my_list
    first_value = current_list[0]
    rotated_list = current_list[1:] + [first_value]
    print(rotated_list)


move_one_left([3, 'A', '3d$#'])
