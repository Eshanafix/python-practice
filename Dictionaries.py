
#Dictionary, hashmaps?
student = {"name" : "John", "age" : 25, "courses": ["math", "comp sci"]}
student["phone"] = "555-555"
print(student)
print(student["name"])
print(student["courses"])
print(student.get("name"))
print(student.get("phone" , "not found"))
student["name"] = "Akbar"
print(student)
student.update({"name": "ya", "age" : 26})
print(student)

del student["age"]
print(student)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key,value)
