def bubble_sort(daftar_nilai):
    n = len(daftar_nilai)
    for i in range(n):
        # Flag untuk menunjukkan apakah ada pertukaran dalam iterasi saat ini
        swapped = False
        for j in range(0, n-i-1):
            if daftar_nilai[j] > daftar_nilai[j+1]:
                # Lakukan pertukaran
                daftar_nilai[j], daftar_nilai[j+1] = daftar_nilai[j+1], daftar_nilai[j]
                swapped = True
        # Jika tidak ada pertukaran dalam iterasi saat ini, daftar nilai sudah terurut
        if not swapped:
            break
    return daftar_nilai

# Daftar nilai awal
daftar_nilai = [78, 65, 90, 82, 70]

# Panggil fungsi bubble_sort untuk mengurutkan daftar nilai
daftar_nilai_terurut = bubble_sort(daftar_nilai)

# Tampilkan daftar nilai terurut
print("Daftar nilai terurut:", daftar_nilai_terurut)
