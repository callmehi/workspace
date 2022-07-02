import clipboard as pc
a1 = "Hey, nice to see you"
pc.copy(a1)
a2 = pc.paste()
print(a2)
print(type(a2))