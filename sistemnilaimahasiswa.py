#Program Menghitung Nilai Rata-Rata Mahasiswa dalam Satu Semester

def hitung_rata_rata_nilai_mahasiswa(nilai: list[float]) -> float:
   return sum(nilai) / 3


def validasi_dan_input_nilai(jenis_nilai: str) -> float:
   while True:
      try:
         nilai: float = float(input(F"Masukan nilai {jenis_nilai} dengan rentang 1 - 100 : "))
   
         if (nilai < 0 or nilai > 100):
            print("Mohon memasukan nilai dengan rentang yang telah disesuaikan!.\nSilahkan coba lagi!")
         else:
            print("Nilai berhasil dimasukan!")
            return nilai
            
      except ValueError:
         print("Terjadi error, nilai yang dimasukan bukan sebuah angka!.\nSilahkan coba lagi!")


def main() -> None:
   #variabel
   nama: str = input("Masukan nama mahasiswa : ").title()
   nim: str = input("Masukan NIM mahasiswa : ")
   
   #Proses input nilai
   nilai_nilai: list[float] = []

   for jenis_nilai in ("Harian", "UTS", "UAS"):
      nilai: float = validasi_dan_input_nilai(jenis_nilai)
      nilai_nilai.append(nilai)
         
   #Proses menghitung nilai rata_rata mahasiswa dari nilai harian, UTS, dan UAS
   rata_rata = hitung_rata_rata_nilai_mahasiswa(nilai_nilai) 
   print(F"Rata-rata nilai mahasiswa bernama \"{nama}\" dengan NIM \"{nim}\" adalah {rata_rata}")
   
   if rata_rata >= 80 :
       kategori_nilai = "A"
   elif rata_rata >= 75 :
       kategori_nilai = "-A"
   elif rata_rata >= 65 :
       kategori_nilai = "B"
   elif rata_rata >= 60 :
       kategori_nilai = "C"
   else:
       kategori_nilai = "Tidak lulus!"
   
   print(F"Kategori nilai anda: {kategori_nilai}")

if __name__ == "__main__":
   main()
