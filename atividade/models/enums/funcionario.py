from models.enums.sexo import sexo
from models.enums.setor import setor

class funcionario:

    def __init__(self, id: str, nome: str, idade: int, salario: float, setor: setor, sexo: sexo) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.setor = setor
        self.sexo = sexo

        

    def __str__(self) -> str:
        return (
            f"\nID: {self.id}"
            f"\nNome: {self.nome}"
            f"\nIdade: {self.idade}"
            f"\nSalário: {self.salario}"
            f"\nSetor: {self.setor}"
            f"\nSexo: {self.sexo}"

        )