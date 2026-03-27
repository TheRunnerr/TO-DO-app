from database import create_table
from tasks import add_task, list_tasks, complete_task, delete_task
from utils import show_tasks

def menu():
    print("""
==== TO-DO APP ====
1. Adicionar tarefa
2. Listar tarefas
3. Concluir tarefa
4. Deletar tarefa
5. Sair
""")

def main():
    create_table()

    while True:
        menu()
        option = input("Escolha uma opção: ")

        if option == "1":
            title = input("Título: ")
            description = input("Descrição: ")
            priority = input("Prioridade (baixa/média/alta): ")
            due_date = input("Prazo (YYYY-MM-DD): ")

            add_task(title, description, priority, due_date)
            print("Tarefa adicionada!")

        elif option == "2":
            tasks = list_tasks()
            show_tasks(tasks)

        elif option == "3":
            task_id = input("ID da tarefa: ")
            complete_task(task_id)
            print("Tarefa concluída!")

        elif option == "4":
            task_id = input("ID da tarefa: ")
            delete_task(task_id)
            print("Tarefa deletada!")

        elif option == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()