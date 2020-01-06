# def square_digits(num):
#
#     for i in str(num):
#         square = int(i) * int(i)
#         print(square,end='')
#
# square_digits(9119)
#
# def square_digits(num):
#     a=''
#     for i in str(num):
#         square = int(i) * int(i)
#         a += str(square)
#     print(int(a))
# #
# # square_digits(9119)
# def square_digits(num):
#     ret = ""
#     for x in str(num):
#         ret += str(int(x)**2)
#     return int(ret)
# #
# # def square_digits(num):
# #     list = []
# #     input().split().append(list)
# #     for i in list:
# #         square = i * i

''' 输出一串数字的单独的平方'''
def square_digits(num):
    a=''
    for i in num:
        print(i)
        square = i*i
        a += str(square)
    print(int(a))

# square_digits(9119)

''' Given two integers a and b, which can be positive or negative, 
find the sum of all the numbers between including them too and return it. 
If the two numbers are equal return a or b.'''

def w_get_sum(a,b):
    # good luck!
    if a != b:
        sum = 0
        l = list(range(a,b+1))
        for x in l:
            sum += x
        print(sum)
    else:
        print(a)
# Test.assert_equals(get_sum(0,-1),-1)
def get_sum(a,b):
    sum=0
    if a==b:
        print(a)
    elif a > b:
        for i in range(b,a+1):
            sum += i
        print(sum)
    else:
        for i in range(a,b+1):
            sum += i
        print(sum)

def get_sum(a,b):

    return sum(range(min(a, b), max(a, b) + 1))
    # print(sum(range(min(a, b), max(a, b) + 1)))

#
# get_sum(0,-1)
# get_sum(1,4)
# get_sum(-2,2)
# get_sum(-3,1)
# get_sum(2,2)


# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
#

def accum(s):
    accum = []

    for index,i in enumerate(s):
        # print(index,i)
        result = i.upper()+i.lower()*index
        accum.append(result)

    print('-'.join(str(a) for a in accum))

2
# accum('AbCdE')
# # accum('xyz')

# "din"      =>  "((("
# "recede"   =>  "()()()"
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])


def w_duplicate_encode(word):
    words = {}
    #your code here
    for w in word:
        a = word.count(w)

        print(a)
        if word.count(w) == 1:
            word_new = word.replace(w,"(")

        else:
            word_new = word.replace(w,")")

    print(word_new)

# duplicate_encode('din')
# duplicate_encode('redede')

# [[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]
import operator
def openOrSenior(data):
    results = []
    # Hmmm.. Where to start?
    for member in data:
        # print(member)
        # print(type(member))

        if member[0] > 55 and member[1] > 6:
            results.append('Senior')
        else:
            results.append('Open')
    print(results)

def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]

# openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]])
# openOrSenior([[16, 23],[73,1],[56, 20],[1, -1]])


def square_digits1(num):
    result = ''
    for i in str(num):
        result += str(int(i)**2)
    return (result)
# square_digits1(9119)



# Kata.getMiddle("test") should return "es"
# Kata.getMiddle("testing") should return "t"


def get_middle(s):
    # print(len(s))
    a = [i for index,i in enumerate(s)]
    #print(a)
    # [print(i,i-1)i if index%2 == 0 else i for index,i in enumerate(s)]
    if len(s)%2 == 0:# 是偶数个字母
        b = a[int(len(s)/2-1)]
        c = a[int(len(s)/2)]
        return b+c
    else:  # 奇数个字符
        return a[int((len(s)-1)/2)]

def get_middle1(s):
    return s[(len(s) - 1) / 2 : len(s) / 2 + 1]

    # (a[int(len(s)/2-1)]+a[int(len(s)/2)] if len(s)%2 == 0 else a[int((len(s)-1)/2)] for a=[i for index,i in enumerate(s)])

# get_middle("test")
# get_middle("testing")

# ([0,0,0,1]), 1)
# ([0,0,1,0]), 2)
# ([1,1,1,1]), 15)
# 1, 0, 0, 1, 0, 0, 0, 1, 0, 1=581
#Tests [1, 1, 1, 1, 1, 0, 1, 0, 0, 0] ==> 1000
def binary_array_to_number(arr):
    # return(
    #     arr[0]*(2**(len(arr)-1))+arr[1]*(2**(len(arr)-2))+arr[2]*(2**(len(arr)-3))+arr[3]*(2**(len(arr)-4))
    # )
    sum = 0
    n = 0
    while n < len(arr):
        a = arr[n]*(2**(len(arr)-(n+1)))
        sum += a
        n += 1
    print(sum)



binary_array_to_number([0,0,0,1])
binary_array_to_number([0,0,1,0])
binary_array_to_number([1,1,1,1])
binary_array_to_number([1, 0, 0, 1, 0, 0, 0, 1, 0, 1])
binary_array_to_number([1, 1, 1, 1, 1, 0, 1, 0, 0, 0])