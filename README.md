# Sistema CRUD de Cadastro de Clientes

## 📝 Descrição
Sistema de cadastro com interface gráfica para gerenciar clientes (Nome, Sobrenome, Email, CPF).

## ⚙️ Funcionalidades
- ✅ Inserir novos clientes
- ✅ Visualizar todos os clientes cadastrados
- ✅ Buscar clientes por nome, sobrenome, email ou CPF
- ✅ Atualizar dados de clientes existentes
- ✅ Deletar clientes do banco de dados

## 🛠️ Tecnologias utilizadas
- Python 3.11+
- Tkinter (Interface Gráfica)
- SQLite3 (Banco de Dados)

## 🚀 Como executar

### Pré-requisitos
- Python 3.11 ou superior instalado
- Git (opcional, para clonar)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/crud-python-sqlite.git
cd crud-python-sqlite
```

2. Crie e ative o ambiente virtual:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Execute o programa:
```bash
python aplicacao.py
```

## 📁 Estrutura do projeto
```
CrudPySqlProject/
├── main.py          # Interface gráfica (Tkinter)
├── Backend.py       # Lógica do banco de dados SQLite
├── aplicacao.py     # Arquivo principal - Execute este!
├── clientes.db      # Banco de dados (gerado automaticamente)
├── README.md        # Este arquivo
├── .gitignore       # Arquivos ignorados pelo Git
└── requirements.txt # Dependências do projeto
```

## 📸 Screenshot
(Imagem 1)
(Imagem 2)
(Imagem 3)

## 🤝 Como contribuir
1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📄 Licença
Este projeto está sob a licença MIT.

## ✒️ Autor
**Carlos Henrique**
- GitHub: https://github.com/CarlosHCS001
- LinkedIn: https://www.linkedin.com/in/carlos-henrique-concei%C3%A7%C3%A3o-soares-5692281b4/l)
```

```
# Ambiente virtual
venv/
.venv/
env/
ENV/

# Banco de dados
*.db
*.sqlite
*.sqlite3

# Python cache
__pycache__/
*.py[cod]
*$py.class
*.so

# IDEs
.idea/
.vscode/
*.swp
*.swo
*~

# Sistema operacional
.DS_Store
Thumbs.db

# Logs
*.log

# Distribuição
dist/
build/
*.egg-info/