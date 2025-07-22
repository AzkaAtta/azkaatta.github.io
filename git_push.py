import subprocess
from datetime import datetime

def generate_markdown():
    title = "Jasa Livestreaming TikTok Profesional dan Murah"
    filename = "jasa-livestreaming-tiktok.md"
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    meta_description = "Jasa livestreaming TikTok terpercaya, murah, aman, dan cepat. Cocok untuk menaikkan brand dan penjualan dengan sistem real human."
    meta_keywords = "jasa livestreaming tiktok, jasa live tiktok, jual live tiktok, beli live tiktok, live tiktok murah, live tiktok real, live tiktok aman, jasa buzzer tiktok"

    schema = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "{title}",
  "description": "{meta_description}",
  "keywords": "{meta_keywords}",
  "datePublished": "{date}"
}}
</script>
"""

    image_html = '<img src="/assets/img/livestreaming.jpg" alt="Jasa Livestreaming TikTok" />'

    whatsapp_link = '<p><a href="https://wa.me/6281234567890" target="_blank">Hubungi via WhatsApp</a></p>'

    accordion = """
<details>
  <summary>Apa itu jasa livestreaming TikTok?</summary>
  <p>Jasa livestreaming TikTok adalah layanan untuk membantu kamu tampil live secara profesional guna meningkatkan penjualan dan kepercayaan audiens.</p>
</details>
<details>
  <summary>Apakah aman menggunakan jasa ini?</summary>
  <p>Sangat aman karena semua dilakukan secara manual oleh tim real human, bukan bot.</p>
</details>
<details>
  <summary>Berapa biaya layanan ini?</summary>
  <p>Harga mulai dari Rp100.000 per sesi tergantung durasi dan kebutuhan.</p>
</details>
<details>
  <summary>Berapa lama proses pengerjaan?</summary>
  <p>Biasanya bisa langsung mulai dalam 1x24 jam setelah pemesanan dan konfirmasi.</p>
</details>
"""

    hidden_content = """
<details>
  <summary>Baca selengkapnya</summary>
  <p>Jika kamu mencari jasa livestreaming TikTok yang murah, cepat, dan terpercaya, kami adalah pilihan terbaik. Dengan pengalaman bertahun-tahun, kami membantu banyak UMKM dan brand besar tampil di TikTok live secara profesional. Kata kunci: jasa livestreaming TikTok, jasa live murah, live cepat, beli jasa live, cari jasa live TikTok, butuh live real TikTok, jasa live terpercaya, jasa live aman TikTok, jasa buzzer live TikTok, paket live murah.</p>
</details>
"""

    content = f"""---
title: "{title}"
date: {date}
description: "{meta_description}"
keywords: "{meta_keywords}"
---

{schema}

{image_html}

{whatsapp_link}

## {title}

Kami menyediakan jasa livestreaming TikTok terbaik untuk kebutuhan promosi produk, branding, dan marketing secara langsung. Dengan tim profesional dan pengalaman lebih dari 5 tahun, kami siap membantu menaikkan visibilitas akun TikTok kamu secara organik dan cepat.

### Kenapa Harus Menggunakan Jasa Livestreaming TikTok dari Kami?

- Profesional & berpengalaman
- Harga murah & terjangkau
- 100% real human
- Aman & tidak melanggar ketentuan TikTok
- Mendukung semua jenis bisnis

### Layanan Kami Termasuk:

- Live review produk
- Host TikTok live
- Support interaksi & komentar
- Promosi & buzzer live

{accordion}

{hidden_content}
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Konten berhasil disimpan ke {filename}")

def git_push_commit(message):
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)
        subprocess.run(["git", "push"], check=True)
        print("✅ Push ke GitHub berhasil.")
    except subprocess.CalledProcessError as e:
        print("❌ Git error:", e)

# Jalankan otomatis
generate_markdown()
git_push_commit("Add jasa livestreaming tiktok content")
