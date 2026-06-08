a = tuple()
a=(0,"str")
print(type(a))
# if single value the datype is of the element if more than 1 dtype ="tuple"
print(list(a))
# we can typecast tuple to list its possible
print(a.index("str"))
# we can get the index postion by index position
b = set()

print(b)
c = {1,2,3,4}
print(type(c))
c.discard(0)
print(c)
# discard is a fucntion of set to remove element by value

set1 = {12,4,5}
set2 = {4,5,6,7}
print(set1.intersection(set2))
print(set1.union(set2))
# how to find the intersection btw the two

