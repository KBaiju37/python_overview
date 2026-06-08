l = [1, 3, 2, 4, 2, 34]

for i in range(len(l)):
    for j in range(len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]

print(l)