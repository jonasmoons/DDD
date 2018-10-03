names =[
        ["geert"],
        ["guus"],
        ["gerda"]
        ]
snacks = []




for name in names:
    fullname = name[0]
    name_length = len(fullname)
    print(name[0] + " is " + str(name_length) + " characters long")

for name in names:
    snack = input("Whats your favorite snack?")
    name.append(snack)
    print(name[0]+ " likes " + name[1])





