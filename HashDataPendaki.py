class Hash:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def _hash(self, idTicket):
        #ambil angka dari idTicket
        numeric_part = int (''.join(filter(str.isdigit, idTicket)))
        #
        return numeric_part % self.size
    
    def cek_duplikat_id(self, idTicket):
        index = self._hash(idTicket)
        for data in self.table[index]:
            if data["id"] == idTicket:
                return True
        return False

    def daftar_pendaki(self, idTicket, nama, kontak):
        index = self._hash(idTicket)
        if self.cek_duplikat_id(idTicket):
            return False

        dataPendaki = {"id": idTicket, "nama": nama, "kontak": kontak}
        self.table[index].append(dataPendaki)
        return True
        
    def verifikasi_pendaki(self, idTicket):
        index = self._hash(idTicket)
        #cari data dengan idTicket yang sesuai
        for data in self.table[index]:
            if data["id"] == idTicket:
                return data
        return None
        
    def cek_seluruh_id(self):
        #ambil semua idTicket yang terdaftar
        id_list = []
        for bucket in self.table:
            for data in bucket:
                id_list.append(data["id"])
        return id_list