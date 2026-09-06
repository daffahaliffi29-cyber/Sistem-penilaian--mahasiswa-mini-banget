#Sistem Penilaian Mahasiswa

#variabel
nama = input("Masukan nama mahasiswa : ")
nim = int(input("Masukan NIM mahasiswa : "))

#nilai
nilai_UTS = float(input("Masukan nilai UTS : "))
nilai_UAS = float(input("Masukan nilai UAS : "))
nilai_harian = float(input("masukan nilai harian : "))

if (nilai_UTS < 0 or nilai_UTS >100 ) or \
   (nilai_UAS < 0 or nilai_UAS >100 ) or \
   (nilai_harian < 0 or nilai_harian >100):
    print("nilai harus dalam rentang 0 - 100")
    exit()

#Gatau nama bagian ini
rata_rata = (nilai_UTS + nilai_UAS + nilai_harian) / 3
print (rata_rata) 
if rata_rata >= 80 :
    grade = "A"
elif rata_rata >= 75 :
    grade = "-A"
elif rata_rata >= 65 :
    grade = "B"
elif rata_rata >= 60 :
    grade = "C"
else:
    grade = "Kamu tidak lulus"

print (grade)

