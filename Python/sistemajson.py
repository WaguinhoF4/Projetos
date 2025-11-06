import json
import os

ARQUIVO = "estudantes.json"


def salvar_estudantes_json(lista):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)


def carregar_estudantes_json():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def incluir_estudante():
    estudantes = carregar_estudantes_json()

    codigo = int(input("Digite o código do estudante: "))
    nome = input("Digite o nome do estudante: ")
    cpf = input("Digite o CPF do estudante: ")

    estudante = {"codigo": codigo, "nome": nome, "cpf": cpf}
    estudantes.append(estudante)
    salvar_estudantes_json(estudantes)

    print("Estudante incluído com sucesso!\n")


def listar_estudantes():
    estudantes = carregar_estudantes_json()

    if not estudantes:
        print("Nenhum estudante cadastrado.\n")
    else:
        print("Lista de Estudantes:")
        for est in estudantes:
            print(
                f"Código: {est['codigo']}, Nome: {est['nome']}, CPF: {est['cpf']}")
        print()


def excluir_estudante():
    estudantes = carregar_estudantes_json()

    codigo = int(input("Digite o código do estudante a ser excluído: "))
    for est in estudantes:
        if est["codigo"] == codigo:
            estudantes.remove(est)
            salvar_estudantes_json(estudantes)
            print("Estudante removido com sucesso!\n")
            return
    print("Estudante não encontrado.\n")


def editar_estudante():
    estudantes = carregar_estudantes_json()

    codigo = int(input("Digite o código do estudante a ser editado: "))
    for est in estudantes:
        if est["codigo"] == codigo:
            est["codigo"] = int(input("Novo código: "))
            est["nome"] = input("Novo nome: ")
            est["cpf"] = input("Novo CPF: ")
            salvar_estudantes_json(estudantes)
            print("Estudante atualizado com sucesso!\n")
            return
    print("Estudante não encontrado.\n")


def menu():
    while True:
        print("===== MENU =====")
        print("1. Incluir Estudante")
        print("2. Listar Estudantes")
        print("3. Editar Estudante")
        print("4. Excluir Estudante")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            incluir_estudante()
        elif opcao == "2":
            listar_estudantes()
        elif opcao == "3":
            editar_estudante()
        elif opcao == "4":
            excluir_estudante()
        elif opcao == "0":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


# Iniciar o programa
menu()
