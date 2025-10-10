# ESTÚDIO ELSA PILATES

![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-FF4B4B.svg?logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.11-3776AB.svg?logo=python)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57.svg?logo=sqlite)

**ESTÚDIO ELSA PILATES** é uma aplicação web completa e profissional para gestão integral de estúdios de Pilates, desenvolvida com Streamlit e SQLite.

## 🎯 Características Principais

- ✅ **Gestão Multi-Perfil**: Administrador, Instrutor e Aluno
- ✅ **Dashboard Interativo**: Estatísticas e métricas em tempo real
- ✅ **Gestão de Alunos**: Cadastro, edição e acompanhamento
- ✅ **Gestão de Aulas**: Calendário semanal e reservas
- ✅ **Controlo Financeiro**: Receitas, despesas e relatórios
- ✅ **Loja Online**: Venda de produtos e gestão de stock
- ✅ **Relatórios Avançados**: Gráficos e análises de desempenho

## 🚀 Tecnologias

- **Frontend**: Streamlit 1.31.0
- **Base de Dados**: SQLite 3
- **Visualização**: Plotly 5.18.0
- **ORM**: SQLAlchemy 2.0.25

## 📦 Instalação Local

Para executar a aplicação localmente:

1. Clone o repositório ou descompacte o ficheiro ZIP
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute a aplicação:
   ```bash
   streamlit run app.py
   ```
4. Aceda à aplicação no seu navegador em: `http://localhost:8501`

## 🌐 Deploy no Streamlit Cloud

Para fazer o deploy no Streamlit Cloud:

1. **Crie um repositório no GitHub** e faça o upload de todos os ficheiros deste projeto
2. **Aceda ao Streamlit Cloud** ([https://streamlit.io/cloud](https://streamlit.io/cloud))
3. **Conecte o seu repositório GitHub** ao Streamlit Cloud
4. **Configure o deploy**:
   - Main file path: `app.py`
   - Python version: 3.11
5. **Clique em "Deploy"** e aguarde a conclusão

A aplicação ficará disponível num URL público fornecido pelo Streamlit Cloud.

## 🔑 Credenciais de Teste

| Perfil | Utilizador | Palavra-passe |
|--------|-----------|---------------|
| Administrador | `admin` | `password` |
| Instrutor | `instructor` | `password` |
| Aluno | `student` | `password` |

## 📚 Estrutura do Projeto

```
estudio_elsa_pilates_streamlit/
├── app.py                          # Aplicação principal e página de login
├── requirements.txt                # Dependências Python
├── .gitignore                      # Ficheiros a ignorar no Git
├── README.md                       # Este ficheiro
├── .streamlit/
│   └── config.toml                 # Configuração do Streamlit
├── database/
│   └── models.py                   # Modelos de dados SQLAlchemy
├── pages/
│   ├── 1_👥_Gestão_de_Alunos.py   # Página de gestão de alunos
│   ├── 2_📅_Gestão_de_Aulas.py    # Página de gestão de aulas
│   ├── 3_💰_Gestão_Financeira.py  # Página de gestão financeira
│   ├── 4_🛒_Gestão_de_Produtos.py # Página de gestão de produtos
│   ├── 5_📈_Relatórios.py         # Página de relatórios
│   ├── 7_🛒_Loja.py               # Loja para alunos
│   ├── 8_💳_Pagamentos.py         # Pagamentos para alunos
│   └── 9_👤_Meu_Perfil.py         # Perfil do aluno
└── estudio_elsa_pilates.db        # Base de dados SQLite (criada automaticamente)
```

## 📝 Funcionalidades por Perfil

### Administrador
- Visão geral do estúdio com métricas em tempo real
- Gestão completa de alunos
- Gestão de aulas e horários
- Controlo financeiro detalhado
- Gestão de produtos e stock
- Relatórios avançados com gráficos

### Instrutor
- Visualização do horário de aulas
- Gestão de alunos inscritos
- Marcação de presenças

### Aluno
- Visualização de aulas reservadas
- Loja online para compra de produtos
- Gestão de pagamentos e planos
- Perfil pessoal e estatísticas

## 🔒 Segurança

**Nota Importante**: Esta é uma versão de demonstração. Para uso em produção, implemente:
- Hash de palavras-passe (bcrypt, argon2)
- Autenticação robusta com JWT ou OAuth
- Validação de inputs
- Proteção contra SQL Injection (já implementada via SQLAlchemy)
- HTTPS obrigatório
- Gestão de sessões segura

## 📄 Licença

Todos os direitos reservados © 2025

## 👨‍💻 Desenvolvido por

**Manus AI** - Outubro de 2025

