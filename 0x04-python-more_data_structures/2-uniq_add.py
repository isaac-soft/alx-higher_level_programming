#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ Add all unique integers in a list
    Args:
        my_list: list of all integer elements
    Returns:
	The return value is the sum of the unique integers
    """
    uniq_list = []
    for each_item in my_list:
        if each_item not in uniq_list:
            uniq_list.append(each_item)
    return sum(uniq_list)


