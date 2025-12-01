import tkinter as tk
from tkinter import ttk, scrolledtext
from threading import Thread
import time

from EjercicioCriaturas.ArenaDeCombate import ArenaDeCombate
from EjercicioCriaturas.DragonSolar import DragonSolar
from EjercicioCriaturas.RobotOmega import RobotOmega


class BattleApp:
    def __init__(self, master):
        self.master = master
        master.title("Arena de Combate Épica (Django Creatures)")
        master.resizable(False, False)


        self.combat_running = False
        self.c1_stats = tk.StringVar()
        self.c2_stats = tk.StringVar()


        self.arena = None
        self.c1 = None
        self.c2 = None


        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=3)
        self.master.columnconfigure(2, weight=1)


        self.log_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=50, height=20, font=('Consolas', 10))
        self.log_area.grid(row=0, column=1, rowspan=3, padx=10, pady=10, sticky="nsew")
        self.log_area.insert(tk.END, ">>> Sistema de Combate Inicializando...\n")


        self.c1 = DragonSolar("Drago", "Solara", 50, log_func=self.log_message)
        self.c2 = RobotOmega("Omni", "Cibernia", 8, log_func=self.log_message)
        self.arena = ArenaDeCombate(log_func=self.log_message)
        self.arena.participantes = [self.c1, self.c2]


        self.panel1 = self._setup_stats_panel(self.c1, 0, self.c1_stats)
        self.panel2 = self._setup_stats_panel(self.c2, 2, self.c2_stats)


        self.btn_frame = ttk.Frame(master)
        self.btn_frame.grid(row=3, column=0, columnspan=3, pady=10)

        self.btn_start = ttk.Button(self.btn_frame, text="INICIAR COMBATE", command=self.start_combat_thread)
        self.btn_start.pack(side=tk.LEFT, padx=10)

        self.btn_recargar = ttk.Button(self.btn_frame, text="RECARGAR Y RESET", command=self.reset_and_recharge)
        self.btn_recargar.pack(side=tk.LEFT, padx=10)


        self.update_stats()
        self.log_message("Listo para la Batalla. Presione INICIAR COMBATE.")



    def log_message(self, message):
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)

    def _setup_stats_panel(self, criatura, col, stat_var):
        frame = ttk.LabelFrame(self.master, text=criatura.nombre, padding="10")
        frame.grid(row=0, column=col, padx=10, pady=10, sticky="n")

        ttk.Label(frame, textvariable=stat_var, font=('Arial', 10, 'bold')).pack(pady=5)

        criatura.bar = ttk.Progressbar(frame, orient='horizontal', length=150, mode='determinate')
        criatura.bar.pack(pady=5)


        ttk.Label(frame, text=criatura.hacer_sonido(), wraplength=140).pack(pady=5)

        return frame

    def update_stats(self):


        self.c1.bar['value'] = self.c1.energia
        self.c1_stats.set(f"Nivel: {self.c1.nivel} | Energía: {self.c1.energia}/100\nEstado: {self.c1.estado}")


        self.c2.bar['value'] = self.c2.energia
        self.c2_stats.set(f"Nivel: {self.c2.nivel} | Energía: {self.c2.energia}/100\nEstado: {self.c2.estado}")

        if self.combat_running:
            self.master.after(100, self.update_stats)

    def reset_and_recharge(self):

        self.combat_running = False
        self.c1.recargar_energia()
        self.c2.recargar_energia()
        self.btn_start['state'] = 'enabled'
        self.log_message("\n--- SISTEMA REINICIADO Y ENERGÍA RECARGADA ---\n")
        self.update_stats()



    def run_combat_simulation(self):
        time.sleep(1)
        self.combat_running = True

        c1, c2 = self.c1, self.c2

        self.log_message("\n--- INICIO DEL COMBATE AUTOMATIZADO ---")

        turno = 0
        while c1.estado != "KO" and c2.estado != "KO" and turno < 10 and self.combat_running:
            turno += 1
            self.log_message(f"\n--- TURNO {turno} ---")


            c1.atacar(c2)
            time.sleep(0.5)
            if c2.estado == "KO": break


            c2.atacar(c1)
            time.sleep(0.5)


        ganador = self.arena._determinar_ganador(c1, c2)

        self.log_message("\n--- 🏁 FIN DEL COMBATE 🏁 ---")
        if isinstance(ganador, type(c1)):
            self.log_message(f"🏆 GANADOR: {ganador.nombre} (¡ha evolucionado!)")
        else:
            self.log_message(f"Resultado: {ganador}")

        self.combat_running = False
        self.btn_start['state'] = 'enabled'

    def start_combat_thread(self):

        if self.combat_running:
            self.log_message("El combate ya está en curso.")
            return

        self.btn_start['state'] = 'disabled'
        combat_thread = Thread(target=self.run_combat_simulation)
        combat_thread.start()



if __name__ == "__main__":
    root = tk.Tk()
    app = BattleApp(root)
    root.mainloop()