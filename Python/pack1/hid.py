

class E(object):
    empCount = 0
    emps = []

    def __init__(self):
        self.empCount += 1
        self.emps.append(self)

e1 = E()
e2 = E()

e1.age = 31

def salary(self):
    return self.age + 100

e1.salary = salary

print(E.empCount)
print(E.emps)
print(e1.emps, e2.emps, e1.empCount)

print(e1.age)
print(e1.salary(e1))

if hasattr(e2, "age"):
    print(e2.age)

del(e1)
# print(e1.age)