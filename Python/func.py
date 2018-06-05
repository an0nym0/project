# def f1(x, y=[], *args, **kwargs):

# def f1(arg1=6):
#     """f1 docstring"""
#     arg1+=1
#     print(arg1)
#     return

# def f2(arg1=[]):
#     """f2 docstring"""
#     arg1.append(1)
#     print(arg1)
#     return

# def f3(*args):
#     print(sum(args))

# x1 = 5

# def f4(**kwargs):
#     global x1
#     x1 = kwargs.get("key2")
#     print(x1)


# f1();f1();f1()
# f2();f2();f2()
# print(f2)
# f1("x", 5, 1,2,3,4,"erg", key1="val1")

# f3(1)
# f3(1,2,3)
# f3(*tuple(range(15)))

# t1 = (1,2,3)
# x,y,z = t1
# print(t1)
# print(*t1)
# print(x1)
# f4(key2="val2")
# print(x1)

from decimal import Decimal

def print_even(arg1=range(-1,101)):
    for x in arg1:
        if isinstance(x, int):
            if not x % 2:
                print(x, end=' ')
    print()

print_even(range(1,11))
print_even()

vat = 0.18

def vat_price_calc(price=Decimal(0)):
    if not isinstance(price, Decimal):
        price = Decimal(price)
    global vat
    price = price + price * Decimal(vat)
    vat = 0.25
    return price
    # return price + price * Decimal(vat)

print(vat_price_calc(5))
print(vat)
print(vat_price_calc(5))