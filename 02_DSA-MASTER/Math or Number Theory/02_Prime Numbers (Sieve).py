class Solution:
    def sieveOfEratosthenes(self, N):
        #code here 
        # primes =[]
        # is_prime = [True] *(N+1)
        # for i in range(2, N + 1):
        #     if is_prime[i]:
        #         primes.append(i)

        #         for j in range(i * i, N + 1, i):
        #             is_prime[j] = False

        # return primes

        primes = []
        is_prime = [True] * (N+1)

        for i in range(2, N+1):
            if is_prime[i]:
                primes.append(i)

                for j in range(i*i, N+1, i):
                    is_prime[j] = False
        return primes
    



obj = Solution()
print(obj.sieveOfEratosthenes(100))



from math import sqrt

n = 11

is_prime = False
if n < 2:
    is_prime = True

arr = []
for i in range(2, int(sqrt(n))+1):
    is_prime = True
    # arr.append(i)

    if i % n == 0:
        is_prime = False
        break
print(is_prime, arr)