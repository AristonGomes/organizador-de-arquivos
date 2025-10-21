# Organizador de Arquivos em Python

Um script de linha de comando para organizar arquivos em subpastas com base em suas extensões.

## Funcionalidades

- Copia arquivos de um diretório de origem para um de destino.
- Agrupa arquivos por extensão (ex: `.pdf`, `.jpg`, `.zip`).
- Lida com arquivos sem extensão, agrupando-os em `sem_extensao`.
- Preserva metadados dos arquivos originais (data de criação/modificação).
- Gera um arquivo de log (`organization_log.log`) com todas as operações.
- Modo interativo (perguntando a origem/destino) e modo de automação (via argumentos).

## Como Usar

1. Clone o repositório.
2. (Opcional) Crie um ambiente virtual: `python -m venv venv`
3. Para rodar, use os argumentos de linha de comando:

```bash
python organizer.py --source "C:\Pasta\Origem" --destination "C:\Pasta\Destino"

Ou simplesmente execute o script para entrar no modo interativo:

```Bash

python organizer.py