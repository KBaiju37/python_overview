a = 10
def fun():
    global a
    b = 10+a
    print(b)
fun()
print(a)
print(b)