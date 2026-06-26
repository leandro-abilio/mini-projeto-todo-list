"""
Gerenciador de Tarefas (To-Do List) em terminal
Mini projeto de 3 aulas — Python puro

Este arquivo cresce ao longo das 3 aulas. Cada bloco abaixo está marcado
com a aula em que deve ser implementado:

    # ===== AULA 1 =====
    # ===== AULA 2 =====
    # ===== AULA 3 =====

Leia o arquivo AULA1.md (depois AULA2.md, depois AULA3.md) para saber
exatamente o que fazer em cada parte. Procure os comentários "# TODO"
-- é ali que vocês vão escrever código. Não apague as docstrings, elas
explicam o que cada função deve fazer.
"""

import csv
import os

# ===== AULA 3 =====
ARQUIVO_TAREFAS = "tarefas.csv"
CAMPOS_CSV = ["titulo", "concluida", "prioridade"]

# Lista que vai guardar todas as tarefas.
# Cada tarefa é um dicionário com as chaves: "titulo", "concluida", "prioridade"
tarefas = []


# =====================================================================
# ===== AULA 1 — Fundação do sistema =====
# =====================================================================

def adicionar_tarefa(titulo, prioridade="media"):
    tarefa = {'titulo':titulo,'concluida':False,'prioridade':prioridade}
    tarefas.append(tarefa)
    print(f"Tarefa [{titulo}] adicionada.")
    # TODO (Aula 3): depois de implementar salvar_tarefas(), chame-a aqui
    pass


def listar_tarefas():
    if len(tarefas) < 1:
        print("Lista vazia")
        return
    else:
        for index, tarefa in enumerate(tarefas, start=1):
            if tarefa['concluida'] == False:
                status = "[ ]"
            else:
                status = "[X]"
            print(f"{index} - {status} {tarefa['titulo']} (prioridade: {tarefa['prioridade']})")

# =====================================================================
# ===== AULA 2 — Lógica e manipulação de tarefas =====
# =====================================================================

def concluir_tarefa(indice):
    if indice < 1 or indice > len(tarefas):
        print("Numero de tarefa invalido.")
        return
    else:
        for index, tarefa in enumerate(tarefas, start=1):
            if index == indice:
                tarefa['concluida'] = True
                print(f"Tarefa [{tarefa['titulo']}] concluida.")
                break

    # TODO (Aula 3): depois de implementar salvar_tarefas(), chame-a aqui
    pass


def remover_tarefa(indice):
    if indice < 1 or indice > len(tarefas):
        print("Numero de tarefa invalido.")
        return
    else:
        for index, tarefa in enumerate(tarefas, start=1):
            if index == indice:
                tarefa_removida = tarefas.pop(indice - 1)
                print(f"Tarefa [{tarefa_removida['titulo']}] removida.")
                break
    
    # TODO (Aula 3): depois de implementar salvar_tarefas(), chame-a aqui
    pass


def editar_tarefa(indice, novo_titulo):
    if indice < 1 or indice > len(tarefas):
        print("Numero de tarefa invalido.")
        return
    else:
        for index, tarefa in enumerate(tarefas, start=1):
            if index == indice:
                tarefa['titulo'] = novo_titulo
                print(f"Tarefa [{novo_titulo}] atualizada.")
                break
    
    # TODO (Aula 3): depois de implementar salvar_tarefas(), chame-a aqui
    pass


# =====================================================================
# ===== AULA 3 — Persistência (CSV) e finalização =====
# =====================================================================

def salvar_tarefas():
    with open(ARQUIVO_TAREFAS, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS_CSV)
        escritor.writeheader()
        escritor.writerows(tarefas)
    pass


def carregar_tarefas():
    global tarefas
    tarefas = []  # Limpa a lista antes de carregar
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, mode="r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                linha["concluida"] = linha["concluida"] == "True"
                tarefas.append(linha)
    pass


def listar_pendentes():
    for index, tarefa in enumerate(tarefas, start=1):
        if not tarefa['concluida']:
            print(f"{index} - [ ] {tarefa['titulo']} (prioridade: {tarefa['prioridade']})")
            
    pass


# =====================================================================
# Menu e função principal
# =====================================================================

def exibir_menu():
    print("=== GERENCIADOR DE TAREFAS ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Editar tarefa")
    print("6. Listar pendentes")
    print("7. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            titulo = input("Titulo da tarefa: ")
            adicionar_tarefa(titulo)

        elif opcao == "2":
            listar_tarefas()

        elif opcao == "3":
            try:
                listar_tarefas()
                indice = int(input("Numero da tarefa a concluir: "))
                concluir_tarefa(indice)
            except ValueError:
                print("Entrada invalida. Por favor, insira um numero.")
        
        elif opcao == "4":
            try:
                listar_tarefas()
                indice = int(input("Numero da tarefa a remover: "))
                remover_tarefa(indice)
            except ValueError:
                print("Entrada invalida. Por favor, insira um numero.")

        elif opcao == "5":
            try:
                listar_tarefas()
                indice = int(input("Numero da tarefa a editar: "))
                novo_titulo = input("Novo titulo da tarefa: ")
                editar_tarefa(indice, novo_titulo)
            except ValueError:
                print("Entrada invalida. Por favor, insira um numero.")

        elif opcao == "6":
            listar_pendentes()

        elif opcao == "7":
            print("Saindo do programa...")
            break

        else:
            print("Opcao invalida, tente novamente.\n")


if __name__ == "__main__":
    main()
