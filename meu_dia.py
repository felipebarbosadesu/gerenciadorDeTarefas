# meu_dia.py

# ============================================
# TAREFAS ORGANIZADAS POR PERÍODO DO DIA
# ============================================
tarefas_por_horario = {
    "Manhã": [
        {
            "nome": "Comer",
            "descricao": "Café da manhã",
            "prioridade": "Alta",
            "categoria": "Necessidades"
        },
        {
            "nome": "Passear com o Cachorro",
            "descricao": "Passeio matinal",
            "prioridade": "Média",
            "categoria": "Bem-estar"
        },
        {
            "nome": "Trabalhar",
            "descricao": "Bloco de trabalho 1",
            "prioridade": "Altíssima",
            "categoria": "Obrigações"
        },
    ],
    "Tarde": [
        {
            "nome": "Comer",
            "descricao": "Almoço",
            "prioridade": "Alta",
            "categoria": "Necessidades"
        },
        {
            "nome": "Estudar",
            "descricao": "Curso de Python",
            "prioridade": "Média",
            "categoria": "Obrigações"
        },
        {
            "nome": "Exercicio Fisico",
            "descricao": "Academia",
            "prioridade": "Média",
            "categoria": "Bem-estar"
        },
    ],
    "Noite": [
        {
            "nome": "Comer",
            "descricao": "Jantar",
            "prioridade": "Alta",
            "categoria": "Necessidades"
        },
        {
            "nome": "Terapia",
            "descricao": "Sessão semanal",
            "prioridade": "Alta",
            "categoria": "Bem-estar"
        },
        {
            "nome": "Lazer",
            "descricao": "Ler um livro ou assistir série",
            "prioridade": "Baixa",
            "categoria": "Lazer"
        }
    ]
}

# ============================================
# FUNÇÃO PARA LISTAR AS TAREFAS DE FORMA ORGANIZADA
# ============================================
def listar_tarefas(horario_especifico=None):
    print("\n" + "="*35)
    
    # Se o usuário pediu um horário específico, mostre apenas ele
    if horario_especifico in tarefas_por_horario:
        print(f"--- TAREFAS DA {horario_especifico.upper()} ---")
        for i, tarefa in enumerate(tarefas_por_horario[horario_especifico], start=1):
            print(f"{i}. {tarefa['nome']} ({tarefa['descricao']})")
            print(f"   Prioridade: {tarefa['prioridade']} | Categoria: {tarefa['categoria']}")
    
    # Se não, mostre todos os horários
    else:
        for horario, tarefas in tarefas_por_horario.items():
            print(f"\n--- TAREFAS DA {horario.upper()} ---")
            if not tarefas:
                print("Nenhuma tarefa para este período.")
                continue
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa['nome']} ({tarefa['descricao']})")
                print(f"   Prioridade: {tarefa['prioridade']} | Categoria: {tarefa['categoria']}")

    print("="*35)


# ============================================
# MENU PRINCIPAL COM OPÇÕES DE FILTRO
# ============================================
def menu():
    while True:
        print("\n=== VISUALIZADOR DE TAREFAS DIÁRIAS ===")
        print("1 - Listar Tarefas da Manhã")
        print("2 - Listar Tarefas da Tarde")
        print("3 - Listar Tarefas da Noite")
        print("4 - Listar Todas as Tarefas do Dia")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_tarefas("Manhã")
        
        elif opcao == "2":
            listar_tarefas("Tarde")

        elif opcao == "3":
            listar_tarefas("Noite")
        
        elif opcao == "4":
            listar_tarefas() # Chama a função sem argumento para mostrar tudo

        elif opcao == "5":
            print("Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

# ============================================
# EXECUÇÃO DO PROGRAMA
# ============================================
if __name__ == "__main__":
    menu()