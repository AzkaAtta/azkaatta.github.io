---
layout: default
title: Daftar
---

<h2>Form Pendaftaran via WhatsApp</h2>

<form id="otpForm">
  <label>Nomor WhatsApp (format 62xxx):</label><br>
  <input type="text" id="phone" required /><br><br>

  <button type="button" onclick="sendOtp()">Kirim OTP</button><br><br>

  <div id="otpSection" style="display:none;">
    <label>Masukkan OTP:</label><br>
    <input type="text" id="otp" /><br><br>
    <button type="button" onclick="verifyOtp()">Verifikasi OTP</button>
  </div>

  <p id="result"></p>
</form>

<script>
const apiUrl = "http://localhost:3000"; // ubah jika beda server

function sendOtp() {
  const phone = document.getElementById("phone").value;
  fetch(`${apiUrl}/api/send-otp`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ phone })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("result").innerText = data.message;
    if (data.message === "OTP berhasil dikirim") {
      document.getElementById("otpSection").style.display = "block";
    }
  })
  .catch(err => {
    console.error(err);
    document.getElementById("result").innerText = "Gagal kirim OTP";
  });
}

function verifyOtp() {
  const phone = document.getElementById("phone").value;
  const otp = document.getElementById("otp").value;

  fetch(`${apiUrl}/api/verify-otp`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ phone, otp })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("result").innerText = data.message;
  })
  .catch(err => {
    console.error(err);
    document.getElementById("result").innerText = "Gagal verifikasi OTP";
  });
}
</script>
