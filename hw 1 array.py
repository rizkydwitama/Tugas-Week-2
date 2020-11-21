arrBerat = []

def hitungMinMax(arrBerat):
    global bMin, bMax
    # Definisikan Proses Mencari Berat Maximum Dan Minimum
    bMin = min(arrBerat)
    bMax = max(arrBerat)


def rerata(arrBerat):
    total = 0

    # Definisikan Proses Mencari Rerata Dari Total Berat
    for a in arrBerat:
        total += a

    rerata = total / n

    # Return Hasil Rerata
    return rerata
print('Masukkan Banyak Data Berat Balita :', end=" ")
n = int(input())

for i in range(n):
    print(f'Masukkan Berat Balita Ke-{i+1} :', end=' ')
    # Inisialisasi Input Data Berat
    Berat = float(input())

    # Masukkan Data Berat Ke Array (arrBerat)
    arrBerat.append(Berat)
    


# Panggil procedur hitungMinMax(arrBerat)
hitungMinMax(arrBerat)

# Print Data Minimum, Maximum, dan Rerata Berat
print("Berat balita minimum: {:.2f} kg".format(bMin))
print("Berat balita maximum: {:.2f} kg".format(bMax))
print("Rerata berat balita: {:.2f} kg".format(rerata(arrBerat)))


