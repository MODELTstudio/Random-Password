import random
sym = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

lenth = int(input("Длина пароля \n"))
pasw = ""

for i in range(lenth):
    pasw += random.choice(sym)

print(f"Ваш пароль {pasw}")

name = ['Player', 'Top1', 'New', 'Best']
name2 = ['Hoster?', 'Bester', 'IOS', 'Android']
namenw = ''
lenth2 = int(input("Количетсво слов? \n"))
for i in range(lenth2):
    ifer = random.randint(1,2)
    if ifer == 1:
        namenw += random.choice(name)
    elif ifer == 2:
        namenw += random.choice(name2)

print(f"Ваш ник {namenw}")