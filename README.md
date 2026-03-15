# 🔐 Password Generator

Program Python sederhana untuk membuat password acak yang kuat, dilengkapi dengan pemilihan nama acak dari daftar nama Indonesia.

---

## 📋 Deskripsi

Program ini akan:
- Meminta pengguna memilih panjang password (8 atau 12 karakter)
- Menghasilkan password acak yang aman menggunakan modul `secrets`
- Menampilkan nama acak dari daftar nama Indonesia bersama password yang dihasilkan

---

## ⚙️ Persyaratan

- Python 3.x

Tidak memerlukan instalasi library tambahan. Semua modul yang digunakan sudah tersedia secara bawaan di Python:

| Modul | Fungsi |
|-------|--------|
| `secrets` | Menghasilkan password yang kriptografis aman |
| `string` | Menyediakan karakter huruf, angka, dan simbol |
| `random` | Memilih nama secara acak dari daftar |

---

## 🚀 Cara Menjalankan

```bash
python pw_generator.py
```

---

## 📖 Cara Penggunaan

1. Jalankan program
2. Masukkan angka `8` atau `12` untuk menentukan panjang password
3. Jika input selain 8 atau 12, program akan meminta input ulang
4. Program menampilkan nama acak dan password yang dihasilkan

**Contoh output:**
```
Pilih panjang password 8/12: 12
Nama: Rizky
Password: aB3$kL9@mZ#q
```

---

## 📁 Struktur Kode

```
pw_generator.py
├── buat_password(panjang)   → Fungsi untuk membuat password acak
├── nama[]                   → Daftar 95 nama Indonesia
└── while True loop          → Input validasi dan output hasil
```

---

## 🔒 Keamanan

Password dihasilkan menggunakan modul `secrets` yang direkomendasikan Python untuk keperluan kriptografi, sehingga lebih aman dibandingkan `random` biasa untuk penggunaan password sungguhan.

---

## 👤 Author

Dibuat sebagai latihan Python — password generator sederhana dengan validasi input.
