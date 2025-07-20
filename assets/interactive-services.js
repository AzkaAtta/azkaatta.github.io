function toggleService(element) {
    const item = element.closest('.tiktok-service-item');
    const content = item.querySelector('.tiktok-service-content');

    // Cek apakah item ini sudah terbuka
    const isCurrentlyOpen = item.classList.contains('open');

    // Tutup semua item lain yang mungkin sedang terbuka
    document.querySelectorAll('.tiktok-service-item.open').forEach(openItem => {
        if (openItem !== item) { // Jangan tutup item yang sedang diklik jika dia yang akan dibuka
            openItem.querySelector('.tiktok-service-content').style.maxHeight = '0';
            openItem.querySelector('.tiktok-service-content').style.paddingBottom = '0';
            openItem.classList.remove('open');
        }
    });

    if (!isCurrentlyOpen) {
        // Jika item yang diklik tadi tertutup, sekarang buka
        content.style.maxHeight = content.scrollHeight + 'px'; // Sesuaikan tinggi dengan konten
        content.style.paddingBottom = '20px'; // Tambahkan padding lagi
        item.classList.add('open');
    } else {
        // Jika item yang diklik tadi sudah terbuka, tutup
        content.style.maxHeight = '0';
        content.style.paddingBottom = '0';
        item.classList.remove('open');
    }
}
