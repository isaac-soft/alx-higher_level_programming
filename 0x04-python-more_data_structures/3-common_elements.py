#!/usr/bin/python3
def common_elements(set_1, set_2):
    """ Find the common elements
    Args:
        set_1: first element
        set_2: second element
    Returns:
        The return value is the shared elements
    """

    common = []
    for i in set_1:
        for j in set_2:
            if i == j:
                common.append(i)
    return common
