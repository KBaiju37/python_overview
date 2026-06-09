def my_deco(say_hello):
    def wrapper():
        print("before call line hello")
        say_hello()
        print("after calling hello")
    return wrapper


@my_deco
def say_hello():
    print("Hello Team")

say_hello()

def sumof(func):
    def wrapper(a, b):
        func(a, b) 
        print(f"Printing the sum from decorator: {a + b}")
    return wrapper

@sumof
def sum_func(a, b):
    print("print the sum (inside the main function)")

sum_func(10, 20)

def deco(func):
    def wrapper(a):
        func(a)
        print(a.upper())
    return wrapper

@deco

def upperof(a):
    print(f"convert {a}")

upperof("hello")


def decomul(func):
    def wrapper(a,b):
        func(a,b)
        c = a*b
        print(f"multiplication of {a} & {b} = {c}")

    return wrapper

@decomul

def dhruv(a,b):
    print("give the multiplication of the two")

dhruv(100,200)

def check_login(func):
    def wrapper(is_logged_in, *args, **kwargs):
        if is_logged_in:
            print("Access Granted: User is logged in.")
            return func(*args, **kwargs)
        else:
            print("Access Denied: You must be logged in to view this page.")
            return None
    return wrapper


@check_login
def view_dashboard(username):
    print(f"Welcome to your dashboard, {username}!")

view_dashboard(True, "Alice")

print("-" * 30)

view_dashboard(False, "Bob")

#create a decorator which accepts the only positive number
def dec(func):
    def wrapper(a):
        if a>



