# first,second,third = [int(input())for i in range(3)]
# print (first)

# print(max([n for n in [int(input()) for i in range(int(input()))] if not n%4]))
# first, second, third = [int(input()) for i in range(3)]
# print (first)

# print(round(8.5,))

# a,b,l,n = [int(input())for i in range(4)]
#
# print((a*n)+(2*(b*(n-1)))+l*2)
# number = float(input())
#
#
#
# print(number%1)

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#
#     print()
#

# n = int(input())
# for n1 in range(1,n+1):
#     for num in range(1,n1+1):
#         print(num,end=" ")
#     print()


def sum_all(*numbers):
    result = 0
    print(numbers[0])
    for number in numbers:
        result += number
    return result


print(sum_all(*range(10)))
