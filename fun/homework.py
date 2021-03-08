""" Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    return max(incoming_list)
    pass


def find_least_number(incoming_list):
    return min(incoming_list)
    pass


def add_list_numbers(incoming_list):
    return sum(filter(None, 0, incoming_list))
    pass


def longest_value_key(incoming_dict):
    first_key_length = len(incoming_dict[0:0])
    second_key_length = len(incoming_dict[1:0])

    if first_key_length > second_key_length:
        return longest_value_key(first_key_length)
    else:
        return longest_value_key(second_key_length)

    pass
