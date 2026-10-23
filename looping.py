# print("sohan")
# name = ["sohan","alamin","rabby"]
# mt = []

# for num in name:
#     if "s" in num:
#         mt.append(num)
# print(mt)

# print(5/8)

# number = [50,60,7,8,5,39,5,58]
# total = 0

# for num in number:
#     total += num
# print(total)


# age = 15

# if age > 17:
#     print(("you ar eligiable"))
# else:
#     print("not elegiable")

# thistuple = ("sohan","saidi","big boss","arafat")
# x = list(thistuple)
# x[1] = "kiwi"
# y = tuple(x)
# print(y)


"""tupol ke list banah change kore nete lagbe pore abar tuple korte lagbe"""


# number = (50,98,5,78,5,8,6,6,8)
# tup = list(number)
# tup.sort()
# print(tuple(tup))


# fruits = ("apple","banana","cherry")

# (green,read,back) = fruits

# print(read,green)


food = ["pizza", "hamburger","hotdog","spagetti","biriyani"]
fav = str(input("Enter your favrite food 1 item: "))
for num in food:
    if fav.strip().lower() == num:
        print(F"i love {num}")
    else:
        print(F"i dont like  {num}")