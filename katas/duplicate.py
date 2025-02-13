
def duplicate(word):
    word2 = list(word)
    word3 = []
    for x in word2:
        if word.count(x) > 1:
            word3.append(")")
        else:
            word3.append("(")
    answer = ''.join(word3)
    return answer
# duplicate("Ball")

# https://www.codewars.com/kata/highest-and-lowest
def high_and_low(numbers):
    x = numbers.replace(" ","")
    y = list(x)
    a = max(y)
    b = min(y)
    answer = str(a) + " " + str(b)
    print(answer)
# high_and_low("2 7 6")

# https://www.codewars.com/kata/two-sum/python
def two_sum(numbers, target):
    foo = []
    for num in numbers:
        value = target - num
        foo.append(value)
    y = [numbers.index(x) for x in foo if x in numbers]
    print(y)
# two_sum([5,2,9,6],7)
#
# https://www.codewars.com/kata/555eded1ad94b00403000071/train/python
def series_sum(n: int) -> float:
    value = []
    i = 1
    while i < n:
        value.append(i/n)
        n = n + 1
    print(value)
# series_sum(9)

def reverse(x: str) -> str:
    x_list = list(x)
    x_list.reverse()
    x_str = ''.join(x_list)
    return x_str
reverse("Bugle")

def validate_pin(input):
    if len(input) == 4 and input.isdigit():
        return True
    else:
        return False
validate_pin("Mort")

# kata: https://www.codewars.com/kata/iq-test/train/python
def iq_test(numbers):
    no_space = numbers.replace(" ","")
    list_form = list(no_space)
    output = [list_form.index(num) for num in list_form if int(num) % 2 == 0]
    for x in output:
        x = x + 1
        return x
# iq_test("4 6 5 2 8 9")

# kata: https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
def disemvowel(string):
    vow = ["a","e","i","o","u"]
    revised = []
    for x in string:
        if x in vow:
            pass
        else:
            revised.append(x)
    output = ''.join(revised)
    print(output)
# disemvowel("Test that function")

# kata: https://www.codewars.com/kata/form-the-largest/train/python
def get_big(n):
    foo = [int(x) for x in str(n)]
    foo.insert(0, foo.pop(foo.index(max(foo))))
    print(foo)
# get_big("21538")

# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#       break
#   i = i + 1

# kata: https://www.codewars.com/kata/bumps-in-the-road/train/python
def bump_checker(road):
    if road.count("n") < 16:
        return "Woohoo!"
    else:
        return "Car Dead!"

bump_checker("none")

# kata: https://www.codewars.com/kata/counting-array-elements/train/python
def unique_counter(list):
    solo = set(list)
    y = [list.count(x) for x in solo]
    z = {(key, value) for (key, value) in zip(solo, y)}
    return z
# unique_counter(["Bob","Joe","Bob"])

# https://www.codewars.com/kata/58223370aef9fc03fd000071/train/python
def dashatize(num):
    num_list = [int(d) for d in str(num)]
    dashed_list = []
    for x in num_list:
        if x % 2 == 0:
            dashed_list.append(x)
        else:
            x = "-"+ str(x) + "-"
            dashed_list.append(x)
    answer = ''.join(str(n) for n in dashed_list)
    return answer
# dashatize(43264)

# https://www.codewars.com/kata/the-highest-profit-wins/train/python
def min_max(lst):
    output_lst = []
    lst.sort()
    output_lst.append(lst[0])
    output_lst.append(lst[-1])
    print(output_lst)
# min_max([34,23,19,88,53])

# https://www.codewars.com/kata/find-the-unique-number-1/train/python
def find_uniq(arr):
    arr_set = set(arr)
    if arr.count(n) != 1:
        for n in arr_set:
            pass
        else:
            return n

# https://www.codewars.com/kata/meeting/python
def meeting(s):
    s_upper = s.upper()
    s_list = s_upper.split(',')
    print(s_list)

# meeting("Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill")

def index_function(word):
    caps = []
    foo = [caps.append(word.index(x)) for x in word if x.isupper()]
    return ordered(caps)

# index_function("DiffTesP")

# kata: https://www.codewars.com/kata/58e0f0bf92d04ccf0a000010/train/python
def lost_sheep(friday: list, saturday: list, total: int):
    friday_sheep = sum(friday)
    saturday_sheep = sum(saturday)
    all_seen_sheep = int(friday_sheep) + int(saturday_sheep)
    all_unseen_sheep = total - all_seen_sheep
    return all_unseen_sheep
# lost_sheep([93,3],[22,9],134)

