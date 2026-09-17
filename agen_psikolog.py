from utilitas import GELAGAT_BOHONG, lapor_komandan

class AgenPsikolog:
    def __init__(self):
        self.nama = "Agen Psikolog"

    def baca_pikiran(self, set_gelagat):
        # Cari gelagat yang nunjukin dia bohong
        tanda_bohong = [sikap for sikap in set_gelagat if sikap.lower() in GELAGAT_BOHONG]

        if len(tanda_bohong) >= 2:
            status = f"Fix bohong Ndan! Tersangka nunjukin gelagat: {', '.join(tanda_bohong)}"
        elif len(tanda_bohong) == 1:
            status = f"Agak mencurigakan, dia mulai {tanda_bohong[0]}."
        else:
            status = "Tersangka santai, kemungkinan besar dia jujur."

        lapor_komandan(self.nama, status)
        
        # Kembalikan poin kecurigaan dari interogasi
        return len(tanda_bohong)