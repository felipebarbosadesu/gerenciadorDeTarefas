📅 Gerenciador de Tarefas Diárias
Um simples, porém eficaz, visualizador de tarefas diárias desenvolvido em Python para execução no terminal.

📝 Sobre o Projeto
Este projeto é um visualizador de tarefas diárias que não requer um banco de dados externo. Ele utiliza uma estrutura de dados interna para armazenar e organizar uma lista pré-definida de atividades, oferecendo uma visão clara da rotina, dividida por períodos do dia: Manhã, Tarde e Noite.

✨ Funcionalidades
Lista de Tarefas Pré-definida: O programa já vem com uma lista de tarefas comuns, que pode ser facilmente customizada no código-fonte.

Organização por Período: As tarefas são agrupadas por "Manhã", "Tarde" e "Noite", facilitando o acompanhamento da rotina.

Visualização Flexível: O usuário pode escolher visualizar as tarefas de um período específico ou todas as tarefas do dia de forma consolidada.

Interface de Linha de Comando: A interação é feita através de um menu simples e intuitivo no terminal.

📄 Escopo Original do Projeto
Esta seção descreve a proposta inicial do projeto, que era mais abrangente. Durante o desenvolvimento, o foco foi ajustado para criar o visualizador de tarefas atual, que é mais simples e direto.

Proposta Inicial
Desenvolver um programa de linha de comando que permite aos usuários gerenciar suas tarefas diárias, atribuindo-lhes prioridades e categorias. O projeto seria organizado em várias partes e usaria funções, listas, tuplas, dicionários, conjuntos e um ambiente virtual.

Passos do projeto:

Configuração do Ambiente Virtual: Criar um ambiente virtual usando o módulo venv.

Definição de Dados: Definir estruturas de dados para representar tarefas (dicionários com nome, descrição, prioridade e categoria).

Funções: Criar funções para adicionar, listar, marcar como concluídas e exibir tarefas por filtros.

Menu de Comandos: Criar um menu de linha de comando para interação com o usuário.

🛠️ Como Executar
Para rodar este projeto, você só precisa ter o Python instalado em sua máquina.

Clone ou baixe o arquivo meu_dia.py para o seu computador.

Navegue até a pasta do projeto pelo terminal.

cd caminho/para/a/pasta/do/projeto

Execute o arquivo principal:

python meu_dia.py

Após a execução, um menu interativo aparecerá. Basta digitar o número da opção desejada e pressionar Enter.

📂 Estrutura do Código
O projeto é contido em um único arquivo para simplicidade:

meu_dia.py: Contém toda a lógica da aplicação.

tarefas_por_horario: Um dicionário Python que armazena a lista de tarefas. É aqui que você pode customizar suas atividades.

listar_tarefas(): A função responsável por exibir as tarefas no terminal.

menu(): A função que gerencia a interação com o usuário.

🚀 Como Customizar
Para adaptar o gerenciador à sua própria rotina, basta editar o dicionário tarefas_por_horario diretamente no arquivo meu_dia.py. Você pode adicionar, remover ou modificar as tarefas em cada período.

Exemplo de uma tarefa:

{
    "nome": "Lazer",
    "descricao": "Ler um livro ou assistir série",
    "prioridade": "Baixa",
    "categoria": "Lazer"
}

📜 Licença
Este projeto está sob a licença MIT.
