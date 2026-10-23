
def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    lulus = []
    for x in data:
        if x >= batas:
            lulus.append(x)
    return lulus


# Data nilai mahasiswa
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Mengolah data
banyak_data = len(nilai)
total = sum(nilai)
rata = rata_rata(nilai)
lulus = nilai_lulus(nilai)
jumlah_lulus = len(lulus)
belum_lulus = banyak_data - jumlah_lulus

# Menampilkan hasil
print("=== ANALISIS NILAI MAHASISWA ===")
print(f"Seluruh nilai    : {nilai}")
print(f"Banyak data      : {banyak_data}")
print(f"Total nilai      : {total}")
print(f"Rata-rata        : {rata:.2f}")
print(f"Nilai minimum    : {min(nilai) if nilai else 'Tidak ada data'}")
print(f"Nilai maksimum   : {max(nilai) if nilai else 'Tidak ada data'}")
print(f"Batas kelulusan  : 60")
print(f"Jumlah lulus     : {jumlah_lulus}")
print(f"Jumlah belum lulus: {belum_lulus}")
print(f"Daftar nilai lulus: {lulus}")
