import requests
import json
import datetime

API_KEY = "AIzaSyAlS-ePk_zlC6EOKVFo72ZdVBUDU953TkA"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

tanggal = datetime.datetime.now().strftime("%Y-%m-%d")

prompt = f"""
Tolong buatkan file konten blog dalam format markdown dengan struktur seperti untuk Jekyll. 
Konten yang harus dibuat:

- Judul: Jasa Livestreaming TikTok Profesional dan Viral
- Meta deskripsi dan keyword lengkap
- Schema lengkap dalam bentuk JSON-LD tanpa "organization", hanya sebagai artikel.
- Gambar ada setelah schema, pakai gambar bebas contoh
- Link WhatsApp tepat di bawah gambar
- Konten isi 600 kata tentang jasa livestreaming TikTok, dengan kata kunci sangat banyak dan sering dicari (contoh: jasa livestreaming tiktok, beli live tiktok, jasa siaran tiktok murah, penonton live tiktok aktif, dll)
- Gunakan SEO yang kuat
- Buat FAQ model accordion (4 pertanyaan)
- Buat konten tersembunyi dengan tombol "Baca Selengkapnya" dan bisa ditutup lagi
- Tulis semua dalam markdown
- Jangan tulis ulang petunjuk ini, langsung mulai dari YAML front matter

Gunakan format ini:
---
title: "Judul..."
description: "..."
keywords: "..., ..., ..."
date: {tanggal}
---

<script type="application/ld+json">
{{ schema json here }}
</script>

![Gambar](https://example.com/livestream.jpg)

[Hubungi via WhatsApp](https://wa.me/6281234567890)

### Isi Artikel...

(600 kata SEO)

### FAQ (Accordion)

(buat 4 pertanyaan dan jawabannya)

### Konten Tersembunyi

Gunakan HTML dan JavaScript sederhana agar bisa tampil/sembunyi konten
"""

headers = {
    "Content-Type": "application/json"
}

data = {
    "contents": [{
        "parts": [{
            "text": prompt
        }]
    }]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    try:
        result = response.json()
        content = result['candidates'][0]['content']['parts'][0]['text']
        filename = "jasa-livestreaming-tiktok.md"
        with open(filename, "w") as f:
            f.write(content)
        print(f"✅ Konten berhasil disimpan ke {filename}")
    except Exception as e:
        print("❌ Gagal parsing hasil:", e)
else:
    print(f"❌ Error {response.status_code}:", response.text)
