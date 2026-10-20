
# SecureTask — DevSecOps Project

## 1. Nama dan Fungsi Aplikasi

SecureTask adalah aplikasi pengelolaan tugas sederhana berbasis Python.
Aplikasi menyediakan fitur untuk menambahkan tugas, melihat daftar tugas,
dan menandai tugas sebagai selesai. Aplikasi juga memvalidasi input agar
judul tugas tidak kosong dan tidak melebihi 100 karakter.

## 2. Bahasa dan Teknologi

- Bahasa pemrograman: Python 3
- Unit testing: unittest
- CI/CD: GitHub Actions
- SAST: Bandit
- Runner: ubuntu-latest

## 3. Struktur Proyek

- `src/app.py`: antarmuka menu aplikasi.
- `src/task_manager.py`: logika pengelolaan tugas.
- `src/validators.py`: validasi judul tugas.
- `src/storage.py`: fungsi membaca dan menyimpan data JSON.
- `src/security.py`: pemeriksaan input.
- `tests/test_task_manager.py`: pengujian otomatis.

## 4. Cara Menjalankan Aplikasi

Pastikan Python 3 sudah terpasang. Dari direktori utama proyek, jalankan:

```bash
python -m src.app
```

Untuk menjalankan unit test:

```bash
python -m unittest discover -s tests -v
```

Untuk memasang dan menjalankan Bandit secara lokal:

```bash
python -m pip install -r requirements.txt
bandit -r src/ -ll
```

## 5. Overview Pipeline CI/CD

Pipeline didefinisikan pada `.github/workflows/devsecops.yml`.
Workflow berjalan saat ada push ke branch `main` atau pull request
yang menargetkan branch `main`.

Pipeline memiliki dua job:

1. `build`: menyiapkan Python dan menjalankan unit test.
2. `sast-scan`: bergantung pada job `build`, lalu menjalankan Bandit
   untuk memindai potensi kerentanan keamanan pada source code.

Quality Gate digunakan untuk menentukan apakah temuan keamanan yang
memenuhi kriteria yang ditetapkan menyebabkan pipeline gagal.
Hasil eksekusi dapat diperiksa melalui tab Actions di GitHub.
