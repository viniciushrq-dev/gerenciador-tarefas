import tarefa

def exibir_menu():
    print("\n===== GERENCIADOR DE TAREFAS =====")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Editar tarefa")
    print("4. Concluir tarefa")
    print("5. Excluir tarefa")
    print("0. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título da tarefa: ")
            descricao = input("Descrição: ")
            tarefa.adicionar_tarefa(titulo, descricao)
            print("Tarefa adicionada com sucesso!")

        elif opcao == "2":
            tarefas = tarefa.listar_tarefas()
            if not tarefas:
                print("Nenhuma tarefa encontrada.")
            else:
                print("\nTAREFAS:")
                for t in tarefas:
                    print(f"{t[0]} - {t[1]} | {t[2]} | Status: {t[3]}")

        elif opcao == "3":
            id = input("ID da tarefa a editar: ")
            novo_titulo = input("Novo título: ")
            nova_descricao = input("Nova descrição: ")
            tarefa.atualizar_tarefa(id, novo_titulo, nova_descricao)
            print("Tarefa atualizada com sucesso!")

        elif opcao == "4":
            id = input("ID da tarefa a marcar como concluída: ")
            tarefa.concluir_tarefa(id)
            print("Tarefa concluída!")

        elif opcao == "5":
            id = input("ID da tarefa a excluir: ")
            tarefa.excluir_tarefa(id)
            print("Tarefa excluída!")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
