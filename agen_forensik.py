from utilitas import BUKTI_BERBAHAYA, lapor_komandan

class AgenForensik:
    def __init__(self):
        self.nama = "Agen Forensik"

    def periksa_tkp(self, set_barang_tkp):
        # Cari barang yang ada di TKP dan juga ada di database barang berbahaya
        barang_sus = [barang for barang in set_barang_tkp if barang.lower() in BUKTI_BERBAHAYA]

        if len(barang_sus) > 0:
            status = f"Ditemukan bukti fatal: {', '.join(barang_sus)}!"
        else:
            status = "Aman, cuma barang-barang normal di TKP."

        lapor_komandan(self.nama, status)
        
        # Kembalikan jumlah poin kecurigaan (makin banyak barang sus, poin makin tinggi)
        return len(barang_sus)