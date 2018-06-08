from list import l1
from traceback import print_exc

try:
    for pos, val in enumerate(l1[:]):
        if not val % 2:
            l1.pop(pos)
    #    print(l1)
    print(l1)



except IndexError as e:
    print("error is: %s" % e)