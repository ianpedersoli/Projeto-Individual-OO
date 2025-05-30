import pickle
import os
from package.models.estudante import Estudante

class SistemaController:
    def __init__(self):
        self.caminho_banco = "estudantes.db"
        self.estudantes = self._carregar_dados()

    def _salvar_dados(self):
        with open(self.caminho_banco, "wb") as f:
            pickle.dump(self.estudantes, f)

    def _carregar_dados(self):
        if os.path.exists(self.caminho_banco):
            with open(self.caminho_banco, "rb") as f:
                return pickle.load(f)
        return []

    def adicionar_estudante(self, nome: str, idade: int, matricula: str):
        for est in self.estudantes:
            if est.matricula == matricula:
                raise ValueError("Matrícula já cadastrada.")
            if est.nome.lower() == nome.lower():
                raise ValueError("Nome já cadastrado.")
        novo_est = Estudante(nome, idade, matricula)
        self.estudantes.append(novo_est)
        self._salvar_dados()

    def remover_estudante(self, matricula: str):
        estudante = self._buscar_estudante_por_matricula(matricula)
        if estudante:
            self.estudantes.remove(estudante)
            self._salvar_dados()
        else:
            raise ValueError("Estudante não encontrado para remoção.")

    def listar_estudantes(self):
        return [est.exibir_dados() for est in self.estudantes]

    def adicionar_nota_estudante(self, matricula: str, nota: float):
        estudante = self._buscar_estudante_por_matricula(matricula)
        if estudante is None:
            raise ValueError("Estudante não encontrado para adicionar nota.")
        estudante.adicionar_nota(nota)
        self._salvar_dados()

    def calcular_media_estudante(self, matricula: str) -> float:
        estudante = self._buscar_estudante_por_matricula(matricula)
        if estudante is None:
            raise ValueError("Estudante não encontrado para calcular média.")
        return estudante.media_notas()

    def limpar_dados(self):
        self.estudantes.clear()
        if os.path.exists(self.caminho_banco):
            os.remove(self.caminho_banco)

    def _buscar_estudante_por_matricula(self, matricula: str):
        for est in self.estudantes:
            if est.matricula == matricula:
                return est
        return None