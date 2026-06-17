# Sistema de Chamados de Suporte (CLI)

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

Ferramenta de linha de comando para registro e gerenciamento de chamados de suporte técnico (help desk de primeiro nível). Desenvolvida em Python puro, sem dependências externas.

## Sobre

O sistema simula o fluxo de uma equipe de suporte de primeiro nível: abertura, acompanhamento, atualização de status e encerramento de chamados, além de um relatório consolidado. Roda inteiramente no terminal e mantém os dados em memória durante a execução.

## Funcionalidades

- Abertura de chamado com título, descrição, solicitante e prioridade
- Geração automática de ID e data de abertura
- Listagem de todos os chamados
- Busca por ID
- Atualização de status (`aberto` → `em andamento` → `resolvido`)
- Filtro por status e por prioridade
- Encerramento de chamados
- Relatório com totais por status e por prioridade
- Validação das entradas do usuário

## Conceitos de Python aplicados

- Tipos, variáveis, operadores e f-strings
- Estruturas de controle (`if` / `elif` / `else`, operadores lógicos)
- Estruturas de dados: listas, tuplas e dicionários
- Laços (`for`, `while`) com `break` / `continue`
- Funções com parâmetros, retorno e valores padrão
- Importação de módulos da biblioteca padrão (`datetime`)

## Como executar

Pré-requisito: Python 3.10 ou superior.

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/sistema-chamados-cli.git

# Acesse a pasta
cd sistema-chamados-cli

# Execute
python main.py
```

Não há dependências externas — o projeto usa apenas a biblioteca padrão do Python.

## Exemplo de uso

```
=== Sistema de Chamados de Suporte ===
1 - Abrir chamado
2 - Listar chamados
3 - Buscar por ID
4 - Atualizar status
5 - Filtrar chamados
6 - Encerrar chamado
7 - Relatório
0 - Sair

Escolha uma opção: 1

Título: Impressora não imprime
Descrição: Setor financeiro, impressora HP sem resposta
Solicitante: Ana Souza
Prioridade (baixa/media/alta): alta

Chamado #001 aberto com sucesso em 17/06/2026.
```

## Estrutura do projeto

```
sistema-chamados-cli/
├── main.py        # Programa principal
└── README.md
```

## Próximas melhorias

- [ ] Persistência dos dados em arquivo JSON
- [ ] Tratamento de exceções (`try` / `except`) na validação de entradas
- [ ] Ordenação dos chamados por prioridade e data no relatório
- [ ] Cálculo do tempo em aberto de cada chamado

## Autor

Vitor — [GitHub](https://github.com/seu-usuario) · [LinkedIn](https://linkedin.com/in/seu-perfil)
