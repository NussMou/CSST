l = ["a","b","c"]
l.append("XDD")
print(l)

l = ["a","b","c"]
l.append(list("XDD"))
print(l)

# if I want ['a', 'b', 'c', 'X', 'D', 'D']


l = ["a","b","c"]
l.extend(list("XDD"))
print(l)




