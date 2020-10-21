def autocomplete(input_, dictionary):
    length = len(input_)
    for x in dictionary:
        if x.isalpha() == True:
            pass
        else:
            x = ''
    answer = [word for word in dictionary if word[:length] == input_]
    print(answer)
# autocomplete('ai', ['airplane','airport','apple','ball'])

def duplicate_sandwich(arr):
    base = range(0, len(arr))
    joined = zip([arr.index(a) for a in arr], base)
    for member in joined:
        if member[0] != member[1]:
            front, back = member[0] + 1, member[1]
            slice = arr[front:back]
            return slice

# duplicate_sandwich(["hi","hey", "hello","howdy","hey"])
from itertools import groupby
from operator import itemgetter
def remove_duplicate_words(s):
   answer = ' '.join(map(itemgetter(0), groupby(s.split())))
   print(answer)
# remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta")

def remove_parentheses(s):
    first = s.split('(')
    last = s[::-1]
    end_last = last.split(')')
    product = ''.join([first[0], end_last[0][::-1]])
    return product

# remove_parentheses("hello(exm(p)l)heyoo")

from collections import Counter
def repeats(arr):
    count = Counter()
    for item in arr:
        count[item] += 1
    singles = []
    for key, value in count.items():
        if value == 1:
            singles.append(key)
    return sum(singles)

# repeats([9, 10, 19, 13, 19, 13])

def string_task(s):
    vowels = ["a", "o", "y", "e", "u", "i"]
    list_s = list(s.lower())
    transformed = []
    for item in list_s:
        if item in vowels:
            pass
        else:
            transformed.append("." + item)
    answer = ''.join(transformed)
    return answer    

# string_task("Codewars")

