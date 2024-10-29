# Konstanta
jam_per_minggu = 40  # Asumsi jam kerja per minggu
minggu = 5  # Lama waktu bekerja dalam minggu
gaji_per_jam = 14  # Gaji per jam dalam satuan mata uang

# Perhitungan
# 1. Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak
pendapatan_total = jam_per_minggu * minggu * gaji_per_jam

# 2. Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak
pajak = 0.14  # 14% pajak
pendapatan_setelah_pajak = pendapatan_total * (1 - pajak)

# 3. Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris
persentase_pakaian = 0.10  # 10% untuk pakaian dan aksesoris
biaya_pakaian = pendapatan_setelah_pajak * persentase_pakaian

# 4. Jumlah uang yang akan Budi habiskan untuk membeli alat tulis
persentase_alat_tulis = 0.01  # 1% untuk alat tulis
biaya_alat_tulis = pendapatan_setelah_pajak * persentase_alat_tulis

# 5. Jumlah uang yang akan Budi sedekahkan
pendapatan_sisa = pendapatan_setelah_pajak - biaya_pakaian - biaya_alat_tulis
persentase_sedekah = 0.25  # 25% untuk sedekah
jumlah_sedekah = pendapatan_sisa * persentase_sedekah

# 6 & 7. Jumlah uang yang akan diterima anak yatim dan kaum dhuafa
jumlah_per_seribu = jumlah_sedekah // 1000  # Jumlah bagian Rp.1000
bagian_anak_yatim = jumlah_per_seribu * 1000 * 0.30  # 30% untuk anak yatim
bagian_kaum_dhuafa = jumlah_per_seribu * 1000 * 0.70  # 70% untuk kaum dhuafa

# Hasil
print("1. Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak:", pendapatan_total)
print("2. Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak:", pendapatan_setelah_pajak)
print("3. Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris:", biaya_pakaian)
print("4. Jumlah uang yang akan Budi habiskan untuk membeli alat tulis:", biaya_alat_tulis)
print("5. Jumlah uang yang akan Budi sedekahkan:", jumlah_sedekah)
print("6. Jumlah uang yang akan diterima anak yatim:", bagian_anak_yatim)
print("7. Jumlah uang yang akan diterima kaum dhuafa:", bagian_kaum_dhuafa)
