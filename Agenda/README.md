# Agenda Escolar

## Descrição
Aplicação de agenda escolar desenvolvida em Python com interface gráfica, permitindo gerenciar tarefas e compromissos acadêmicos.

## Funcionalidades
- ✅ Gerenciamento de tarefas
- ✅ Interface gráfica intuitiva
- ✅ Persistência em banco de dados
- ✅ Utilitários de datas e 

## Estrutura do Projeto
```
├── main.py                 # Ponto de entrada
├── Classes.py             # Definições de classes
├── DEFs.py               # Funções principais
├── requirements.txt       # Dependências
├── db/                   # Banco de dados
│   ├── database.py
│   └── migrations.sql
├── models/               # Modelos de dados
│   └── tarefa.py
├── ui/                   # Interface gráfica
│   ├── dialogs.py
│   ├── forms.py
│   └── main_window.py
├── utils/                # Utilitários
│   ├── dates.py
│   ├── export.py
│   └── helpers.py
└── tests/                # Testes
    └── tests_db.py
```

## Instalação
1. Clone o repositório
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute: `python main.py`

## Testes
```bash
pytest tests/
```
