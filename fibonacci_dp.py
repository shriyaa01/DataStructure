cache=[None]*(100)
def fibonacci(n):
    if n<=1:
        return n
    if not cache[n]:
        cache[n]=fibonacci(n-1)+fibonacci(n-2)
    return cache[n]

num=int(input("Enter the number you want fibonacci of:"))
ans=fibonacci(num)
print(ans)