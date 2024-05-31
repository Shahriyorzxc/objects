# #Task1
# def family(name):
#     Family = {
#         "Darth Vader": "father",
#         "Leia": "sister",
#         "Han": "brother in law",
#         "R2D2": "droid"
#     }
#
#     if name in Family:
#         return f"Luke, I am your {Family[name]}. "
#     else:
#         return "Error"
#
#
# print(family("Darth Vader"))  # ---> "Luke, I am your father."
# print(family("Leia"))  # ---> "Luke, I am your sister."
# print(family("Han"))  # ---> "Luke, I am your brother, in law."
#
#
# #Task2
# def get_budgets(l):
#     tot = 0
#     for x in l:
#         tot += x['budget']
#     return tot
#
#
# print(get_budgets([
#   { "name": "John", "age": 21, "budget": 23000 },
#   { "name": "Steve",  "age": 32, "budget": 40000 },
#   { "name": "Martin",  "age": 16, "budget": 2700 }
# ]))  # ➞ 65700
#
# print(get_budgets([
#   { "name": "John",  "age": 21, "budget": 29000 },
#   { "name": "Steve",  "age": 32, "budget": 32000 },
#   { "name": "Martin",  "age": 16, "budget": 1600 }
# ]))  # ➞ 62600
#
#
#
# #Task3
# def get_students_names(st):
#     lst = []
#     for x in st:
#         lst.append(x)
#     return sorted(st.values())
#
# print(get_students_names({
#   "Student 1": "Steve",
#   "Student 2": "Becky",
#   "Student 3": "John"
# }))  # ➞ ["Becky", "John", "Steve"]
#
# #Task4
# def maximum_score(l):
#     lst = []
#     for x in l:
#         lst.append(x['score'])
#     return sum(lst)
#
#
#
# print(maximum_score([
# { "tile": "N", "score": 1 },
# { "tile": "K", "score": 5 }, { "tile": "Z", "score": 10 },
# { "tile": "X", "score": 8 }, { "tile": "D", "score": 2 },
# { "tile": "A", "score": 1 }, { "tile": "E", "score": 1 } ]))  #28
#
# print(maximum_score([{ "tile": "B", "score": 2 },{ "tile": "V", "score": 4 },
# {"tile": "F", "score": 4 }, { "tile": "U", "score": 1 },
# {"tile": "D", "score": 2 }, { "tile": "O", "score": 1 },
# { "tile": "U", "score": 1 } ]))  #15
#
#
#
# #Task5
# def mapping(s):
#     l = {}
#     for x in s:
#         if type(x) is set:
#             pass
#
#         else:
#             l[x] = x.upper()
#     return l
#
#
# print(mapping(["p", "s"]))  # ➞ {"p": "P", "s": "S"}
# print(mapping(["a", "b", "c"]))  # ➞ {"a": "A", "b": "B", "c": "C"}
# print(mapping(["a", "v", "y", "z"]))   # ➞ {"a": "A", "v": "V", "y": "Y", "z": "Z")





# #Task6
# def calc_diff(set1, set2):
#     s = 0
#     for x in set1:
#         if x in set2:
#             s += min(set1[x] - set2[x], set2[x] + set1[x])
#         else:
#             s += set1[x]
#     return s
#
#
# print(calc_diff({ "baseball bat": 20 }, { "baseball bat": 5 })) # ➞ 15
# print(calc_diff({"skate": 10, "painting": 20 }, {"skate": 19})) # ➞ 11
# print(calc_diff({"skate": 200, "painting": 200, "shoes": 1 }, {"skate": 400})) # ➞ 1
#

# Task7
def profit(l):
    result = 0
    for x,y in l.items():
        if type(y) == int or float:
            result += y
    return result


print(profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}))
print(profit({
  "cost_price": 225.89,
  "sell_price": 550.00,
  "inventory": 100
}))
print(profit({
  "cost_price": 2.77,
  "sell_price": 7.95,
  "inventory": 8500
}))


# #Task8
# p1 = {
#     "name": "Samuel",
#     "age": 24

# }

# p2 = {
#     "name": "Joel",
#     "age": 36
#
# }
#
# p3 = {
#     "name": "Lily",
#     "age": 24
#
# }
#
# while True:
#     name = input("Name: ")
#     if name == "Samuel":
#         print("Joel is older than me. ")   # Joel is older than me.
#
#     elif name == "Joel":
#         print("Samuel is younger than me.")  # Samuel is younger than me.
#
#     elif name == "Lily":
#         print("Lily is the same age as me.")  # Lily is the same age as me.
#
#     else:
#         print("Youre cooked")
#

#Task9
def dict_to_list(l):
    return sorted(l.items())


print(dict_to_list({
  "D": 1,
  "B": 2,
  "C": 3
}))  # ➞ [("B", 2), ("C", 3), ("D", 1)]

print(dict_to_list({
  "likes": 2,
  "dislikes": 3,
  "followers": 10
}))  # ➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]

#Task10
def to_dict(l):
    d = {}
    for x in l:
        d[x] = (x)
    return d


print(to_dict(["a", "b", "c"])) # ➞ [{"a": 97}, {"b": 98}, {"c": 99}]
print(to_dict(["^"])) # ➞ [{"^": 94}]
print(to_dict({})) # ➞ {}


#Task11
def total_amount_adjectives(d):
    return len(d)


print(total_amount_adjectives({ "a": "moron" })) # ➞ 1
print(total_amount_adjectives({ "a": "idiot", "b": "idiot", "c": "idiot" })) # ➞ 3
print(total_amount_adjectives({ "a": "moron", "b": "scumbag", "c": "moron", "d": "dirtbag" })) # ➞ 4


#Task12
def is_equal(obj_one, obj_two):
    if obj_one == obj_two:
        return True
    else:
        return False


obj_one = {
  "name": "Benny",
  "phone": "3325558745",
  "email": "benny@edabit.com"
}

obj_two = {
  "name": "Jason",
  "phone": "9853759720",
  "email": "jason@edabit.com"
}

print(is_equal(obj_one, obj_two))  # ➞ False

obj_one = {
  "name": "Jason",
  "phone": "9853759720",
  "email": "jason@edabit.com"
}

obj_two = {
  "name": "Jason",
  "phone": "9853759720",
  "email": "jason@edabit.com"
}

print(is_equal(obj_one, obj_two))  # ➞ True


#Task13
lst = [1, 2, 3, 4, 5, 6, 7, 8]
first = lst[0]
second = lst[1]
third = lst[2]
other = lst[3:]

print(first) # ➞ outputs 1
print(second) # ➞ outputs 2
print(third) # ➞ outputs 3
print(other) # ➞ outputs [4, 5, 6, 7, 8]


#Task14
def element_from_set(s):
    if s:
        return s.pop()
    else:
        return None


print(element_from_set(({"edabit"}))) # ➞ "edabit"
print(element_from_set(({True}))) # ➞ True
print(element_from_set(({11037}))) # ➞ 11037


#Task15
def has_key(l,l1):
    return l1 in l


print(has_key({ "a": 44, "b": 45, "c": 46 }, "d")) # ➞ False
print(has_key({ "craves": True, "midnight": True, "snack": True }, "morning")) # ➞ False
print(has_key({ "pot": 1, "tot": 2, "not": 3 }, "not")) # ➞ True