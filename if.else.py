# Indentation : lùi đầu dòng
age = input()

if int(age) < 10:
    print("Tre  nho")
else:
    print("khong phai tre nho")
a = 20
b = 18

if a < b:
    min = a
elif a == b:
    min = a
    min = b
else:
    min = b
print(min)

# if else reduction
reduce = 2
meo = 6

max = meo if reduce < meo else reduce
print(max)