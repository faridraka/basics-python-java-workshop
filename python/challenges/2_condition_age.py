# Program Klasifikasi Usia

# 1. TODO: Baca input dari pengguna
age = int(input("Masukkan umur kamu: "))
# 2. TODO Tentukan kategori berdasarkan usia

if age >= 60:
  print("Lansia")
elif age >= 18:
  print("Dewasa")
elif age >= 12:
  print("Remaja")
else:
  print("Anak-anak")