def show_tasks(tasks):
    if not tasks:
        print("\nNenhuma tarefa encontrada.")
        return

    print("\n=== LISTA DE TAREFAS ===")

    for task in tasks:
        print(f"""
ID: {task[0]}
Título: {task[1]}
Descrição: {task[2]}
Prioridade: {task[3]}
Prazo: {task[4]}
Status: {task[5]}
-------------------------
""")