import operator
d={'apple':20,'orange':10,'mango':12}
print("orginal dictionary")
print(d)
print("ascending")
sdk=sorted(d.items(),key=operator.itemgetter(0))
print(sdk)
print("descending")
sdk=sorted(d.items(),key=operator.itemgetter(0),reverse=True)
print(sdk)
