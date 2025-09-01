# utils.py

# --- Funções existentes (sem alterações) ---
def validar_prioridade(prioridade, prioridades):
    return prioridade in prioridades

def validar_categoria(categoria, categorias):
    return categoria in categorias

def validar_descricao(atividade, descricao, descricoes):
    return descricao in descricoes.get(atividade, [])

def tarefa_duplicada(tarefa, lista_tarefas):
    return tarefa in lista_tarefas

def formatar_texto(texto):
    return texto.strip().capitalize()

def mostrar_lista(lista):
    print("Opções válidas:")
    for item in lista:
        print(f"- {item}")

# --- NOVA FUNÇÃO ---
def selecionar_opcao(titulo, opcoes):
    """
    Mostra um menu numerado de opções e pede ao usuário para escolher uma.
    Valida a entrada e retorna a opção escolhida.
    """
    print(f"\n{titulo}")
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i} - {opcao}")
    
    while True:
        try:
            escolha = int(input("Digite o número da sua escolha: "))
            if 1 <= escolha <= len(opcoes):
                # Retorna o item da lista (índice é escolha - 1)
                return opcoes[escolha - 1]
            else:
                print("Erro: número fora do intervalo. Tente novamente.")
        except ValueError:
            print("Erro: por favor, digite apenas o número.")