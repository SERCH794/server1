import tkinter as tk
from tkinter import ttk
import math
import random

class ArbolImposibleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🌳 ÁRBOL IMPOSIBLE - RUPTURA RÁPIDA")
        self.root.geometry("900x750")
        self.root.configure(bg="#1a1a2e")
        
        # Variables del juego
        self.altura_arbol = 1.7
        self.altura_maxima = 500  # Colapsa a los 500 metros
        self.puntuacion = 0
        self.colapso_ocurrido = False
        self.creciendo = False
        self.animacion_activa = False
        
        self.setup_ui()
        self.update_display()
    
    def setup_ui(self):
        # Título
        titulo = tk.Label(self.root, text="🌳 SIMULADOR DE ÁRBOL IMPOSIBLE 🌳", 
                         font=("Arial", 20, "bold"), bg="#1a1a2e", fg="#ffd700")
        titulo.pack(pady=10)
        
        # Canvas para dibujar
        self.canvas = tk.Canvas(self.root, width=800, height=450, bg="#87CEEB")
        self.canvas.pack(pady=10)
        
        # Botón de crecimiento
        self.btn_crecer = tk.Button(self.root, text="🌱 CRECER +10 METROS 🌱", 
                                    font=("Arial", 16, "bold"), bg="#00a8cc", 
                                    fg="white", padx=30, pady=15, cursor="hand2")
        self.btn_crecer.pack(pady=10)
        self.btn_crecer.config(command=self.crecer_arbol)
        
        # Botón reset
        self.btn_reset = tk.Button(self.root, text="🔄 REINICIAR 🌳", 
                                   command=self.reiniciar,
                                   font=("Arial", 12, "bold"), bg="#e94560", 
                                   fg="white", padx=20, pady=8, cursor="hand2")
        self.btn_reset.pack(pady=10)
        
        # Barra de estrés
        tk.Label(self.root, text="⚠️ ESTRÉS ESTRUCTURAL ⚠️", 
                font=("Arial", 10, "bold"), bg="#1a1a2e", fg="#ffd700").pack()
        self.progress = ttk.Progressbar(self.root, length=600, mode='determinate')
        self.progress.pack(pady=5)
        
        # Label para información (¡ESTE FALTABA!)
        self.info_label = tk.Label(self.root, text="", font=("Arial", 12), 
                                   bg="#1a1a2e", fg="white")
        self.info_label.pack(pady=5)
        
        # Área de mensajes
        self.mensaje_text = tk.Text(self.root, height=6, width=80, 
                                   font=("Arial", 9), bg="#0f3460", 
                                   fg="white", wrap=tk.WORD)
        self.mensaje_text.pack(pady=10)
        self.mensaje_text.insert(tk.END, "🌱 ¡Presiona CRECER para hacer crecer el árbol! Llegará a 500m y colapsará\n")
        self.mensaje_text.config(state=tk.DISABLED)
    
    def crecer_arbol(self):
        if self.colapso_ocurrido:
            self.agregar_mensaje("❌ El árbol ya colapsó. ¡Presiona REINICIAR!")
            return
        if self.animacion_activa:
            return
        
        # Crecer 10 metros por clic
        self.altura_arbol += 10
        self.puntuacion += 10
        
        # Calcular estrés
        estres = min(100, (self.altura_arbol / self.altura_maxima) * 100)
        self.progress['value'] = estres
        
        self.agregar_mensaje(f"📏 Altura: {self.altura_arbol:.1f} m | Estrés: {estres:.1f}%")
        
        # Verificar colapso
        if self.altura_arbol >= self.altura_maxima:
            self.colapsar_arbol()
        else:
            self.update_display()
    
    def colapsar_arbol(self):
        self.colapso_ocurrido = True
        self.animacion_activa = True
        self.agregar_mensaje("💥 ¡EL ÁRBOL ALCANZÓ SU LÍMITE! 💥")
        self.animacion_ruptura()
    
    def animacion_ruptura(self):
        """Animación de 5 pasos"""
        
        def paso1():
            self.canvas.delete("all")
            self.canvas.create_rectangle(0, 0, 800, 400, fill="#87CEEB", outline="")
            self.canvas.create_rectangle(0, 400, 800, 450, fill="#2d5016", outline="")
            
            # Árbol normal
            self.canvas.create_rectangle(375, 100, 425, 420, fill="#8B4513", outline="#5c3a21", width=2)
            self.canvas.create_oval(340, 60, 460, 160, fill="#228B22", outline="#006400", width=2)
            
            # Grietas
            self.canvas.create_line(390, 200, 410, 220, fill="red", width=4)
            self.canvas.create_line(385, 240, 415, 260, fill="red", width=4)
            self.canvas.create_line(395, 280, 405, 300, fill="red", width=4)
            
            self.canvas.create_text(400, 30, text="💥 ¡GRIETAS EN EL TRONCO! 💥", 
                                   font=("Arial", 18, "bold"), fill="red")
            self.root.after(500, paso2)
        
        def paso2():
            self.canvas.delete("all")
            self.canvas.create_rectangle(0, 0, 800, 400, fill="#87CEEB", outline="")
            self.canvas.create_rectangle(0, 400, 800, 450, fill="#2d5016", outline="")
            
            # Árbol partiéndose
            self.canvas.create_polygon(350, 100, 390, 100, 390, 420, 350, 420,
                                      fill="#8B4513", outline="#5c3a21", width=2)
            self.canvas.create_polygon(410, 100, 450, 100, 450, 420, 410, 420,
                                      fill="#CD853F", outline="#5c3a21", width=2)
            
            self.canvas.create_oval(330, 60, 400, 160, fill="#228B22", outline="#006400", width=2)
            self.canvas.create_oval(400, 60, 470, 160, fill="#228B22", outline="#006400", width=2)
            
            self.canvas.create_text(400, 30, text="🌪️ ¡SE PARTE POR LA MITAD! 🌪️", 
                                   font=("Arial", 18, "bold"), fill="orange")
            self.root.after(500, paso3)
        
        def paso3():
            self.canvas.delete("all")
            self.canvas.create_rectangle(0, 0, 800, 400, fill="#87CEEB", outline="")
            self.canvas.create_rectangle(0, 400, 800, 450, fill="#2d5016", outline="")
            
            # Mitades separadas
            self.canvas.create_polygon(320, 100, 370, 100, 370, 420, 320, 420,
                                      fill="#8B4513", outline="#5c3a21", width=2)
            self.canvas.create_polygon(430, 100, 480, 100, 480, 420, 430, 420,
                                      fill="#CD853F", outline="#5c3a21", width=2)
            
            # Astillas
            for _ in range(50):
                x = random.randint(350, 450)
                y = random.randint(180, 350)
                self.canvas.create_rectangle(x, y, x+5, y+8, fill="#8B4513")
            
            self.canvas.create_text(400, 30, text="💨 ¡ASTILLAS VOLANDO! 💨", 
                                   font=("Arial", 18, "bold"), fill="darkred")
            self.root.after(500, paso4)
        
        def paso4():
            self.canvas.delete("all")
            self.canvas.create_rectangle(0, 0, 800, 400, fill="#87CEEB", outline="")
            self.canvas.create_rectangle(0, 400, 800, 450, fill="#2d5016", outline="")
            
            # Tronco caído
            self.canvas.create_rectangle(280, 380, 520, 395, fill="#8B4513", outline="#5c3a21", width=2)
            
            # Hojas esparcidas
            for _ in range(80):
                x = random.randint(250, 550)
                y = random.randint(360, 430)
                self.canvas.create_oval(x, y, x+5, y+5, fill="#228B22")
            
            self.canvas.create_text(400, 100, text="💀 ¡ÁRBOL DESTRUIDO! 💀", 
                                   font=("Arial", 28, "bold"), fill="darkred")
            self.canvas.create_text(400, 150, text="No superó los límites físicos", 
                                   font=("Arial", 14), fill="white")
            self.root.after(800, paso5)
        
        def paso5():
            self.mostrar_ventana_colapso()
            self.animacion_activa = False
        
        paso1()
    
    def mostrar_ventana_colapso(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("📚 ¿POR QUÉ COLAPSÓ EL ÁRBOL?")
        ventana.geometry("600x500")
        ventana.configure(bg="#1a1a2e")
        
        tk.Label(ventana, text="🌳❌🌳", font=("Arial", 40), bg="#1a1a2e", fg="#e94560").pack(pady=10)
        tk.Label(ventana, text="EL ÁRBOL NO SUPERO LOS LÍMITES FÍSICOS", 
                font=("Arial", 14, "bold"), bg="#1a1a2e", fg="#ffd700").pack()
        
        texto = tk.Text(ventana, wrap=tk.WORD, font=("Arial", 11), 
                       bg="#0f3460", fg="white", padx=15, pady=15)
        texto.pack(pady=15, padx=20, fill=tk.BOTH, expand=True)
        
        explicacion = """
╔══════════════════════════════════════════════════════════════╗
║              🔬 ¿POR QUÉ NO PUEDE CRECER MÁS? 🔬             ║
╚══════════════════════════════════════════════════════════════╝

1️⃣ RESISTENCIA DE MATERIALES
   • El peso crece con el VOLUMEN (altura³)
   • La sección del tronco crece con altura²
   • Tensión de compresión ∝ ALTURA
   • A 500 metros: ¡la madera se pulveriza!

2️⃣ TRANSPORTE DE SAVIA
   • Límite físico por capilaridad: ~300 metros
   • Más allá: CAVITACIÓN (burbujas de vapor)
   • ¡El agua NO puede subir!

3️⃣ GRAVEDAD Y ENERGÍA
   • Energía para subir nutrientes = m × g × h
   • El costo energético supera la fotosíntesis

4️⃣ TIEMPO DE CRECIMIENTO
   • Una secuoya tarda 2000 años en llegar a 100m
   • Para 500m tomaría 10,000 años

🎯 CONCLUSIÓN: Los árboles reales máximo ~120m
   ¡La física de materiales LO IMPIDE!
        """
        
        texto.insert(tk.END, explicacion)
        texto.config(state=tk.DISABLED)
        
        tk.Button(ventana, text="ENTENDIDO ✓", command=ventana.destroy,
                 font=("Arial", 12, "bold"), bg="#00a8cc", fg="white",
                 padx=20, pady=8).pack(pady=15)
    
    def agregar_mensaje(self, msg):
        self.mensaje_text.config(state=tk.NORMAL)
        self.mensaje_text.insert(tk.END, msg + "\n")
        self.mensaje_text.see(tk.END)
        self.mensaje_text.config(state=tk.DISABLED)
    
    def update_display(self):
        if self.animacion_activa:
            return
        
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, 800, 400, fill="#87CEEB", outline="")
        self.canvas.create_rectangle(0, 400, 800, 450, fill="#2d5016", outline="")
        
        if not self.colapso_ocurrido:
            # Altura en pantalla
            altura_px = min(350, (self.altura_arbol / self.altura_maxima) * 350)
            
            # Color según estrés
            if self.altura_arbol >= 400:
                color = "#FF6347"
            elif self.altura_arbol >= 300:
                color = "#CD853F"
            else:
                color = "#8B4513"
            
            # Dibujar árbol
            self.canvas.create_rectangle(375, 420 - altura_px, 425, 420,
                                        fill=color, outline="#5c3a21", width=2)
            self.canvas.create_oval(340, 420 - altura_px - 50, 460, 420 - altura_px,
                                   fill="#228B22", outline="#006400", width=2)
            
            # Texto
            self.canvas.create_text(400, 30, text=f"🌳 Altura: {self.altura_arbol:.1f} metros",
                                   font=("Arial", 16, "bold"), fill="black")
            
            if self.altura_arbol >= 120:
                self.canvas.create_text(400, 60, text="⚠️ ¡EXCEDE LÍMITE NATURAL! ⚠️",
                                       font=("Arial", 12, "bold"), fill="red")
        
        self.info_label.config(text=f"📊 PUNTOS: {int(self.puntuacion)}")
    
    def reiniciar(self):
        self.altura_arbol = 1.7
        self.puntuacion = 0
        self.colapso_ocurrido = False
        self.animacion_activa = False
        self.progress['value'] = 0
        
        self.mensaje_text.config(state=tk.NORMAL)
        self.mensaje_text.delete(1.0, tk.END)
        self.mensaje_text.insert(tk.END, "🌱 ¡ÁRBOL REINICIADO! Presiona CRECER para empezar...\n")
        self.mensaje_text.config(state=tk.DISABLED)
        
        self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    game = ArbolImposibleGame(root)
    root.mainloop()