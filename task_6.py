from sympy import primerange
from math import log

"""
დავალება 2

რა იქნება X-რიცხვისვის, ყველა მარტივი გამყოფი რიცხვის ჯამი
"""


def prime_exponents_in_binomial(n, k, p):
    exp_n = sum(n // p ** i for i in range(1, int(log(n, p)) + 1))
    exp_k = sum(k // p ** i for i in range(1, int(log(k, p)) + 1))
    exp_nk = sum((n - k) // p ** i for i in range(1, int(log(n - k, p)) + 1))
    return exp_n - exp_k - exp_nk


def sum_of_prime_factors_binomial(n, k):
    prime_sum = 0
    for p in primerange(2, int(n ** 0.5) + 1):
        if prime_exponents_in_binomial(n, k, p) > 0:
            prime_sum += p

    return prime_sum


a = 20000000
b = 15000000

result = sum_of_prime_factors_binomial(a, b)
print(f"The sum of all unique prime factors of the binomial coefficient is: {result}")
