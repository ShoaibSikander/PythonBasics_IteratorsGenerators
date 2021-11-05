print("Iterating a list, tuple, set, string")

print("***** ---------- *****")

# Iterating a list
my_list = ["List Element 1", "List Element 2", "List Element 3"]      # make a list
iter_obj = iter(my_list)                                              # make an iterator object
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))

print("***** ---------- *****")

# Iterating a tuple
my_tuple = ("Tuple Element 1", "Tuple Element 2", "Tuple Element 3")  # make a list
iter_obj = iter(my_tuple)                                             # make an iterator object
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))

print("***** ---------- *****")

# Iterating a set
my_set = {"Set Element 1", "Set Element 2", "Set Element 3"}          # make a set
iter_obj = iter(my_set)                                               # make an iterator object
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))

print("***** ---------- *****")

# Iterating a string
my_str = "Shoaib"                                                     # make a string
iter_obj = iter(my_str)                                               # make an iterator object
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))

print("***** ---------- *****")