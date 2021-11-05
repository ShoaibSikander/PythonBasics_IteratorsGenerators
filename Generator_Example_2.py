print("Working with Python Generators")

print("***** ---------- *****")

def my_gen():
    n = 3
    yield n
    n=n*n
    yield n

my_obj = my_gen()

for val in my_obj:
    print(val)

print("***** ---------- *****")