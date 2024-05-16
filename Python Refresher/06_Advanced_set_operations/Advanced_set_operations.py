friends = {"Bob", "Rolf", "Adam"}
abroad = {"Bob", "Adam"}

# DIFFERENCE BETWEEN TWO SETS
local_friends = friends.difference(abroad)
print(local_friends)

# CALCULATING SETS
local = {"Rolf"}
friends = local.union(abroad)
print(friends)

# INTERSECTION SETS
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(both)