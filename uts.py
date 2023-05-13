import os

print("_____________________________________________")
print("|\tSELAMAT DATANG DI APLIKASI SISTEM PAKAR \t|")
print("|\t\t DETEKSI MALARIA DAN DEMAM BERDARAH \t\t|")
print("_____________________________________________")

nama = input("NAMA\t")
pilihan = input(f"Hallo {nama},\nApakah anda ingin memulai diagnosa? (y/n)")

os.system("cls" if os.name == "nt" else "clear")

while pilihan == "y":
    print("\nApakah anda merasakan gejala berikut ini?")
    print("1. Demam/ Suhu badan tinggi?")
    print("2. Sakit kepala?")
    print("3. Nyeri pada sendi, otot, dan tulang?")
    print("4. Merasa mual dan muntah ?")
    diag1 = input("Jawab (y/n): ")

    if diag1 == "y":
        print("\nApakah anda merasakan gejala berikut ini?")
        print("1. Hilang nafsu makan")
        print("2. Nyeri pada bagian mata")
        print("3. Ruam kemerahan")
        diag2 = input("Jawab (y/n): ")

        if diag2 == "y":
            print(f"\nHai {nama}, hasil awal diagnosa kamu adalah :")
            print("\nGejala demam berdarah, segera ke dokter!")
            
        elif diag2 == "n":
            print("1. Menggigil sedang sampai berat")
            print("2. Tubuh kelelahan")
            print("3. Banyak berkeringat")
            print("4. Diare")
            diag3 = input("Jawab (y/n): ")

            if diag3 == "y":
                print(f"\nHai {nama}, hasil awal diagnosa kamu adalah :")
                print("\nGejala malaria, segera ke dokter!")
            elif diag3 == "n":
                print(f"\nHai {nama}, sepertinya kamu kurang istirahat")
            else:
                print(f"\nHai {nama}, sepertinya kamu tidak mau berobat")
        elif diag1 == "n":
            print(f"\nHai {nama}, anda sepertinya butuh istirahat")     
    else:
        print(f"Hai {nama}, sepertinya kamu tidak ingin berobat")

    print("________________________________________________")
    pilihan = input(f"Hallo {nama},\nApakah anda ingin memulai tes lagi? (y/n)")

    if pilihan == "y":
        os.system("cls" if os.name == "nt" else "clear")
        print("_____________________________________________")
        print("|\tSELAMAT DATANG DI APLIKASI SISTEM PAKAR\t|")
        print("|\t\t DETEKSI MALARIA DAN DEMAM BERDARAH\t\t|")
        print("_____________________________________________")
    
    else:
        print("_________________TERIMA KASIH________________") 
