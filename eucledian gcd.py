def get_gcd(a,b):
   while b:
       a,b = b,a%b
   return a

numbers = [18,24,36]
gcd = get_gcd(numbers[0], numbers[1])
for i in range(2, len(numbers)):
    gcd = get_gcd(gcd, numbers[i])

print(gcd)
