# Random Group Maker Generator

Repositori ini berisi implementasi **aplikasi pembuat grup acak** yang dibuat sebagai proyek akhir mata kuliah *Matematika Diskrit*. Aplikasi ini membantu membagi sekumpulan nama (misalnya daftar mahasiswa dalam satu kelas) ke dalam beberapa kelompok secara acak.

## Fitur

- Input daftar nama (secara manual / dari file, sesuai implementasi)
- Pengacakan urutan nama
- Pembagian menjadi beberapa kelompok berdasarkan:
  - jumlah anggota per kelompok, **atau**
  - jumlah kelompok yang diinginkan
- Menjamin setiap nama hanya masuk ke satu kelompok
- Menampilkan hasil pembagian kelompok dengan format yang mudah dibaca

## Cara Kerja Singkat

Secara umum, program melakukan langkah-langkah berikut:

1. Menerima input daftar nama.
2. Mengacak urutan nama menggunakan fungsi pseudo-random.
3. Membagi daftar yang sudah diacak menjadi beberapa kelompok sesuai parameter yang dipilih (jumlah anggota / jumlah kelompok).
4. Menampilkan hasil kelompok beserta anggotanya.

Logika ini terkait dengan konsep-konsep dalam **Matematika Diskrit**, seperti himpunan, permutasi, dan kombinatorika sederhana.
