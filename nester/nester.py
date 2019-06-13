"""This is nester.py module. It provides function print_list_items to print elements of list. Also works for nested lists"""
""" TODO: change way of distributing package """
def print_list_items(items_list):
#   """This function takes a positional argument called items_list, which should be any of lists types.
        # Function works rercursively."""
    for item in items_list:
        if isinstance(item, list):
            print_list_items(item)
        else:
            print(item)
