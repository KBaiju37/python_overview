add = lambda x,y:(x+y,x-y)
a,b = add(x= 4, y=5)
print(a)
print(b)
#lambda is a anonomous fucntion :nameless it is a single line of expression

num=[1,2,3,4]
a=list(filter(lambda x:x%2==0,num))
print(a)

marks = [23,67,7,8,67]
a = list(filter(lambda x:x<60 ,marks))
print(a)


n = 0
for i in range(10):
    if(n == 5):
        break


