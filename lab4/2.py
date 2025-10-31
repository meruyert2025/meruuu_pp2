n=str(input())
a=["a","e","o","y"]

def m(n):
    for i in n:
        if i in a:
            continue
        yield i
            

        
for i in m(n):
    print(i)
