import tkinter as tk
import subprocess
import os


class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600")
        self.root.title("RPA AQUAMAN Emissor de Faturas de Contas Agrupadas")
        self.root.option_add("*Font", "Helvetica 12 bold")
        self.root.configure(bg="#303030")

        # Cores e estilos
        button_color = "#606060"
        button_hover_color = "#808080"
        button_active_color = "#A0A0A0"
        label_color = "#D0D0D0"
        label_font = ("Helvetica", 12, "bold")

        self.scripts = [
            {
                'path': fr'C:\Users\mlm15\Documents\Python\RPA_AQUAMAN_Emissor_de_Faturas_de_Contas_Agrupadas\scripts\script_rpa_municipal.py',
                'status': tk.StringVar(value="Aguardando")},
            {
                'path': fr'',
                'status': tk.StringVar(value="Aguardando")},
            {
                'path': fr'',
                'status': tk.StringVar(value="Aguardando")},
            {
                'path': fr'',
                'status': tk.StringVar(value="Aguardando")},
            {
                'path': fr'',
                'status': tk.StringVar(value="Aguardando")}
        ]

        self.buttons = []

        for i, script in enumerate(self.scripts, start=1):
            label = tk.Label(self.root, text=os.path.basename(script['path']), bg="#303030", fg=label_color,
                             font=label_font)
            label.grid(row=i, column=0, sticky='w', padx=10, pady=5)

            button = tk.Button(self.root, textvariable=script['status'], state='disabled', bg=button_color,
                               relief="flat", fg="#FFFFFF")
            button.grid(row=i, column=1, padx=10, pady=5)
            self.buttons.append(button)
            button.bind("<Enter>", lambda e, b=button: b.configure(bg=button_hover_color))
            button.bind("<Leave>", lambda e, b=button: b.configure(bg=button_color))
            button.bind("<Button-1>", lambda e, b=button: b.configure(bg=button_active_color))

        execute_button = tk.Button(self.root, text="Executar scripts", command=self.run_scripts, bg=button_color,
                                   relief="flat", fg="#FFFFFF")
        execute_button.grid(row=i + 1, column=0, columnspan=4, padx=10, pady=10)
        label_sobre = tk.Label(self.root, text="""

        Para executar o robô acesse SIFAR -> Transferência -> 3 -> 2
        
        Front-End Desenvolvido por Michel G. Chaves de Moura

        Back-End Desenvolvido por Matheus L. Marchetti

        Versão 1.0.0 - Janeiro de 2024

        """, bg="#303030", fg=label_color, font=label_font)
        label_sobre.grid(row=i + 2, column=0, columnspan=4, padx=10, pady=10)

    def run_scripts(self):
        for script, button in zip(self.scripts, self.buttons):
            script['status'].set("Executando...")
            button.configure(bg="#7BD3EA", fg="#ffffff")  # Cor para 'Executando'
            self.root.update()
            process = subprocess.Popen(f'python "{script["path"]}"', shell=True)
            process.wait()
            if process.returncode == 0:
                script['status'].set("Finalizado")
                button.configure(bg="#A1EEBD", fg="#343339")
            else:
                script['status'].set("Erro")
            button.configure(bg="#F6F7C4", fg="#343339")  # Cor para 'Esperando' ou 'Erro'


root = tk.Tk()
app = App(root)
root.mainloop()