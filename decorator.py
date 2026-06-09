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