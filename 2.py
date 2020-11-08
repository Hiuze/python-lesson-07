a = int(input("a: "))
b = int(input("b: "))
ma = max(a,b)
mi = min(a,b)
i = 0
while mi <= ma:
    if mi % 2 == 0:
        print(mi)
        i += mi
    mi += 1
print("niilber", i)
