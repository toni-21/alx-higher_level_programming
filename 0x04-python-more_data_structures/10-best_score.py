#!/usr/bin/python3
def best_score(my_dict):
    if my_dict == None or my_dict == {}:
        return None
    biggest = max(my_dict.values())
    for k, v in my_dict.items():
        if v is biggest:
            return (k)
