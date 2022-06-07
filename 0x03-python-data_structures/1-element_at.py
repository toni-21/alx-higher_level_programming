#!/usr/bin/python3
def element_at(my_List, idx):
    if idx < 0:
        return None;

    if idx > (len(my_List) - 1):
        return None;

    return (my_List[idx]);
