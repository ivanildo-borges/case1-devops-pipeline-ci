# case2-DevSecOps-pipeline-CI

API REST simples desenvolvida com Python e Flask para o projeto FastOrder. O
repositório também demonstra uma esteira de Integração Contínua (CI), com
dependências de desenvolvimento para validação e testes.

## Estrutura do projeto

```text
.
├── .dockerignore           # Arquivos não enviados para o contexto Docker
├── .gitignore
├── app/
│   ├── __init__.py       # Fábrica da aplicação Flask
│   └── routes.py         # Rotas e endpoints da API
├── tests/
│   └── test_app.py        # Testes das rotas da aplicação
├── main.py                # Ponto de entrada para executar a API
├── Dockerfile             # Configuração para criar a imagem da aplicação
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

- Python 3.11 ou superior
- `pip`
- Docker Desktop em execução
- Git
- Trivy instalado ou acesso ao Docker para executá-lo como contêiner

### Por que usar Trivy e Bandit?

As ferramentas atuam em camadas diferentes e se complementam na proteção do
projeto:

- **Trivy** analisa a imagem Docker, identificando vulnerabilidades no sistema
  operacional e nas bibliotecas instaladas. O resultado impede a publicação de
  imagens com vulnerabilidades críticas, altas ou médias.
- **Bandit** realiza análise estática do código Python (SAST), identificando
  padrões que podem causar problemas de segurança antes da execução da
  aplicação.

No projeto, o Bandit é executado no job de análise de segurança e o Trivy é
executado após o build da imagem no job de container. Assim, vulnerabilidades
no código e na imagem são detectadas durante o desenvolvimento e na integração
contínua, antes do deploy.

### 2. Criar e ativar o ambiente virtual

No Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

No Windows Prompt Command (CMD):
```bash
python -m venv venv
.\venv\Scripts\activate
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

Para executar testes e análises de segurança localmente, instale também as
dependências de desenvolvimento:

```bash
pip install -r requirements-dev.txt
```

### 4. Executar a API

```bash
python main.py
```

A API ficará disponível em `http://localhost:5000`.

### Executar com Docker localmente

Com o Docker instalado e em execução, crie a imagem:

```bash
docker build -t fastorder-api:latest .
```

Depois, inicie o contêiner em segundo plano:

```bash
docker run -d -p 5000:5000 --name fastorder-container fastorder-api:latest
```

A API ficará disponível em `http://localhost:5000`.

Para acompanhar os logs ou parar o contêiner:

```bash
docker logs -f fastorder-container
docker stop fastorder-container
```

> **Atenção:** em plataformas modernas de nuvem com planos gratuitos, como
> Render, Koyeb e Railway, normalmente basta disponibilizar o `Dockerfile` no
> repositório e configurar o serviço para usar essa aplicação. A própria
> plataforma realiza o processo de build da imagem e de execução do contêiner
> nos servidores dela. Nesse cenário, não é necessário executar manualmente
> os comandos `docker build` e `docker run`.

### 5. Escaneamento de segurança

#### Trivy: análise da imagem Docker

Depois de criar ou atualizar a imagem, execute o escaneamento com o Trivy:

```bash
trivy image fastorder-api:latest
```

Se o Trivy não estiver instalado no sistema, execute-o pelo Docker Desktop:

```bash
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest image --scanners vuln --severity CRITICAL,HIGH,MEDIUM --ignore-unfixed=false fastorder-api:latest
```

O comando deve retornar zero vulnerabilidades críticas, altas ou médias. O
pipeline aplica o mesmo critério e falha quando encontra uma vulnerabilidade
nessas severidades.

#### Bandit: análise estática do código Python

Com as dependências de desenvolvimento instaladas, execute:

```bash
bandit -r app main.py -ll -ii
```

O comando analisa o código da aplicação sem executá-lo. As opções `-ll` e
`-ii` incluem problemas de severidade e confiança médias ou altas, permitindo
que o mesmo tipo de alerta verificado pela esteira seja reproduzido localmente.

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
