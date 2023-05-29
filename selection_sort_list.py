def selection_sort(daftar_angka):
    n = len(daftar_angka)
    for i in range(n-1):
        # Cari nilai terkecil di antara angka yang belum terurut
        min_index = i
        for j in range(i+1, n):
            if daftar_angka[j] < daftar_angka[min_index]:
                min_index = j

        # Tukar angka pada posisi iterasi saat ini dengan angka terkecil
        daftar_angka[i], daftar_angka[min_index] = daftar_angka[min_index], daftar_angka[i]

    return daftar_angka

# Daftar angka awal
daftar_angka = [9, 5, 3, 8, 2]

# Panggil fungsi selection_sort untuk mengurutkan daftar angka
daftar_angka_terurut = selection_sort(daftar_angka)

# Tampilkan daftar angka terurut
print("Daftar angka terurut:", daftar_angka_terurut)
