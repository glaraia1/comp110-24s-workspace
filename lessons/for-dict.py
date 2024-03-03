"""Practice with Dictionaries and for loops."""

in_stock: dict[str, bool] = {"carrots": True, "beets": False, "apples": True}
#Print only the True values using a for loop

for key in in_stock:
    print(key)
    #this will print all keys (carrots, beets, apples)
    print(in_stock[key])
    #this will print the values at the key (True, False, True)

#including the necessary if conditional
for key in in_stock:
    if in_stock[key]: #or can say if in_stock[key] is True:
        print(key)
