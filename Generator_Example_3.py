print("Working with Python Generators")

print("***** ---------- *****")

def my_gen(dict):
    for x,y in dict.items():
        yield x,y

my_dict = {1:"Hi", 2:"Welcome"}
result = my_gen(my_dict)

print(next(result))
print(next(result))

print("***** ---------- *****")