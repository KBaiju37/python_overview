a = [1,2,3,4,"by",True,31,2,3,2]
b = [56,7,8,0]

print(a)
#list is hetrogenous and can store duplicates
print(a[0::2])
print(b[::-2])
#[start : stop : step]

#usage of append,insert and extend
#list.insert(index, element)
a.insert(3,5)
print(a)
#list.extend(list)
a.extend(b)
print(a)
#usage of pop pops removes the last in list as its ordered
a.pop()
print(a)

# pop removes the element from index
a.pop(5)
print(a)

# tuple is not mutable
        
tup = (1,2,3,4)
print(tup[0]) = 21 