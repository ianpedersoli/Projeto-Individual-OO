from .pessoa import Pessoa

class Estudante(Pessoa):
    def __init__(self, nome: str, idade: int, matricula: str):
        if not matricula.isdigit() or len(matricula) != 9:
            raise ValueError("A matrícula deve conter exatamente 9 dígitos numéricos.")
        super().__init__(nome, idade)
        self._matricula = matricula
        self._notas = []

    def adicionar_nota(self, nota):
        self._notas.append(nota)

    def media_notas(self):
        if not self._notas:
            return 0
        return sum(self._notas) / len(self._notas)

    @property
    def matricula(self):
        return self._matricula

    @property
    def notas(self):
        return self._notas

    def exibir_dados(self):
        media = self.media_notas()
        return f"{super().exibir_dados()} - Matrícula: {self.matricula} - Média: {media:.2f}"