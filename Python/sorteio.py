# random.choice: Escolhe um item aleatorio de uma lista.
import random

aluno1 = input("Digite o Nome do 1° Aluno: ")
aluno2 = input("Digite o Nome do 2° Aluno: ")
aluno3 = input("Digite o Nome do 3° Aluno: ")
aluno4 = input("Digite o Nome do 4° Aluno: ")

escolhido = random.choice([aluno1, aluno2, aluno3, aluno4])
print(f"O Aluno escolhido para apagar o quadro foi {escolhido}")
