def get_gcd(a,b):
    if b==0:
        return a
    else:
        return get_gcd(b,a%b)

a=int(input())
b=int(input())
print(get_gcd(a,b))
