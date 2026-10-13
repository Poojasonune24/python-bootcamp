items = {"Rice":10, "Soap": 20, "Shampu": 30, "Dal": 10}
print(items)

items["Rice"] = items["Rice"]-2
print(items)

if "Masala" in items:
    items["Masala"] += 1
else:
    items["Masala"] = 10

print(items)

