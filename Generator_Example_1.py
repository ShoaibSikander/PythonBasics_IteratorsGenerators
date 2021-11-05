print("Working with Python Generators")

print("***** ---------- *****")

def my_gen():
    n = 3
    yield n
    n=n*n
    yield n

my_obj = my_gen()

print(next(my_obj))
print(next(my_obj))

print("***** ---------- *****")