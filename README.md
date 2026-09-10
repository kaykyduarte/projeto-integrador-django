# Projeto Integrador — População dos Estados Brasileiros

Projeto acadêmico desenvolvido no segundo semestre da faculdade para praticar Python, banco de dados e desenvolvimento web. A aplicação apresenta um gráfico interativo com a população das unidades da federação brasileiras em 2025, usando os dados do IBGE presentes no arquivo CSV do projeto.

## Objetivo

Integrar a leitura e o tratamento de dados com pandas, o armazenamento no SQLite usando comandos SQL e a exibição de um gráfico em uma página Django.

O gráfico mostra as unidades da federação em ordem decrescente de população. Ao passar o mouse sobre uma barra, é possível consultar a UF e sua população.

## Tecnologias

- **Python:** linguagem utilizada no projeto.
- **Django:** criação da aplicação web e acesso ao banco de dados.
- **pandas:** leitura do CSV e organização dos dados.
- **SQLite e SQL:** armazenamento, inserção e consulta dos registros.
- **Bokeh:** criação do gráfico interativo.
- **HTML:** página que apresenta o gráfico.
- **Jupyter Notebook:** análise dos dados no arquivo `analise_dados.ipynb`.

As versões das bibliotecas necessárias para executar a aplicação estão em `requirements.txt`. O SQLite já faz parte da biblioteca padrão do Python.

## Estrutura

```text
Projeto_Integrador_Django/
├── dados/
│   └── IBGE_populacaobrasil_2025.csv   # Dados de população
├── graficos/                         # Aplicação responsável pelo gráfico
│   ├── templates/graficos/
│   │   └── exibir_grafico.html        # Página HTML
│   ├── urls.py                       # Rota da página
│   └── views.py                      # Consulta SQL e criação do gráfico
├── meu_projeto/                      # Configurações e rotas do Django
├── sql/
│   └── criar_tabela.sql              # Comando de criação da tabela
├── analise_dados.ipynb               # Notebook de análise
├── carregar_dados.py                 # Tratamento do CSV e inserção no banco
├── manage.py                        # Comandos do Django
├── requirements.txt                 # Dependências da aplicação
└── README.md
```

O arquivo `db.sqlite3` é criado durante a preparação do banco e não é versionado no Git.

## Como executar

Os comandos abaixo são para o **PowerShell no Windows**, usando Python 3.13, utilizado no desenvolvimento. Execute-os dentro da pasta `Projeto_Integrador_Django`, onde está o arquivo `manage.py`.

### 1. Criar o ambiente virtual e instalar as dependências

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Se a `.venv` do projeto já existir, basta ativá-la e instalar as dependências. Use esse mesmo ambiente para instalar as bibliotecas e iniciar o Django.

### 2. Preparar o banco de dados

Crie as tabelas padrão do Django:

```powershell
python manage.py migrate
```

A tabela `populacao_estados` é criada separadamente pelo arquivo SQL. Execute o comando abaixo uma única vez em um banco novo:

```powershell
python -c "import sqlite3; c = sqlite3.connect('db.sqlite3'); c.executescript(open('sql/criar_tabela.sql', encoding='utf-8').read()); c.commit(); c.close()"
```

### 3. Carregar os dados

```powershell
python carregar_dados.py
```

O script lê o CSV, remove os pontos usados como separadores de milhares na população e insere os registros com `INSERT` e `executemany()`.

Faça essa carga apenas uma vez para os mesmos dados. A tabela não permite repetir a combinação de UF e ano, então executar novamente causará erro de duplicidade. Se o banco já estiver preparado e preenchido, pule as etapas 2 e 3.

### 4. Iniciar o servidor

```powershell
python manage.py runserver
```

Abra no navegador: **http://127.0.0.1:8000/exibir_grafico/**

A página carrega os recursos do Bokeh pela internet, portanto é necessário ter conexão para visualizar o gráfico. Para parar o servidor, pressione `Ctrl + C` no terminal.

Se o terminal estiver usando o Python de outro ambiente, inicie explicitamente com o Python do projeto:

```powershell
.\.venv\Scripts\python.exe manage.py runserver
```

O notebook é um material de análise separado e não precisa ser executado para abrir a aplicação.
