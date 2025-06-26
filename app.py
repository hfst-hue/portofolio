from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'nama': 'Mhd Hafist Akmal',
        'profesi': 'Web Developer',
        'tentang': (
            "Saya pribadi cepat belajar dan mampu beradaptasi dengan lingkungan baru. "
            "Berpengalaman dalam Food Server, desain web, pemrograman Python, serta memiliki keterampilan Office & komputer umum."
        ),
        'keahlian': [
            "Dapat bekerja di bawah tekanan",
            "Cleanliness & Tanggung Jawab",
            "Multitasking & Teamwork",
            "Pembuatan Website",
            "Python Programming",
            "Microsoft Office & Komputer Umum",
            "Pemeliharaan Mesin Produksi",
            "Mekanik Sepeda Motor",
            "Pengelasan & Pengoperasian Komputer"
        ],
        'pengalaman': [
            {
                'posisi': 'Helper Produksi',
                'perusahaan': 'PT. Gunung Gahapi Sakti, Medan',
                'tahun': 'Mei 2023 –  2023',
                'deskripsi': [
                    "Pemeriksaan dan perawatan mesin.",
                    "Berinovasi dalam proses produksi.",
                    "Mencapai target efisiensi kerja."
                ]
            },
            {
                'posisi': 'Cleaning Service',
                'perusahaan': 'PT. Arah, Selangor Malaysia',
                'tahun': 'Jan 2024 – Jul 2024',
                'deskripsi': [
                    "Menjaga kebersihan profesional.",
                    "Kerja tim tepat waktu.",
                    "Merawat alat kebersihan."
                ]
            },
            {
                'posisi': 'Food Server',
                'perusahaan': 'Sambal Gesek, Selangor Malaysia',
                'tahun': 'Ags 2024 – Sep 2024',
                'deskripsi': [
                    "Menjelaskan menu dan bahan.",
                    "Adaptif terhadap perubahan.",
                    "Layanan pelanggan yang efisien."
                ]
            }
        ],
        'portofolio': [
            {
                'judul': 'Sistem Absensi Karyawan',
                'gambar': 'project1.jpg',
                'link': 'https://github.com/hfst-hue/aplikasi-absensi-kerja'
            },
            {
                'judul': 'Landing Page Jasa Joki Game',
                'gambar': 'project2.jpg',
                'link': 'https://github.com/hfst-hue/mlbbsite'
            }
        ]
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
