from agen_forensik import AgenForensik
from agen_psikolog import AgenPsikolog

def main():
    print("=== BIRO DETEKTIF: KASUS MISTERI HARI INI ===\n")
    
    # Panggil agen-agennya
    detektif_tkp = AgenForensik()
    detektif_interogasi = AgenPsikolog()

    data_tkp = ["kunci motor", "pisau", "jaket", "bercak darah"]
    data_wawancara = ["minta minum", "gugup", "keringat dingin", "ngantuk"]

    print("-> Mengirim Agen Forensik ke lokasi kejadian...")
    poin_tkp = detektif_tkp.periksa_tkp(data_tkp)

    print("\n-> Membawa tersangka ke ruang interogasi...")
    poin_wawancara = detektif_interogasi.baca_pikiran(data_wawancara)

    print("\n==============================")
    print("=== KESIMPULAN AKHIR KASUS ===")
    print("==============================")
    
    # Hitung total kecurigaan dari kedua agen
    total_sus = poin_tkp + poin_wawancara
    
    if total_sus >= 3:
        print("VONIS: TANGKAP DIA! Bukti fisik dan gelagat psikologis valid!")
    elif total_sus > 0:
        print("VONIS: Jadikan tahanan kota. Dia masih berpotensi sebagai pelaku.")
    else:
        print("VONIS: Bebaskan. Salah tangkap, dia innocent.")

if __name__ == "__main__":
    main()