# https://www.codewars.com/kata/rot13-1/train/python
def rot13(message: str):
    alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
    alph_dict = {k: v for v, k in enumerate(alphabet)}
    for x in message:
        if x in alph_dict:
            print(alph_dict.get(x))

# rot13("test")

# kata: https://www.codewars.com/kata/thinkful-string-drills-repeater/python

def repeater(string, number):
    return string * int(number)

# kata: https://www.codewars.com/kata/rotate-for-a-max/train/python

def max_rot(num: int):
    store = []
    #
    num_to_str = str(num)
    str_to_list = list(num_to_str)
    str_to_list.insert(len(str_to_list),str_to_list[0])
    str_to_list.pop(0)
    store.append(str_to_list)
    print(store)



# max_rot(5832)
# kata: https://www.codewars.com/kata/find-the-stray-number/train/python
def stray_num(nums):
    assert len(nums) % 2 != 0
    x = [n for n in nums if nums.count(n) == 1]
    return int(x[0])
# stray_num([4,5,5])


# kata: https://www.codewars.com/kata/highest-scoring-word/train/python
def highest_word(arr):
    from itertools import count
    from string import ascii_lowercase
    assert isinstance(arr,str)
    foo = arr.split()
    letter_mapping = dict(zip(ascii_lowercase, count(1)))
    new = []
    for x in foo:
        val = [letter_mapping[letter] for letter in x.lower() if letter in letter_mapping]
        new.append(sum(val))
    answer = [y for y in foo if foo.index(y) == new.index(max(new))]
    return answer[0]



def clean_plant(str):
    str_list = str.split()
    del str_list[:2]
    clean_plt = ' '.join(str_list)
    return clean_plt

# split_test('047 - San Diego Inspiration Point')

# https://www.codewars.com/kata/equal-sides-of-an-array/train/python
def find_even_index(arr):
    arr_rev = arr[::-1]
    z = []
    for x,y in zip(arr,arr_rev):
        z.append(x+y)
    sorted_z = sorted(z)
    length = len(z)
    index = (length -1) // 2
    print(index)

# find_even_index([40,9,-6,3,4,19,11])

# kata: https://www.codewars.com/kata/testing-1-2-3/train/python
def testing(lines):
    presidents = lines
    for num, name in enumerate(presidents, start=1):
        print("President {}: {}".format(num, name))

# testing(["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"])


# kata: https://www.codewars.com/kata/compare-strings-by-sum-of-chars/train/python
def compare(s1,s2):
    a = list(s1.upper())
    b = list(s2.upper())
    v1 = sum(map(lambda x: ord(x),a))
    v2 = sum(map(lambda x: ord(x),b))
    if v1 == v2:
        return True
    else:
        return False
# compare("AA","AA")

# kata: https://www.codewars.com/kata/write-number-in-expanded-form/train/python
def expanded_form(num):
    num_str = str(num)
    base = "0"
    starting = len(num) - 1
    add_zero = list(map(lambda x: x + (base * starting),list(num)))
    print(add_zero)

# expanded_form("brand")
# kata: https://www.codewars.com/kata/format-a-string-of-names-like-bart-lisa-and-maggie/train/python
def nameList(names):
    foo = []
    for x in names:
        foo.append(names.get(x))
    output = " & ".join([", ".join(foo[:-1]),foo[-1]])
    return output


foo = {'blue' : '42','red' : '18','green' : '18'}
# nameList(foo)

# kata: https://www.hackerrank.com/challenges/np-shape-reshape/problem
import numpy as np

def reshape(arr):
    foo_bar = arr.replace(" ","")
    foo = list(foo_bar)
    print(np.reshape(foo,[3,3]))

# reshape("4 3 2 6 9 8 1 5 5")

# np.random.seed(42)
# rand =  np.random.random(size=4)
# heads = rand > 0.5
# print(heads)

# kata: https://www.codewars.com/kata/make-a-function-that-does-arithmetic/train/python
def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    else:
        return a / b

# arithmetic(5,3,"add")
# arithmetic(5,3,"divide")
# arithmetic(9,3,"foo")

# kata: https://www.codewars.com/kata/beginner-series-number-3-sum-of-numbers/train/python
def get_sum(a,b):
    print(sum(list(range(a,b + 1))))
# get_sum(0,-1)

def xo(s):
    ls = list(s)
    exes = []
    ohs = []
    for i in ls:
        if i == "x":
            exes.append(i)
        elif i == "o":
            ohs.append(i)
        elif i == "X":
            exes.append(i)
        elif i == "O":
            ohs.append(i)
    if len(exes) == len(ohs):
        return True
    else:
        return False
