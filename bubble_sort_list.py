def bubble_sort_descending(daftar_angka):
    n = len(daftar_angka)
    for i in range(n):
        # Flag untuk menunjukkan apakah ada pertukaran dalam iterasi saat ini
        swapped = False
        for j in range(0, n-i-1):
            if daftar_angka[j] < daftar_angka[j+1]:
                # Lakukan pertukaran
                daftar_angka[j], daftar_angka[j+1] = daftar_angka[j+1], daftar_angka[j]
                swapped = True
        # Jika tidak ada pertukaran dalam iterasi saat ini, daftar angka sudah terurut
        if not swapped:
            break
    return daftar_angka

# Daftar angka awal
daftar_angka = [42, 19, 33, 8, 55]

# Panggil fungsi bubble_sort_descending untuk mengurutkan daftar angka
daftar_angka_terurut = bubble_sort_descending(daftar_angka)

# Tampilkan daftar angka terurut
print("Daftar angka terurut:", daftar_angka_terurut)
