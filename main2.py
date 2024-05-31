person = [{
    'name': 'Ali',
    'age': 25,
    'friend': {
        'name': 'Ali',
        'age': 24,
        'friend': {
            'name': 'Shoxruh',
            'age': 22,
        }

    }

}]
print(person[0]['friend']['age'] + person[0]['friend']['age'] + person[0]['friend']['age'])


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
