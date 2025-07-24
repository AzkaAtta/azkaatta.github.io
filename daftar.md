---
layout: default
title: Daftar OTP WhatsApp
permalink: /daftar/
---

<style>
body {
  font-family: sans-serif;
  background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
  color: white;
  text-align: center;
  padding-top: 100px;
}
input {
  padding: 12px;
  width: 250px;
  font-size: 16px;
  border-radius: 8px;
  border: none;
}
button {
  margin-top: 20px;
  padding: 12px 30px;
  font-size: 16px;
  background-color: #25D366;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}
</style>

# 🟢 Pendaftaran via WhatsApp OTP

Masukkan nomor WhatsApp kamu di bawah ini, dan sistem akan mengirimkan kode OTP ke nomor tersebut secara otomatis.

<br><br>

<input type="text" id="phone" placeholder="Masukkan nomor WhatsApp (format 62...)">
<br>
<button onclick="kirimOTP()">Kirim OTP</button>

<script>
async function kirimOTP() {
  const phone = document.getElementById("phone").value.trim();
  if (!phone.match(/^62\d{9,}$/)) {
    alert("Nomor tidak valid. Gunakan format: 628xxxx...");
    return;
  }

  const response = await fetch("https://yourdomain.com/api/send-otp", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ phone })
  });

  const result = await response.json();
  alert(result.message || "OTP berhasil dikirim ke WhatsApp kamu!");
}
</script>


