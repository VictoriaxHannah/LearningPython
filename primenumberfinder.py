small = int(input("Enter minumum number for range: "))
large = int(input("Enter maximum number for range: "))
primes = []

for num in range(small,large + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           primes.append(num)

print("\nThere are",len(primes),"prime numbers between",small,"and",large)
print("The numbers are:",primes)
