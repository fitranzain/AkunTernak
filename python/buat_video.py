from moviepy.editor import *
import textwrap

# === 1. Baca naskah ===
naskah = """
Halo, perkenalkan nama saya Fitran Zain.  
Saya seorang akuntan yang sehari-hari bergelut dengan angka, laporan, dan pencatatan keuangan. Namun di sisi lain, saya juga sedang belajar dan membangun usaha peternakan ayam skala rumahan. Tujuannya nanti peternakan ini dapat dilakukan dengan konsep **integrated farming** – yaitu menggabungkan ternak, pertanian, dan sumber daya sekitar agar saling mendukung dan lebih efisien.

Saya percaya, ilmu akuntansi tidak hanya berguna di kantor atau perusahaan besar, tapi juga bisa diterapkan dalam usaha kecil seperti **peternakan** dalam berbagai skala, mulai dari skala rumahan sampai dengan skala profesional.

Saat ini, saya sudah memulai beberapa langkah kecil diantaranya :

1. Kandang semi dengan ukuran 2 x 8 meter dibagi menjadi 4 petak masing-masing 2 x 2 meter;
2. Saya memelihara beberapa jenis ayam, diantaranya; 2 ekor betina ayam kampung asli, 4 ekor betina ayam elba, 2 ekor pejantan elba, 8 ekor ayam kampung Black Permud 2 (BP 2), dan 1 ekor pejantan ayam kampung BP 2.

Itu adalah beberapa aset fisik yang saya miliki. Bagi saya, aset bukan hanya soal uang atau bangunan, tapi juga **ilmu, pengalaman, dan semangat belajar** yang terus saya kembangkan.

Lewat platform ini, saya ingin berbagi perjalanan saya dalam membangun usaha peternakan. Secara umum tentang pengalaman merawat ayam-ayam saya, dan nanti secara khusus saya akan berbagi pengalaman pengelolaan peternakan dari sisi keuangan. Mengingat _background_ saya yang seorang akuntan setidaknya memiliki sedikit ilmu yang bisa saya bagikan kepada anda.

Konten yang saya buat akan fokus pada tiga hal:

1. **Cerita nyata** tentang perjalanan beternak ayam dari awal mulai sampai dengan hari ini.
2. **Penerapan akuntansi sederhana** untuk membantu peternak dan usaha kecil lebih rapi dalam pencatatan.
3. **Tips praktis** agar usaha menjadi lebih teratur, terukur, dan tentu saja, lebih menguntungkan.

Saya ingin membuktikan bahwa dengan **catatan yang rapi, usaha kecil pun bisa tumbuh besar**.  
Semoga konten ini bisa menjadi inspirasi, terutama bagi peternak pemula dan orang-orang yang ingin belajar akuntansi lewat contoh nyata.

Selamat datang di **akunternak.com – Rapi Catatannya, Rapi Usahanya, Keuntungan hasilnya**.  
Mari kita belajar bersama!
"""

# Pisah naskah jadi beberapa scene (tiap kalimat 1 slide)
scenes = [kal.strip() for kal in naskah.strip().split("\n") if kal.strip()]

# === 2. Buat slide video per scene ===
clips = []
for teks in scenes:
    wrapped_text = "\n".join(textwrap.wrap(teks, width=40))  # Bungkus biar rapi
    txt_clip = (
        TextClip(
            wrapped_text,
            fontsize=50,
            color='white',
            font='Arial-Bold',
            method='caption',       # <-- FIX: pakai Pillow, bukan ImageMagick
            size=(1280, 720)        # <-- FIX: atur resolusi biar rapi
        )
        .on_color(size=(1280, 720), color=(0, 0, 0), col_opacity=1)
        .set_duration(4)  # durasi per scene (detik)
        .set_position('center')
    )
    clips.append(txt_clip)

# === 3. Gabung semua scene ===
video = concatenate_videoclips(clips, method="compose")

# === 4. (Opsional) Tambah musik latar ===
try:
    audio = AudioFileClip("musik-latar.mp3").volumex(0.2)
    video = video.set_audio(audio)
except:
    print("Tidak ada musik latar, lanjut tanpa audio.")

# === 5. Export ===
video.write_videofile("video_teks.mp4", fps=24)
