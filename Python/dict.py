d1 = {}
d2 = dict(((1,2), (3,4)))
d3 = {"key":"value1"}
for key in d3:
    print("d3[%s] is %s" %(key, d3[key]))

print(d1, d2)
val1 = d2.get(3,"Not found")
print(val1)