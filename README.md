# case1-devops-pipeline-ci

API REST simples desenvolvida com Python e Flask para o projeto FastOrder. O
repositório também demonstra uma esteira de Integração Contínua (CI), com
dependências de desenvolvimento para validação e testes.

## Estrutura do projeto

```text
.
├── .gitignore
├── app/
│   ├── __init__.py       # Fábrica da aplicação Flask
│   └── routes.py         # Rotas e endpoints da API
├── tests/
│   └── test_app.py        # Testes das rotas da aplicação
├── main.py                # Ponto de entrada para executar a API
├── pytest.ini             # Configuração de descoberta dos testes
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação do projeto
```

As responsabilidades da aplicação ficam dentro de `app/`. O arquivo
`main.py` permanece apenas como ponto de entrada, o que facilita adicionar
novas rotas e regras de negócio sem concentrar tudo em um único arquivo. Os
testes automatizados ficam em `tests/`, enquanto `pytest.ini` configura o
pytest para localizar o pacote `app` a partir da raiz do projeto.

## Como iniciar

### 1. Pré-requisitos

- Python 3.10 ou superior
- `pip`

### 2. Criar e ativar o ambiente virtual

No Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

No Linux ou macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a API

```bash
python main.py
```

A API ficará disponível em `http://localhost:5000`.

## Endpoints disponíveis

| Método | Rota | Descrição |
| --- | --- | --- |
| GET | `/` | Mensagem de boas-vindas |
| GET | `/api/status` | Retorna o status da aplicação |
| GET | `/api/soma?a=2&b=3` | Soma dois números e retorna `{"resultado": 5}` |

Exemplo:

```bash
curl "http://localhost:5000/api/soma?a=2&b=3"
```

## Verificações locais

Com o ambiente virtual ativado, execute:

```bash
pytest
flake8 .
```
