print()
print("=== SIMPAN DATA NILAI ===")

file = open("src/data/nilai_siswa.txt", "w")

while True:
  nama = str(input("Masukan nama siswa (enter untuk selesai): "))

  if nama == "":
    break

  nilai = int(input("Masukan nilai siswa: "))
  
  data = file.write(f"{nama}, {nilai}, \n")
  print(f"Data {nama} berhasil disimpan")

file.close()
print("=== PROGRAM SELESAI ===")

print()
print("=== MEMBACA ISI FILE ===")

file = open("src/data/nilai_siswa.txt", "r")

for line in file:
  data = line.strip().split(',')
  print(f"{data[0]}:{data[1]}")

file.close()

print("=== SELESAI ===")

print()
print("=== MEMBACA ISI FILE DENGAN KEYWORD 'WITH' ===")

with open("src/data/nilai_siswa.txt", "r") as file:
  for line in file:
    data = line.strip().split(",")
    print(f"{data[0]}:{data[1]}")

print("=== SELESAI ===")

print()
print("=== MEMBACA ISI FILE DENGAN 'TRY EXCEPT' ===")

try:
  with open("src/data/nilai_siswa.txt", "r") as file:
    for line in file:
      data = line.strip().split(",")
      print(f"{data[0]}:{data[1]}")
except FileNotFoundError:
  print("file error / tidak ditemukan")
finally:
  print("=== SELESAI ===")
