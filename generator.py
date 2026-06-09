#generator is a special type of function that allows generate u to generate a value one at a time instaed of returning all at ones
# dont store everything in memory,generate on demand
# saves memory -> useful for large datasets
# faster execution for streaming data
# easy to implement iterators


def even_numbers(n):
    for i in range(n+1):
        a=i**2 
        if a %2==0 and a in range(n+1):
            yield a

g = even_numbers(4)
print(next(g))
print(next(g))

def empid(n):
    for i in range(n,1000):
        if i >= 100:
            print(f"empid is :{i}")
            yield i

a=empid(100)
print(next(a))
print(next(a))    
