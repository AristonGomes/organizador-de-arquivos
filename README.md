# Organizador de Arquivos em Python

Utilitário de linha de comando (CLI) em **Python** para automação da organização de diretórios, classificando arquivos em subpastas de acordo com suas extensões, com preservação de metadados e registro de auditoria em log.

---

## Funcionalidades

- **Classificação Automatizada por Extensão:** agrupa arquivos em subpastas correspondentes ao seu formato (ex.: `.pdf`, `.jpg`, `.xlsx`, `.zip`).
- **Tratamento de Exceções:** arquivos sem extensão definida são isolados automaticamente no diretório `sem_extensao`.
- **Preservação de Metadados:** utiliza cópia com manutenção de atributos originais (datas de criação e modificação).
- **Auditoria de Operações:** registra todas as movimentações e eventuais erros no arquivo `organization_log.log`.
- **Execução Flexível:** suporta tanto uso interativo via terminal quanto execução automatizada via argumentos de linha de comando (CLI).

---

## Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/AristonGomes/organizador-de-arquivos.git
cd organizador-de-arquivos
```

### 2. Modo Automatizado (via argumentos CLI)

Ideal para integração em rotinas agendadas ou scripts de automação:

```bash
python organizer.py --source "C:\Pasta\Origem" --destination "C:\Pasta\Destino"
```

### 3. Modo Interativo

Execute o script sem argumentos para informar os diretórios de origem e destino diretamente no prompt:

```bash
python organizer.py
```

---

## Estrutura do Projeto

```text
organizador-de-arquivos/
├── organizer.py    # Script principal de varredura, cópia e logging
├── .gitignore      # Configuração de arquivos ignorados pelo Git
└── README.md       # Documentação do projeto
```

---

## Autor e Licença

- **Autor:** [Ariston Gomes](https://www.linkedin.com/in/ariston-gomes/)
- **Licença:** Distribuído sob a licença MIT.
