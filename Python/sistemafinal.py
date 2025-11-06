import json
import os

# ========== Funções utilitárias ==========


def salvar_json(nome_arquivo, dados):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def carregar_json(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        return []
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        return json.load(f)


def validar_codigo_existente(lista, codigo):
    return any(registro["codigo"] == codigo for registro in lista)

# ========== Operações CRUD ==========


def incluir_registro(nome, campos, arquivo):
    registros = carregar_json(arquivo)
    try:
        novo = {}
        for campo in campos:
            if "codigo" in campo:
                novo[campo] = int(input(f"Digite {campo}: "))
            else:
                novo[campo] = input(f"Digite {campo}: ")

        if validar_codigo_existente(registros, novo["codigo"]):
            print(f"{nome} com esse código já existe.\n")
            return

        registros.append(novo)
        salvar_json(arquivo, registros)
        print(f"{nome} incluído com sucesso!\n")
    except Exception as e:
        print(f"Erro ao incluir {nome}: {e}")


def listar_registros(nome, arquivo):
    registros = carregar_json(arquivo)
    if not registros:
        print(f"Nenhum {nome} cadastrado.\n")
    else:
        print(f"Lista de {nome}s:")
        for r in registros:
            print(" - " + ", ".join([f"{k}: {v}" for k, v in r.items()]))
        print()


def editar_registro(nome, campos, arquivo):
    registros = carregar_json(arquivo)
    try:
        codigo = int(input(f"Digite o código do {nome} a ser editado: "))
        for r in registros:
            if r["codigo"] == codigo:
                for campo in campos:
                    if "codigo" in campo:
                        r[campo] = int(input(f"Novo {campo}: "))
                    else:
                        r[campo] = input(f"Novo {campo}: ")
                salvar_json(arquivo, registros)
                print(f"{nome} atualizado com sucesso!\n")
                return
        print(f"{nome} não encontrado.\n")
    except Exception as e:
        print(f"Erro ao editar {nome}: {e}")


def excluir_registro(nome, arquivo):
    registros = carregar_json(arquivo)
    try:
        codigo = int(input(f"Digite o código do {nome} a ser excluído: "))
        for r in registros:
            if r["codigo"] == codigo:
                registros.remove(r)
                salvar_json(arquivo, registros)
                print(f"{nome} excluído com sucesso!\n")
                return
        print(f"{nome} não encontrado.\n")
    except Exception as e:
        print(f"Erro ao excluir {nome}: {e}")

# ========== Menus ==========


def menu_modulo(nome, campos, arquivo):
    while True:
        print(f"\n--- Menu de {nome.capitalize()} ---")
        print(f"1. Incluir {nome}")
        print(f"2. Listar {nome}s")
        print(f"3. Editar {nome}")
        print(f"4. Excluir {nome}")
        print("0. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            incluir_registro(nome, campos, arquivo)
        elif opcao == "2":
            listar_registros(nome, arquivo)
        elif opcao == "3":
            editar_registro(nome, campos, arquivo)
        elif opcao == "4":
            excluir_registro(nome, arquivo)
        elif opcao == "0":
            break
        else:
            print("Opção inválida!\n")


def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Estudantes")
        print("2. Professores")
        print("3. Disciplinas")
        print("4. Turmas")
        print("5. Matrículas")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_modulo(
                "estudante", ["codigo", "nome", "cpf"], "estudantes.json")
        elif opcao == "2":
            menu_modulo(
                "professor", ["codigo", "nome", "cpf"], "professores.json")
        elif opcao == "3":
            menu_modulo("disciplina", ["codigo", "nome"], "disciplinas.json")
        elif opcao == "4":
            menu_modulo("turma", ["codigo", "codigo_professor",
                        "codigo_disciplina"], "turmas.json")
        elif opcao == "5":
            menu_modulo(
                "matrícula", ["codigo", "codigo_turma", "codigo_estudante"], "matriculas.json")
        elif opcao == "0":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.\n")


# Iniciar
menu_principal()
