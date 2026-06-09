
from time import sleep
from threading import Thread

class A(Thread):
    def run(self):
        for i in range(3):
            print("PUNE")
            

class B(Thread):
    def run(self):
        for i in range(3):
            print("MIT")
            

t1 = A()
t2 = B()

t1.start()
t2.start()

t1.join()
t2.join()
