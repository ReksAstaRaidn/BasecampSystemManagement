import graphviz
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os   

class Graph:
    def __init__(self):
        self.adjacency_list = {}
        
        self.posisi = {
            "Basecamp": "0, 0!",
            "Pos 1": "-1.2, 2.5!",
            "Pos 2": "1.2, 5.0!",
            "Pos 3": "-1.2, 7.5!",
            "Puncak": "0, 10.0!"
        }
        
    def tambah_pos(self, pos):
       if pos not in self.adjacency_list:
           self.adjacency_list[pos] = []
           
    def tambah_jalur(self, pos1, pos2, jarak):
        if pos1 in self.adjacency_list and pos2 in self.adjacency_list:
           self.adjacency_list[pos1].append({"ke": pos2, "jarak": jarak})
           self.adjacency_list[pos2].append({"ke": pos1, "jarak": jarak})
           
    def show_jalur(self):
        print("\nJalur Pendakian:")
        #tampilkan jalur dengan format yang lebih rapi
        for pos, jalur in self.adjacency_list.items():
            koneksi = ", ".join([f"{j['ke']} (jarak: {j['jarak']} km)" for j in jalur])
            print(f"[{pos}] terhubung ke: {koneksi if koneksi else 'Tidak ada jalur'}")
            
    def visualisasi_jalur(self):
        print("\nVisualisasi Jalur Pendakian:")
        #buat graph tak berarah dengan graphviz
        dot = graphviz.Digraph('Peta_Pendakian', comment='Jalur Pendakian', engine='neato')
        dot.attr(size='8,11')
        
        #atur gaya node dan edge 
        dot.attr('node', shape='ellipse', style='filled', color='darkgreen', fontcolor='white', fontsize='11', width='1,2', height='0.6', fontname='Helvetica')
        dot.attr('edge', color='gray', style='dashed', fontcolor='red', fontname='Helvetica', fontsize='16', arrowsize='0.7')
        
        for pos in self.adjacency_list.keys():
            if pos in self.posisi:
                dot.node(pos, pos, pos=self.posisi[pos])
            else:
                dot.node(pos, pos)
            
        drawn_edges = set()
        
        for pos, jalur in self.adjacency_list.items():
            for j in jalur:
                target = j['ke']
                jarak = j['jarak']
                
                edge = tuple(sorted([pos, target]))
                if edge not in drawn_edges:
                    dot.edge(pos, target, label=f"{jarak} km")
                    drawn_edges.add(edge)
                    
        try:
            filename = 'jalur_pendakian'
            dot.render(filename, format='png', view=False, cleanup=True)
            
            img_path = f"{filename}.png"
            img = mpimg.imread(img_path)
            
            fig, ax = plt.subplots(figsize=(7, 9))
            ax.imshow(img)
            ax.axis('off')
            
            plt.title("Peta Jalur Pendakian", fontsize=16, fontweight='bold', pad=20)
            
            plt.tight_layout()
            plt.show()
            
            if os.path.exists(img_path):
                os.remove(img_path)
            
        except Exception as e:
            print(f"Gagal membuat visualisasi jalur pendakian: {e}")
        
        
        