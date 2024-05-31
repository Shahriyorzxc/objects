# person = [{
#     'name': 'Ali',
#     'age': 25,
#     'friend': {
#         'name': 'Ali',
#         'age': 24,
#         'friend': {
#             'name': 'Shoxruh',
#             'age': 22,
#         }
#
#     }
#
# }]
# print(person[0]['friend']['age'] + person[0]['friend']['age'] + person[0]['friend']['age'])


# l = 0
# for x,y in person[0].items():
#     if x == 'age':
#         l += y
#
#         if x == 'friend':
#             for a, b in y.items():
#                 print(a, b)
#                 if a == 'age':
#                     l += b
#
#                 if a == 'friend':
#                     for key, value, in b.items():
#                         if key == 'age':
#                             l += value
#
# print(l)
#



#
# l = sorted([5,2,4,1,3]), reverse=True)

#
# data = list(enumerate(["Ali", "Doni", "Vohid"]))
# print(data)
#
#
# l = ["Ali", "Vali", "Vohid", ""]







# alf = ["c", "b", "a", "f", "g", "d", "e"]
# lst = [0,1,2,3,4]
# x = sorted(alf)
# m = dict(zip(lst, x))
# print(m)

# dict3 = {
#     1 : "a"
#     # ....
# }


#lst = int(input("Son: "))
# l = 0
# for x in range(1, lst + 1):
#     l += x
# print(l)

# l3 = 0
# res = 0
# while l3 == lst:
#     res -= l3
#     print(l3)
#     l3 += 1

string = "Shohjahon"
for x in range(len(string)):
    print(string[x])

x = 0
while x < len(string):
    x += 1
    print(x)


t = (1,2,3,4,5,6)
# for x in t:
#     print(t)



for x in range(0, len(t)):
    print(t[x])


