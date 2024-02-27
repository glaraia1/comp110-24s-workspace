"""Practice with dictionaries."""

ice_cream: dict[str, int] ={"choclate": 12, "vanilla": 8, "strawberry": 5}
  # sometimes beneficial to only use one quite

#  adding mint
ice_cream["mint"] = 3
print(ice_cream)

# removing mint
ice_cream.pop("mint")
print(ice_cream)

#  Accessing = only want to print how many ordered vanilla
print(ice_cream["vanilla"])
# if using an f string, use single quotes for key to prevent error
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

# Updating a value (adding one more to the order)
ice_cream["vanilla"] +=1
print(ice_cream)
print(len(ice_cream)) # to see length of dictionary

# How to check if a key is in dictionary -> returns a bool
#type: <key> in <dict name>
print("mint" in ice_cream)

# cannot have duplicates of keys, but can have duplicates of values