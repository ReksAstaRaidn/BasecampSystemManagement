class Hash:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def _hash(self, idTicket):
        #ambil angka dari idTicket
        numeric_part = int (''.join(filter(str.isdigit, idTicket)))
        #
        return numeric_part % self.size
    
    def daftar_pendaki(self, idTicket, nama, kontak):
        index = self._hash(idTicket)
        dataPendaki = {"id": idTicket, "nama": nama,"kontak": kontak}
        #cek apakah idTicket sudah ada, jika tidak ada tambahkan data baru
        for i, data in enumerate(self.table[index]):
            if data["id"] == idTicket:
                self.table[index][i] = dataPendaki
                return
            
        self.table[index].append(dataPendaki)
        
    def verifikasi_pendaki(self, idTicket):
        index = self._hash(idTicket)
        #cari data dengan idTicket yang sesuai
        for data in self.table[index]:
            if data["id"] == idTicket:
                return data
        return None
        