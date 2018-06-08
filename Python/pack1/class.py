class C1(object):
    '''Dockstring for class'''

    field1 = "string1"
    field2 = 5

    def method1(self, param1=[]):
        self.param1 = param1
        print(self.param1)

    def __init__(self, *args, **kwargs):
        self.field1 = kwargs.get("field1")
        self.field2 = kwargs.get("field2")

    def __repr__(self):
        return "{}: class {}: {}; {}".format(self.__module__, self.__class__.__name__, self.field1, self.field2)

i1 = C1(field1="f1", field2="f2")
print(i1)
# i1.method1()