a = input("Вводится дата в формате dd.mm.yyyy: ")
a1 = a.replace(".", "\\") 
print(f"mm\dd\yyyy: {a1[3:6] + a1[0:3] + a1[6:]}")








