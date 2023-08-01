## Sieve of Eratosthenes
# This algorithm extracts only the prime numbers from a list of given natural numbers.
# The Sieve of Eratosthenes algorithm finds primes up to a number, say 50, by eliminating every multiple of a prime number (starting from 2).
# It also assumes that every number between 2 and 50 is a prime number (even though they are actually not prime). 
# Hence, all the multiples of a number (except the number itself) must be discarded from the list.
# The process is continued until all the actual non-prime numbers are discarded from the list.

# Initial Solution (uns in O(n^2) time)
n = int(input("Please enter a number until which you need all primes: "))
n = 50 # As a base case, we use 50
primes = [i for i in range(2, n + 1)]  
print("Before discarding:", primes)
for i in range(len(primes)):
  current_prime = primes[i]
  if current_prime != 0:   
    for j in range(current_prime + i, len(primes), current_prime):
      primes[j] = 0
print(primes)

## Alternative solution (also runs in O(n^2) time)
primes = [i for i in range(n + 1)]
print(primes)
for prime in range(2, len(primes)):
  current_prime = prime
  if current_prime != 0: 
    for i in range(current_prime * 2, len(primes), current_prime):
      primes[i] = 0  
print(primes[2:])