# student = {
#     'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']
# }

# # # student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})
# # # student['phone'] = '555-5555'
# # # student['name'] = 'Jane'
# # # del student['age']
# # # age = student.pop('age')

# # # # print(student.get('phone', 'Not Found'))
# # # print(student)
# # # print(age)

# # # print(len(student))
# # # print(student.keys())
# # # print(student.values())
# # # print(student.items())

# for key, value in student.items():
#     print(key, value)

# print()

# locations = {
#     'name': 'rexburg',
# }

# print(locations)

capitals = {
    'USA':'Washington D.C.',
    'India': 'New Delhi',
    'China': 'Beijing',
    'Russia': 'Moscow'
}

print(capitals.get("USA"))
print(capitals.get("India"))

# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital does not exist.")

capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()
keys = capitals.keys()
values = capitals.values()

print(capitals)
# print(keys)
# print(values)

# for key in capitals.keys():
#     print(key)

# for value in capitals.values():
#     print(value)

items = capitals.items()
print(items)

for key, value in capitals.items():
    print(key, value)