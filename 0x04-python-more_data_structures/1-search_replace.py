#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """" Search and Replace function
    Args:
        my_list: initial list
        search: element to to be replaced in the list
        replace: new element
    Returns:
        The return value is a new list with the replaced value
    """

    new_list = []
    for each_item in my_list:
        if each_item == search:
            new_list.append(replace)
            continue
        new_list.append(each_item)
    return new_list
