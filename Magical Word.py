def isprime(n, i = 2):
    # Base cases
    if (n <= 2):
        return True if(n == 2) else False
    if (n % i == 0):
        return False
    if (i * i > n):
        return True
    return isprime(n, i + 1)

def find_next_prime(n):
   # Not sure if you want this line or not
   # if isprime(n):
   #   return n

   low = n - 1
   high = n + 1
   while True:
      if isprime(low):
         return low
      elif isprime(high):
         return high
      else:
         low -= 1
         high += 1


for i in range(int(input())):
    n=int(input())
    s=input()
    s=list(s)
    for j in range(n):
        s[j]=ord(s[j])
        if s[j] < 65:
            s[j] = 65

        ans=isprime(s[j])
        if ans:
            s[j]=chr(s[j])
        else:
            if s[j] > 120:
                s[j] = 120
            pic=find_next_prime(s[j])
            s[j]=chr(pic)

    print("".join(s))



