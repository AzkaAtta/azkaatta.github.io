import express from "express";
import { Boom } from "@hapi/boom";
import makeWASocket, { useMultiFileAuthState } from "@whiskeysockets/baileys";
import qrcode from "qrcode-terminal";
import cors from "cors";
import bodyParser from "body-parser";

const app = express();
const port = 3000;

app.use(cors());
app.use(bodyParser.json());

let sock;

async function startBot() {
  const { state, saveCreds } = await useMultiFileAuthState("session");
  sock = makeWASocket({
    auth: state,
    printQRInTerminal: true,
  });

  sock.ev.on("connection.update", (update) => {
    const { connection, qr } = update;
    if (qr) {
      qrcode.generate(qr, { small: true });
    }
    if (connection === "open") {
      console.log("✅ WhatsApp bot terhubung!");
    }
  });

  sock.ev.on("creds.update", saveCreds);
}

startBot();

app.post("/api/send-otp", async (req, res) => {
  const { phone } = req.body;
  if (!phone || !phone.startsWith("62")) {
    return res.status(400).json({ message: "Nomor tidak valid" });
  }

  const otp = Math.floor(100000 + Math.random() * 900000);

  try {
    await sock.sendMessage(`${phone}@s.whatsapp.net`, {
      text: `Kode OTP kamu adalah: ${otp}`,
    });
    console.log(`✅ OTP ${otp} dikirim ke ${phone}`);
    return res.json({ message: "OTP berhasil dikirim" });
  } catch (err) {
    console.error("❌ Gagal kirim OTP:", err);
    return res.status(500).json({ message: "Gagal kirim OTP" });
  }
});

app.listen(port, () => {
  console.log(`🚀 Server berjalan di http://localhost:${port}`);
});
