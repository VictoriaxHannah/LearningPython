small = int(input("Minumum number for range: "))
large = int(input("Maximum number for range: "))
primes = []

def Prime(n):
    for n in range(small,large + 1):
       if n > 1:
           for i in range(2,n):
               if (n % i) == 0:
                   break
           else:
               primes.append(n)

Prime(large)
 
print("\nThere are",len(primes),"prime numbers between",small,"and",large)
print("The numbers are:",primes)
