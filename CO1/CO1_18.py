dict1={"name":'Aswin',"age":18}
dict2={"class":'mca',"year":2021}
print("Dictionary 1=",dict1)
print("Dictionary 2=",dict2)
d=dict1.copy()
d.update(dict2)
print("Merged dictionary",d)
