import os

os.system("cls || clear")

from models.enums.sexo import sexo
from models.enums.setor import setor
from models.enums.funcionario import funcionario

funcionario1 = funcionario(21222, "Robson", 17, 8000, setor.RECURSOS_HUMANOS.value, sexo.MASCULINO.value)
print(funcionario1)



