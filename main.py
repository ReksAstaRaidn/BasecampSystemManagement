from HashDataPendaki import Hash 
from QueueAntrianPendaki import Queue
from GraphJalur import Graph
from StackRiwayat import Stack

class SistemManajemenPendaki:
    def __init__(self):
        self.dataPendaki = Hash(size = 1000)
        self.antrianPendaki = Queue()
        self.jalurPendakian = Graph()
        self.riwayatPendaki = Stack()
        
    def map_jalur_pendakian(self):
        pos_pendakian = ["Basecamp", "Pos 1", "Pos 2", "Pos 3", "Puncak"]
        
        # tambahkan pos ke dalam graph
        for pos in pos_pendakian:
            self.jalurPendakian.tambah_pos(pos)
        
        # tambahkan jalur dengan jarak antar pos
        self.jalurPendakian.tambah_jalur("Basecamp", "Pos 1", 200)
        self.jalurPendakian.tambah_jalur("Pos 1", "Pos 2", 320)
        self.jalurPendakian.tambah_jalur("Pos 2", "Pos 3", 400)
        self.jalurPendakian.tambah_jalur("Pos 3", "Puncak", 150)
        print("Peta jalur pendakian telah dibuat.")
        
    def daftar_dan_antri_pendaki(self, idTicket, nama, kontak):
        # jika ID sudah ada di riwayat, tolak pendaftaran jika datanya berbeda
        riwayat_data = self.riwayatPendaki.find_by_id(idTicket)
        if riwayat_data is not None:
            if riwayat_data.get("nama") != nama or riwayat_data.get("kontak") != kontak:
                print(f"\nID Ticket {idTicket} sudah digunakan oleh pendaki {riwayat_data.get('nama')} di riwayat. Pendaki berbeda tidak dapat menggunakan ID yang sama.")
            else:
                print(f"\nID Ticket {idTicket} sudah pernah digunakan dan tidak dapat didaftarkan ulang.")
            return

        # daftarkan pendaki dan tambahkan ke antrian jika ID belum ada
        if self.dataPendaki.daftar_pendaki(idTicket, nama, kontak):
            pendaki = self.dataPendaki.verifikasi_pendaki(idTicket)
            self.antrianPendaki.penambahan_pendaki(pendaki)
            print(f"\nPendaki {nama} (ID: {idTicket}) telah terdaftar dan masuk antrian.")
        else:
            print(f"\nID Ticket {idTicket} sudah terdaftar. Gunakan ID yang berbeda untuk pendaki baru.")
        
    def kirim_pendaki(self, kuota):
        print(f"\nMengirim pendaki ke jalur pendakian dengan kuota: {kuota}")
        dikirim = 0
        while dikirim < kuota and not self.antrianPendaki.is_empty(): # pastikan masih ada pendaki dalam antrian
            pendaki = self.antrianPendaki.pengurangan_pendaki()
            if pendaki is not None:
                self.riwayatPendaki.push(pendaki)
                print(f"Pendaki {pendaki['nama']} (ID: {pendaki['id']}) telah dikirim ke jalur pendakian.")
                dikirim += 1
            
        if self.antrianPendaki.is_empty() and dikirim < kuota:
            print("Antrian pendaki sudah kosong, tidak ada lagi yang bisa dikirim.")
            
    def tampilkan_seluruh_id_pendaki(self):
        id_list = self.dataPendaki.cek_seluruh_id()
        print("\nDaftar ID Ticket Pendaki yang Terdaftar:")
        for idTicket in id_list:
            print(f"- {idTicket}")
            
    def list_pendaki_riwayat(self):
        print("\nRiwayat Pendaki yang Telah Mendaki:")
        if self.riwayatPendaki.is_empty():
            print("Belum ada pendaki yang mendaki.")
        else:
            for i in range(self.riwayatPendaki.size()):
                pendaki = self.riwayatPendaki.stack[i]
                print(f"- {pendaki['nama']} (ID: {pendaki['id']}), Kontak: {pendaki['kontak']}")
        
if __name__ == "__main__":
    sistem_mendaki = SistemManajemenPendaki()
    print("Selamat datang di Sistem Manajemen Pendaki Gunung!")
    sistem_mendaki.map_jalur_pendakian()
    
    while True:
        print("\n[MENU PETUGAS BASECAMP]")
        print("="*30)
        print("[1] Lihat Peta Jalur Pendakian")
        print("[2] Daftarkan Pendaki")
        print("[3] Atur Kirim Pendaki ke Jalur")
        print("[4] Cek Identitas Pendaki")
        print("[5] Cek Sisa Antrian Basecamp")
        print("[6] Lihat Riwayat Pendaki")
        print("[0] Keluar") 
        
        pilihan = input("Masukkan pilihan: ")
        
        if pilihan == "1":
            print("\n[PETA JALUR PENDAKIAN]")
            print("="*30)
            print("[1] Peta Teks")
            print("[2] Visualisasi Grafis")
            sub_pilihan = input("Pilih jenis peta: ")
            if sub_pilihan == "1":
                sistem_mendaki.jalurPendakian.show_jalur()
            elif sub_pilihan == "2":
                sistem_mendaki.jalurPendakian.visualisasi_jalur()
            else:
                print("Pilihan tidak valid. Kembali ke menu utama.")            
        
        elif pilihan == "2":
            idTicket = input("Masukkan ID Ticket (Contoh: MT-001): ")
            nama = input("Masukkan Nama Pendaki: ")
            kontak = input("Masukkan Kontak Darurat: ")
            sistem_mendaki.daftar_dan_antri_pendaki(idTicket, nama, kontak)
            
        elif pilihan == "3":
            try:
                kirim = int(input("Berapa Pendaki yang akan dikirim: "))
                sistem_mendaki.kirim_pendaki(kirim)
            except ValueError:
                print("Input tidak valid. Harap masukkan angka untuk kuota.")
            
        elif pilihan == "4":
            sistem_mendaki.tampilkan_seluruh_id_pendaki()
            cari_id = input("Masukkan ID Ticket yang ingin dicari: ")
            hasil = sistem_mendaki.dataPendaki.verifikasi_pendaki(cari_id)
            if hasil:
                print(f"Data Pendaki ditemukan: Nama: {hasil['nama']}, Kontak: {hasil['kontak']}")
            else:
                print("Data Pendaki tidak ditemukan.")
                
        elif pilihan == "5":
            sisa_antrian = sistem_mendaki.antrianPendaki.waktu_tunggu()
            print(f"Sisa antrian di Basecamp: {sisa_antrian} pendaki")
            
        elif pilihan == "6":
            sistem_mendaki.list_pendaki_riwayat()
            
        elif pilihan == "0":
            print("Terima kasih telah menggunakan Sistem Manajemen Pendaki Gunung. Sampai jumpa!")
            break
        
        else:
            print("Pilihan tidak valid. Pilih dari 0-5.")