# xo("xxoo")

def find_longest(arr):
    z = []
    for x in arr:
        z.append(len(str(x)))
    for y in arr:
        if len(str(y)) == max(z):
            return y
find_longest([33,462,31])

# kata: https://www.codewars.com/kata/remove-anchor-from-url/train/python
def remove_url_anchor(url):
    lst = list(url)
    foo = [lst.index(x) for x in lst if x == "#"]
    x = foo[0]
    y = slice(0,x)
    return url[y]

# remove_url_anchor("www.espn.com#test")


items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
# print(squared)

wo = [500,325,4353,324,904]
misc_cost = list(map(lambda x: x*.15, wo))
# print("Miscellaneous costs for Macerich in November: " + str(sum(misc_cost)))

def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))

# order("let4 6us 9try")

def kebabize(string):
    s = string.split()
    s2 = '-'.join(s)
    return s2.lower()

# kebabize("This is a test")

# kata: https://www.codewars.com/kata/statistics-for-an-athletic-association/python

def stat(strg):
    strg_splt = strg.split()
    cln = [word.rstrip(",") for word in strg_splt]
    x = cln[0]
    y = x.split("|")

    team_times = []

    def time_work(time):
        hr_sec = int(time[0]) * 3600
        min_sec = int(time[1]) * 60
        time_num = hr_sec + min_sec + int(time[2])
        team_times.append(time_num)

    time_work(y)
    print(team_times)

# kata: https://www.codewars.com/kata/square-every-digit/train/python
def square_digits(num):
    num_s = [int(x) for x in str(num)]
    sq = list(map(lambda y : y ** 2, num_s))
    x = [str(i) for i in sq]
    ans = int(''.join(x))
    return ans
# square_digits(5523)
def comp(array1, array2):
    import math
    comp_arr = list(map(lambda x : x * x, array1))
    sorted1 = comp_arr.sort()
    sorted2 = array2.sort()
    if sorted1 == sorted2:
        return True
    else:
        return False

# comp([4,5,6],[16,25,36])

# kata: https://www.codewars.com/kata/extract-the-domain-name-from-a-url-1/train/python
def domain_name(url):
    import re
    x = re.split(r"\.|\/", url)
    clean_x = ' '.join(x).split()
    return clean_x[1]

# domain_name("https://espn.com")

# kata: https://www.codewars.com/kata/539ee3b6757843632d00026b/train/python
def capitals(word):
    list_word = list(word)
    z = [list_word.index(y) for y in list_word if y.islower() == False]
    answer = set(z)
    foo = sorted((list(answer)))
    print(foo)
# capitals("nnnYXsagU")

# kata: https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c
def sort_by_length(arr):
    try:
        print(sorted(arr,key=len))
    except:
        print("Input did not work with function")
# sort_by_length(["44","forty"])

# kata: https://www.codewars.com/kata/summing-a-numbers-digits/train/python
def sum_digits(number):
    values = list(map(int, str(number)))
    return sum(values)


# sum_digits(542)

# a = input("Is your car silent when you turn the key? Please answer with 'Y' or 'N'")
# if a == "Y":
#     b = input("Are the battery terminals corroded?")
#     if b == "Y":
#         print("Clean terminals and try again")
#     elif b == "N":
#         print("Replace cables and try again")
# elif a == "N":
#     c = input("Does the car make a clicking noise?")
#     if c == "Y":
#         print("Replace the battery")
#     elif c == "N":
#         d = input("Does the car crank up but fail to start?")
#         if d == "Y":
#             print("Check the spark plug connections")
#         elif d == "N":
#             e = input("Does the engine start and then die?")
#             if e == "Y":
#                 f = input("Does your car have fuel injection?")
#                 if f == "Y":
#                     print("Get it in for service")
#                 else:
#                     print("Check to ensure the choke is opening and closing")


def phone_number(digits: list) -> str:
    assert len(digits) == 10
    # add parentheses
    par1 = "("
    par2 = ")"
    digits.insert(0,par1)
    digits.insert(4,par2)
    # add space and dash
    space = ' '
    dash = "-"
    digits.insert(8,dash)
    digits.insert(5,space)
    number = ''.join(str(x) for x in digits)
    return number


# phone_number([1,2,3,5,5,6,6,3,2,3])
import random
service_providers = ['MaxGen','Bay4','SST']
print(random.choices(service_providers, weights = [4, 3, 3], k = 20))
