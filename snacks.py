names = ["geert", "guus", "gerda"]
snacks = []

for fullname in names:
    snack = input("Whats your favorite snack?")
    snacks.append(snack)
    name_length = str(len(fullname))
   # print(fullname, name_length)


index = 0
for fullname in names:
    snack = snacks[index]
    index = index +1
    print(fullname + "likes" + snack)
    print(index)
