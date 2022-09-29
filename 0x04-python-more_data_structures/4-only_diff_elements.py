#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """prints exclusive list element
    Args:
        set_1: first element
        set_2: second element
    Returns:
        The value is exclusive to one of the elements
    """
    return (set_1 ^ set_2)
