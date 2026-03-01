# typo
# print("hello world"

# undefined
# print(name)

# print(int("string"))

# list_data = [1, 2, 3]
# print(list_data[8])

# siswa = {"nama": 19}
# print(siswa["age"])

# print(10 /  0)

print("KALKULATOR SEDERHANA")

try:
  angka1 = int(input("Masukan angka: "))
  angka2 = int(input("Masukan angka: "))
  hasil_bagi = angka1 / angka2
  print(f"hasil: {hasil_bagi}")

except:
  print("Error")

print("PROGRAM SLSAI")

print()
print("KALKULATOR SEDERHANA V.2")

try:
  angka1 = int(input("Masukan angka: "))
  angka2 = int(input("Masukan angka: "))
  hasil_bagi = angka1 / angka2
  print(f"hasil: {hasil_bagi}")
except ValueError:
  print("Masukan angka yang valid!")
except ZeroDivisionError:
  print("Tidak boleh membagikan dengan 0")
except:
  print("Terjadi kesalahan lain")

print("PROGRAM SELSAI")

print()
try:
  angka = int(input("Masukan angka: "))
except ValueError:
  print("Masukan angka yang benar!")
else:
  print(f"Angka yang anda masukan: {angka}")
  if(angka > 0):
    print("Angka Positif")
  elif(angka < 0):
    print("Angka Negatif")
  else:
    print("Angka nol")
finally:
  print("PROGRAM SELESAI.")

print()
try:
  angka = int(input("Masukan angka: "))
except ValueError:
  print("Masukan angka yang valid!")
finally:
  print("Program Selesai.")