class Queue:
    def __init__(self):
        self.queue = []
        
    def penambahan_pendaki(self, idTicket):
        self.queue.append(idTicket)
        
    def pengurangan_pendaki(self):
        #jika antrian tidak kosong, keluarkan pendaki pertama
        if not self.is_empty():
            return self.queue.pop(0)
        return None
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def waktu_tunggu(self):
        return len(self.queue) 