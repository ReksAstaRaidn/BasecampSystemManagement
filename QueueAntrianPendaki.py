class Queue:
    def __init__(self):
        self.queue = []
        
    def penambahan_pendaki(self, idTicket):
        self.queue.append(idTicket)
        
    def pengurangan_pendaki(self):
        #jika antrian tidak kosong, keluarkan pendaki pertama
        if not self.is_empty():
            pendaki_keluar = self.queue.pop(0)
            return pendaki_keluar
        return None
    
    def is_empty(self):
        return len(self.queue) == 0 # cek apakah antrian kosong
    
    def waktu_tunggu(self):
        return len(self.queue) # hitung jumlah pendaki dalam antrian untuk estimasi waktu tunggu