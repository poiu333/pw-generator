import secrets
import string
import random
def buat_password(panjang):
    karakter = string.ascii_letters + string.digits + string.punctuation
    sandi = ''.join(secrets.choice(karakter) for _ in range(panjang))
    return sandi
nama=["Andi","Budi","Cahyo","Dedi","Eko","Fajar","Hadi","Indra","Joko","Krisna","Lukman","Mahendra","Nanda","Oki","Putra","Rafi","Satria","Taufik","Umar","Vino","Wahyu","Yoga","Zaki","Agus","Bayu","Candra","Darma","Edy","Fikri","Gunawan","Hendra","Ilham","Jefri","Kamal","Leo","Maulana","Naufal","Omar","Prasetyo","Rizky","Syahrul","Teguh","Udin","Valen","Wira","Yusuf","Zain","Adit","Bima","Cakra","Dion","Erwin","Fauzan","Gery","Haris","Irfan","Jason","Kiki","Luthfi","Miko","Nico","Oscar","Pras","Rama","Sandy","Tomi","Ucok","Vega","Wawan","Yanuar","Zidan","Arga","Bagas","Cipto","Daffa","Elang","Fadli","Gilang","Hafiz","Ikbal","Jovan","Kenzie","Lingga","Mirza","Nabil","Ozan","Pandu","Raka","Syafiq","Tariq","Ubaid","Vicky","Willy","Yasir","Zuhri"]
while True:
    input1 = int(input("pilih panjang password 8/12: "))
    if input1 not in [8, 12]:
     print("Panjang password harus 8 atau 12.")
     continue  
    
    nama_random = random.choice(nama)
    password = buat_password(input1)
    print(f"Nama: {nama_random}")
    print(f"Password: {password}")
    break