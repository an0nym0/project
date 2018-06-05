# inp = int(input("Insert some value"))
# inp_with_nalog = inp * 1.18
# print("Price with tax will be %s" % inp_with_nalog)
# import pdb as ipdb;
# a = 3
# b = 3.2
# #b = str(3.2)
# c = "John Smith"
# d = "Learn"
# e = str(b) + c
# print(e)
# print(len(c))
# print(e[:4])
#print(a + c)
#print(c + d)

# l1 = ['abcd', 786, 2.23, 'john', 70.2]
# print(l1)
# print(l1[0])
# print(l1[3:])
# l10 = l1 * 2
# print(l10)
# l2 = ['second', '123']
# l3 = list()
# l3.append(l1)
# l3.append(l2)
# print(l3)
# l1[1] = 666
# l3 = [l1, l2]
# print(l3)
#
# l4 = l2
# l2[0] = '321'
# print(l4)

# l5 = [111, 222, 333, 444]
# l55 = slice(0,2)
# print(l5[l55])
# copyofl55 = l55[:]
# print(copyofl55)
#
# l6 = [l1, l2, l5]
# l1[0] = 6161
# print(l6)

# Create list l4, that contains all elements of l2. Updated l2[0] value. Print l4.
# Create list l5 with 4 elements.
# –Using slice operator, update first 2 items to have values ‘1’ and ‘2’.
# –Insert list [7,7,7,7,7,7] after value ‘1’
# –Insert a copy of itself at the beginning.
# –Clear list
# Create list l6 that has l1, l2, l5 elements as list. Update first element of list l1. Print l6

# l1 = [1, 2, 3, 4, 5]
# l2 = l1[:2]
# print(l1); print(l2)
# print(l1 == l2)
# l2[0] = 5
# print(l1, l2)
# str1 = "string1"
# # str1[3] = "1"
# l1.append("new string1")
# print(l1)
# l1.extend(l2)
#
# ipdb.set_trace()
# l1.pop()

# tuple = ('abcd', 786, 2.23, 'john', 70.2)
# tuple[2] = 1000


# l1 = [1,2,3,4,5]
# lenght = len(l1)
# counter = 0

# pos = 10
# for ind, val in enumerate(l1):
    # print(ind, l1[ind])

# for key in range(pos):
    # print(key)


# while counter < lenght:
    # print(l1[counter])
    # counter+=1
    # for key in l1:
    #     print(l1)
    # pass
# for key in l1:
#     print(key)
#     if key == 3:
#         continue
#         print("Broken!")
        # break

# Having a(3), b(‘test’), c([1,2,3]), d(‘none’), e(None), f(0) what will be the values for the following operations:
#     –a or b; a and b; a and c; a and d; b or d; a and e; a and f
# Create a program that sets a value to a variable.
# It should print ‘Yes’ if the variable is number and the number is greater than 5.
# Prints ‘String’ if the variable is string.
# Prints ‘No’ if the variable is number and less than 5. Prints ‘other’ if the variable is nor string nor number.
# Having list l1, print each element of the list on a line. Use for with range, enumerate and zip options.
# Using while, print all the even values between 5 and 47.
# Update program above to skip values 20, 24, 36.

a = 3
b = 'test'
c = [1,2,3]
d = 'none'
e = None
f = 0
print(a or b, a and b, a and c, a and d, b or d, a and e, a and f)

assert (a or b)
assert (a and b)
assert (a and c)
assert (a and d)
assert (b or d)
assert (a and e, "Result is False!")
assert (a and f, "Result is False!")
