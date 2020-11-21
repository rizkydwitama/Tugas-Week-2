klub_a = input("Klub A : ")
klub_b = input("Klub B : ")
menang = []
n = 1

while True:
    a, b = map(int, input(f"Pertandingan {n} : ").split())
    if a >= 0 and b >= 0:
        n += 1
        if a > b:
            menang.append(klub_a)
        elif a == b:
            menang.append("Draw")
        else:
            menang.append(klub_b)
    else:
        break
y = 1
for x in menang:
    print(f"Hasil {y}: {x}",)
    y += 1
print("Pertandingan selesai")