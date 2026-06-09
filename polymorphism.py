class Test:
    def show(self,a):
        print(a)

    def show(self,a,b):
        print(a)


t = Test()
t.show(10,12)

# this is method overloading which python doesnt support same function with diff parameter python only considers the function nearby object only

class boys:
    def show(self):
        print("abe oiii")
    
class girls:
    def show(self):
        print("slayyyy")

b = boys()
g = girls()
b.show()
g.show()
# method overriding just class change same function with same parameters
