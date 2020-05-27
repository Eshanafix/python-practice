#Hello :)

li = [9,1,8,2,7,3,6,4,5,]

s_li = sorted(li)
print(f'{s_li} <--> {li}')

#li.sort()
print(li)

s_li = sorted(li, reverse= True)
print(s_li)

tup = (9,1,8,7,3,7,3,6,4,5,)
s_tup = sorted(tup)
print(s_tup)

student = {"name" : "John", "age" : 25, "courses": ["math", "comp sci"]}
s_di = sorted(student)
print(s_di)


lis = [-6,-5,-4,1,2,3]
print(lis)
sorted(lis)
print(lis)

#abs attribute
s_lis = sorted(lis, key=abs)
print(s_lis)

