import networkx as nx  # Importación del paquete NetworkX
import matplotlib.pyplot as plt  # Importación del paquete Matplotlib
import tkinter as tk
from tkinter import messagebox

class ventana():
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("Havel-Hakimi Algorithm")
        self.window.geometry("600x300")
        self.window.configure(background="#FFFFFF")
        self.text = tk.StringVar()
        self.text.set("")
        self.label = tk.Label(self.window, textvariable=self.text)

        # Etiqueta de la secuencia de grados+
        self.label_secuencia = tk.Label(self.window, text="Secuencia de grados:", font=("Arial", 14), background="#FFFFFF")
        self.label_secuencia.place(x=50, y=50)
        self.label.pack()
        self.label_instruccion = tk.Label(self.window, text="Escribe la secuencia de forma espaciada(No use comas)", font=("Arial", 14),background="#FFFFFF")
        self.label_instruccion.place(x=50, y=200)
        self.label.pack()
        self.label_secuencia.pack()
        self.entry = tk.Entry(self.window, font=("Arial", 14), width=30)
        self.entry.place(x=250, y=50)
        self.entry.pack()
        self.button = tk.Button(self.window, text="Create graph",font=("Arial", 14), command=lambda: self.mostrar([d for d in self.entry.get().split()]))
        self.button.place(x=550, y=50)
        self.button.pack()
        self.button_exit = tk.Button(self.window, text="Exit", command=self.window.destroy, font=("Arial", 14) )
        self.button_exit.pack()
        self.button_exit.place(x=550, y=250)
        self.window.mainloop()

    def validacion(self) -> bool:
        try:
            secuencia = 0
            lista = [d for d in self.entry.get().split()]
            for i in lista:
                if isinstance(int(i), int) == False:
                    return False
            for i in lista:
                secuencia += int(i)
                if int(i) < 0:
                    return False
            if secuencia % 2 != 0:
                return False
            if len(lista) == 0:
                return False
            return True
        except ValueError:
            return False

    def  mostrar(self, secuencia: list):
        nueva = []
        try:
            nueva = [int(i) for i in secuencia]
        except ValueError:
            messagebox.showerror("Error", "La secuencia de grados no debe ser letras.")
            return
        
        valido = self.validacion()
        if valido == False:
            self.text.set("Invalid sequence")
            messagebox.showerror("Error", "La secuencia de grados debe ser una lista de números separados por espacios.")
        else:
            self.text.set("sequence valid")
            self.havel_hakimi(nueva)

    def graficar_grafo(self, secuencia: list[int]):
        G = nx.havel_hakimi_graph(secuencia)  # Generar el grafo simple G, dada una secuencia d, con el algoritmo H-H
        
        """# Dibujar el grafo en una figura de matplotlib
        fig, ax = plt.subplots()
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='red', font_color='white', font_weight='bold', font_size=16, edge_color='black', width=2, ax=ax)
        canvas_fig = FigureCanvasTkAgg(fig, master=self.canvas)
        canvas_fig.draw()

        # Mostrar la figura en una ventana secundaria
        self.canvas.create_window(500, 300, window=canvas_fig.get_tk_widget())"""

        # Dibujar el canvas
        
        plt.axis("equal")
        nx.draw(G, with_labels=True)
        plt.show()

    def havel_hakimi(self,seq, cop=None) -> bool:
        # if seq is empty or only contains zeros,
        # degree sequence is valid
        if cop is None:
            cop = seq.copy()
        if len(seq) < 1 or all(deg == 0 for deg in seq):
            print("Finished! Graph IS constructable with Havel Hakimi algorithm.")
            self.graficar_grafo(cop)
            return True

        print(seq, end="")
        seq.sort()
        print(" --sort--> ", end="")
        print(seq)

        last = seq[len(seq) - 1]
        if last > len(seq) - 1:
            print("Failed! Graph IS NOT constructable with Havel Hakimi algorithm.")
            return False

        print(seq, end="")

        # remove last element
        seq.remove(last)

        # iterate seq backwards
        for num in range(len(seq) - 1, len(seq) - last - 1, -1):
            if seq[num] > 0:
                seq[num] -= 1
            else:
                print("\nFailed! Graph is not constructable with Havel Hakimi algorithm")
                return False

        print(" --alg-->", end="")
        print(seq)

        # recursive call
        return self.havel_hakimi(seq, cop)

def main():
    ventana()

if __name__ == "__main__":
    main()