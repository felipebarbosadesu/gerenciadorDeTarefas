📅 Gerenciador de Tarefas Diárias
Um simples, porém eficaz, visualizador de tarefas diárias desenvolvido em Python para execução no terminal.
📝 Sobre o Projeto
Este projeto é um visualizador de tarefas diárias que não requer um banco de dados externo. Ele utiliza uma estrutura de dados interna para armazenar e organizar uma lista pré-definida de atividades, oferecendo uma visão clara da rotina, dividida por períodos do dia: Manhã, Tarde e Noite.

✨ Funcionalidades
Lista de Tarefas Pré-definida: O programa já vem com uma lista de tarefas comuns, que pode ser facilmente customizada no código-fonte.
Organização por Período: As tarefas são agrupadas por "Manhã", "Tarde" e "Noite".
Visualização Flexível: O usuário pode escolher visualizar as tarefas de um período específico ou todas.
Interface de Linha de Comando: A interação é feita através de um menu simples no terminal.
📄 Escopo Original do Projeto
Esta seção descreve a proposta inicial do projeto, que era mais abrangente. Durante o desenvolvimento, o foco foi ajustado para criar o visualizador de tarefas atual.

Proposta Inicial
Desenvolver um programa de linha de comando que permitisse aos usuários gerenciar (adicionar, listar, concluir) suas tarefas diárias. O projeto seria organizado em vários módulos e utilizaria funções, listas, tuplas, dicionários, conjuntos e um ambiente virtual.

🛠️ Como Executar
Clone ou baixe o arquivo meu_dia.py para o seu computador.
Navegue até a pasta do projeto pelo terminal.
cd caminho/para/a/pasta/do/projeto
Execute o arquivo principal:
python meu_dia.py
🚀 Como Customizar
Para adaptar o gerenciador à sua própria rotina, basta editar o dicionário tarefas_por_horario diretamente no arquivo meu_dia.py.

Exemplo de uma tarefa:

{
    "nome": "Lazer",
    "descricao": "Ler um livro ou assistir série",
    "prioridade": "Baixa",
    "categoria": "Lazer"
}
📜 Licença
Este projeto está sob a licença MIT.
