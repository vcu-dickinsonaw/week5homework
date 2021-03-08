""" Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    incoming_list = [2, 4, 6, 8, 10]
    find_greatest_number(max(incoming_list))
    pass


def find_least_number(incoming_list):
    incoming_list = [2, 4, 6, 8, 10]
    find_least_number(min(incoming_list))
    pass


def add_list_numbers(incoming_list):
    incoming_list = [2, 4, 6, 8, 10]
    add_list_numbers(sum(incoming_list))
    pass


def longest_value_key(incoming_dict):
    incoming_dict = {
        "name": "Alex Dickinson",
        "study": "Information Systems",
        "college": "VCU"
    }
    first_key_length = len(incoming_dict['name'])
    second_key_length = len(incoming_dict['study'])
    third_key_length = len(incoming_dict['college'])

    if first_key_length > second_key_length and first_key_length > third_key_length:
        longest_value_key(first_key_length)
    elif second_key_length > first_key_length and second_key_length > third_key_length:
        longest_value_key(second_key_length)
    else:
        longest_value_key(third_key_length)

    pass
