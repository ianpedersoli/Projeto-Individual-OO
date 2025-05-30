import tkinter as tk
from tkinter import messagebox
from package.controllers.sistema_controller import SistemaController

class Interface:
    def __init__(self, master):
        self.master = master
        master.title("Sistema de Controle de Estudantes")
        self.controller = SistemaController()

        tk.Label(master, text="Nome:").grid(row=0, column=0, padx=5, pady=3)
        tk.Label(master, text="Idade:").grid(row=1, column=0, padx=5, pady=3)
        tk.Label(master, text="Matrícula:").grid(row=2, column=0, padx=5, pady=3)

        self.nome_entry = tk.Entry(master)
        self.idade_entry = tk.Entry(master)
        self.matricula_entry = tk.Entry(master)
        self.nome_entry.grid(row=0, column=1, padx=5, pady=3)
        self.idade_entry.grid(row=1, column=1, padx=5, pady=3)
        self.matricula_entry.grid(row=2, column=1, padx=5, pady=3)

        tk.Button(master, text="Adicionar Estudante", command=self.adicionar_estudante).grid(row=3, column=0, columnspan=2, pady=5)
        tk.Button(master, text="Remover Estudante", command=self.remover_estudante).grid(row=4, column=0, columnspan=2, pady=5)
        tk.Button(master, text="Listar Estudantes", command=self.listar_estudantes).grid(row=5, column=0, columnspan=2, pady=5)

        tk.Label(master, text="Nota:").grid(row=6, column=0, padx=5, pady=3)
        self.nota_entry = tk.Entry(master)
        self.nota_entry.grid(row=6, column=1, padx=5, pady=3)

        tk.Button(master, text="Adicionar Nota", command=self.adicionar_nota).grid(row=7, column=0, columnspan=2, pady=5)
        tk.Button(master, text="Média de Notas", command=self.media_estudante).grid(row=8, column=0, columnspan=2, pady=5)

        tk.Button(master, text="Limpar Banco de Dados", command=self.limpar_dados).grid(row=9, column=0, columnspan=2, pady=5)
        tk.Button(master, text="Sair", command=master.quit, bg="red", fg="white").grid(row=10, column=0, columnspan=2, pady=10)

        self.resultado = tk.Text(master, height=10, width=50)
        self.resultado.grid(row=11, column=0, columnspan=2, padx=5, pady=5)

    def limpar_campos(self):
        self.nome_entry.delete(0, tk.END)
        self.idade_entry.delete(0, tk.END)
        self.matricula_entry.delete(0, tk.END)
        self.nota_entry.delete(0, tk.END)

    def adicionar_estudante(self):
        nome = self.nome_entry.get().strip()
        idade = self.idade_entry.get().strip()
        matricula = self.matricula_entry.get().strip()
        try:
            if not nome or not idade or not matricula:
                raise ValueError("Todos os campos são obrigatórios.")
            self.controller.adicionar_estudante(nome, int(idade), matricula)
            messagebox.showinfo("Sucesso", "Estudante adicionado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))
        finally:
            self.limpar_campos()

    def remover_estudante(self):
        matricula = self.matricula_entry.get().strip()
        if not matricula:
            messagebox.showwarning("Atenção", "Informe a matrícula para remover.")
            return
        try:
            self.controller.remover_estudante(matricula)
            messagebox.showinfo("Sucesso", "Estudante removido com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", str(e))
        finally:
            self.limpar_campos()

    def listar_estudantes(self):
        exibicoes = self.controller.listar_estudantes()
        self.resultado.delete(1.0, tk.END)
        if not exibicoes:
            self.resultado.insert(tk.END, "Nenhum estudante cadastrado.\n")
        else:
            for est in exibicoes:
                self.resultado.insert(tk.END, f"{est}\n")

    def adicionar_nota(self):
        matricula = self.matricula_entry.get().strip()
        nota = self.nota_entry.get().strip()
        try:
            if not matricula or not nota:
                raise ValueError("Informe a matrícula e a nota.")
            self.controller.adicionar_nota_estudante(matricula, float(nota))
            messagebox.showinfo("Sucesso", "Nota adicionada com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", str(e))
        finally:
            self.limpar_campos()

    def media_estudante(self):
        matricula = self.matricula_entry.get().strip()
        try:
            media = self.controller.calcular_media_estudante(matricula)
            messagebox.showinfo("Média", f"Média do estudante: {media:.2f}")
        except Exception as e:
            messagebox.showerror("Erro", str(e))
        finally:
            self.limpar_campos()

    def limpar_dados(self):
        if messagebox.askyesno("Confirmar", "Deseja apagar todos os dados?"):
            self.controller.limpar_dados()
            self.resultado.delete(1.0, tk.END)
            messagebox.showinfo("Sucesso", "Todos os dados foram apagados.")
            self.limpar_campos()