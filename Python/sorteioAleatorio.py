# random.shuffler embaralha a ordem inteira.
import random

aluno1 = input("Digite o Nome do 1° Aluno: ")
aluno2 = input("Digite o Nome do 2° Aluno: ")
aluno3 = input("Digite o Nome do 3° Aluno: ")
aluno4 = input("Digite o Nome do 4° Aluno: ")

lista = ([aluno1, aluno2, aluno3, aluno4])
random.shuffle(lista)
print("A ordem de apresentação será: ")
print(lista)
