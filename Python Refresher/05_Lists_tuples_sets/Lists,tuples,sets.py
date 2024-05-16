# LISTS
# Can add,remove elements
# Always remain the order of elements "Bob", "Rolf", "Adam"
l = ["Bob", "Rolf", "Adam"]
print(l[0])
l[0] = "Smith"
print(l)

# WE CAN ADD ELEMENT TO LISTS
l.append("Val")
print(l)

# WE CAN REMOVE ELEMENT FROM THE LIST
l.remove("Rolf")
print(l)

## TUPLES
# Can't be modified
t = ("Bob", "Rolf", "Adam")
print(t[1])

## SETS
# Can add,remove elements
# Don't necessarily keep the order of the elements, order CAN be changed in any moment
s = {"Bob", "Rolf", "Adam"}
# Can't duplicate elements ex. Can't be two "Bob" in the set
s.add("Josh")
s.add("Bob")
print(s)
