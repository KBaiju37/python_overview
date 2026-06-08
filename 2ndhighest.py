a = [56,23,56,78,23]
high = 0
second = 0
for i in range(len(a)):
    if (a[i] >= second):
        second = a[i]
        if(a[i]>high):
            high,second=a[i],high
    i=i+1


print(second)


    




