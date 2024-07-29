"""
დავალება 5

პირველი ექვსი მარტივი რიცხვია: 2, 3, 5, 7, 11, 13. მარტივი შესამჩნევია, რომ მე-6
მარტივი რიცხვია 13. რა იქნება ამ მიმდევრობის მეოციათასე (20000-st) წევრი.
(მოცემული დავალება უნდა შესრულდეს უშუალოდ Python-ით, დამატებითი
ბიბლიოთეკების გამოყენების გარეშე)
"""


def sieve_of_eratosthenes(limit):
    """Generate a list of prime numbers up to 'limit'
     using the Sieve of Eratosthenes algorithm."""
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False
    p = 2
    while p * p <= limit:
        if prime[p]:
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1
    return [p for p in range(limit + 1) if prime[p]]


def find_nth_prime(n):
    limit = 400000  # upper limit
    primes = sieve_of_eratosthenes(limit)
    if len(primes) >= n:
        return primes[n - 1]
    else:
        raise ValueError("Increase the limit! not enough primes found.")


nth_prime = find_nth_prime(20000)
print(nth_prime)
