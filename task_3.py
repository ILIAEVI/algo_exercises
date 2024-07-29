from math import factorial

"""
დავალება 1

2 X 2 ბადეში მოძრაობას ვიწყებთ მაღლა მარცხენა
კუთხიდან და ვამთავრებთ დაბლა მარჯვენა კუთხესთან. თუ დავაკვირდებით
დავინახავთ, რომ ამ გზის გასავლელად არსებობს 6 სხვადასხვა გზა.
რა იქნება ერთმანეთისგან განხსვავებული გზების რაოდენობა თუ 2 X 2 -ბადის
მაგივრად მოძრაობას დავიწყებთ 20 X 20- ბადეში.
"""


def number_of_paths(x):
    return factorial(2 * x) // (factorial(x) * factorial(x))


n = 20

print("Number of unique paths in a 20x20 grid:", number_of_paths(n))
