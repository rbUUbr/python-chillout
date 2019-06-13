numbers = ["first", "second", "third"]
numbers.insert(1, 1) # extra insert

for my_number in numbers:
    print(my_number)


# working with nested lists

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Palin", "John Cleese",
"Terry Gilliam", "Eric Idle", "Terry Jones"]]]
# you can use isinstance BIF to iterate over nested items
# the only issue that you need to know max deep size
for movie in movies:
    if isinstance(movie, list):
        for n_movie in movie:
            if isinstance(n_movie, list):
                for n_item in n_movie:
                    print(n_item)
            else:
                print(n_movie)
    else:
        print(movie)

# temporary solution is to build reusable function
def print_list_items(items_list):
    for item in items_list:
        if isinstance(item, list):
            print_list_items(item)
        else:
            print(item)

# now code is:
print_list_items(movies)
