# Documentação Técnica - ESTÚDIO ELSA PILATES (Streamlit)

## 1. Introdução

Este documento detalha a arquitetura técnica e as funcionalidades da aplicação "ESTÚDIO ELSA PILATES", desenvolvida com Streamlit e SQLite, com foco na facilidade de deploy via GitHub e Streamlit Cloud.

## 2. Arquitetura da Aplicação

A aplicação segue uma arquitetura monolítica simplificada, onde o frontend (interface de utilizador), a lógica de negócio e a interação com a base de dados são geridos dentro de um único ambiente Python/Streamlit.

### 2.1. Componentes Principais

-   **Streamlit**: Framework Python para construção rápida de aplicações web interativas. Atua como frontend e hospeda a lógica de negócio.
-   **SQLite**: Base de dados leve e baseada em ficheiros, ideal para portabilidade e deploy no Streamlit Cloud. Os dados são armazenados no ficheiro `estudio_elsa_pilates.db`.
-   **SQLAlchemy**: ORM (Object-Relational Mapper) Python para interagir com a base de dados SQLite, permitindo a manipulação de dados através de objetos Python.
-   **Pandas**: Biblioteca para manipulação e análise de dados, utilizada para exibir tabelas e processar dados para visualizações.
-   **Plotly**: Biblioteca para criação de gráficos interativos, utilizada nos relatórios e dashboards.

### 2.2. Estrutura de Diretórios

```
estudio_elsa_pilates_streamlit/
├── app.py                          # Aplicação principal e página de login
├── requirements.txt                # Dependências Python
├── README.md                       # Visão geral do projeto
├── .gitignore                      # Ficheiros a ignorar no Git
├── .streamlit/
│   └── config.toml                 # Configuração do Streamlit (tema, porta)
├── database/
│   └── models.py                   # Definição dos modelos de dados e funções de DB
├── pages/
│   ├── 1_👥_Gestão_de_Alunos.py   # Página de gestão de alunos (Admin)
│   ├── 2_📅_Gestão_de_Aulas.py    # Página de gestão de aulas (Admin)
│   ├── 3_💰_Gestão_Financeira.py  # Página de gestão financeira (Admin)
│   ├── 4_🛒_Gestão_de_Produtos.py # Página de gestão de produtos (Admin)
│   ├── 5_📈_Relatórios.py         # Página de relatórios (Admin)
│   ├── 7_🛒_Loja.py               # Loja para alunos
│   ├── 8_💳_Pagamentos.py         # Pagamentos para alunos
│   └── 9_👤_Meu_Perfil.py         # Perfil do aluno
└── estudio_elsa_pilates.db        # Ficheiro da base de dados SQLite
```

## 3. Modelos de Dados (database/models.py)

Os modelos de dados são definidos usando SQLAlchemy, mapeando objetos Python para tabelas na base de dados SQLite. A base de dados é inicializada e populada com dados de exemplo automaticamente na primeira execução.

### Entidades:

-   **User**: Armazena informações de login (username, password_hash, role, email, phone, first_name, last_name).
-   **Student**: Detalhes específicos do aluno (user_id, birth_date, anamnesis, is_active, enrollment_date, plan, credits).
-   **Instructor**: Detalhes específicos do instrutor (user_id, specialty, hire_date).
-   **Class**: Informações sobre as aulas (name, description, schedule_time, duration_minutes, max_capacity, instructor_id).
-   **ClassAttendance**: Registo de presenças dos alunos nas aulas (student_id, class_id, attended, attendance_date).
-   **Product**: Produtos vendidos no estúdio (name, description, category, price, stock, sold, is_active).
-   **Payment**: Registo de pagamentos (student_id, amount, payment_date, payment_method, status, payment_type, description).

### Funções de Base de Dados:

-   `init_db()`: Cria todas as tabelas na base de dados SQLite, se ainda não existirem.
-   `get_db()`: Retorna uma sessão de base de dados para interagir com os modelos.
-   `populate_sample_data()`: Popula a base de dados com dados de exemplo para demonstração, se a base de dados estiver vazia.

## 4. Lógica de Negócio e Frontend (app.py e pages/)

A lógica de negócio está integrada nos scripts Streamlit. A aplicação `app.py` gere o fluxo de login e a navegação entre as páginas, que são ficheiros Python separados dentro do diretório `pages/`.

### 4.1. `app.py`

-   **Configuração**: Define o título da página, ícone, layout e estado inicial da sidebar.
-   **Inicialização**: Chama `init_db()` e `populate_sample_data()` para garantir que a base de dados está pronta.
-   **Gestão de Sessão**: Utiliza `st.session_state` para gerir o estado de login do utilizador (`logged_in`, `user`, `role`).
-   **Login/Logout**: Funções para autenticar utilizadores e gerir o estado de sessão.
-   **Navegação**: Utiliza `st.page_link` para criar links para as páginas específicas de cada perfil (Admin, Instrutor, Aluno).
-   **Dashboard Principal**: Exibe uma visão geral com métricas e aulas de hoje para o administrador, e informações básicas para alunos e instrutores.

### 4.2. Páginas (pages/)

Cada ficheiro Python em `pages/` representa uma secção da aplicação, acessível através da sidebar. As páginas verificam o estado de login e o perfil do utilizador antes de exibir o conteúdo.

-   **`1_👥_Gestão_de_Alunos.py`**: Tabela de alunos com pesquisa e opção de adicionar novo aluno.
-   **`2_📅_Gestão_de_Aulas.py`**: Calendário semanal e lista de aulas.
-   **`3_💰_Gestão_Financeira.py`**: Métricas financeiras, pagamentos recentes e gráfico de distribuição de despesas.
-   **`4_🛒_Gestão_de_Produtos.py`**: Métricas de produtos, tabela de produtos com stock e opção de adicionar novo produto.
-   **`5_📈_Relatórios.py`**: Gráficos de receitas vs despesas, taxa de frequência e distribuição de planos.
-   **`7_🛒_Loja.py`**: Exibição de produtos, funcionalidade de adicionar ao carrinho e finalizar compra.
-   **`8_💳_Pagamentos.py`**: Informações do plano atual, planos disponíveis, métodos de pagamento e histórico de pagamentos.
-   **`9_👤_Meu_Perfil.py`**: Formulário para edição de informações pessoais e alteração de palavra-passe, e estatísticas do aluno.

## 5. Configuração do Streamlit (`.streamlit/config.toml`)

Este ficheiro configura aspetos visuais e de servidor do Streamlit:

-   **`[theme]`**: Define cores primárias, de fundo, texto e fonte para personalizar a aparência da aplicação.
-   **`[server]`**: Configura o servidor Streamlit, incluindo `headless = true` (para deploy em ambientes sem GUI) e a porta (`8501`).

## 6. Deploy e Escalabilidade

### 6.1. GitHub e Streamlit Cloud

A aplicação é projetada para um deploy contínuo e fácil no Streamlit Cloud. Basta conectar o repositório GitHub ao Streamlit Cloud, e qualquer `push` para o branch configurado acionará um redeploy automático.

### 6.2. Persistência de Dados

Para a versão Streamlit Cloud, o ficheiro `estudio_elsa_pilates.db` é versionado no GitHub. No entanto, o Streamlit Cloud pode reiniciar as instâncias da aplicação, o que pode levar à perda de dados se o ficheiro `.db` não for tratado corretamente (ex: recriado a cada deploy). Para dados persistentes em produção, recomenda-se:

-   **Base de Dados Externa**: Utilizar um serviço de base de dados externa (ex: PostgreSQL, MySQL) e configurar a conexão através de `st.secrets` no Streamlit Cloud.
-   **Armazenamento de Ficheiros**: Para SQLite, usar um serviço de armazenamento de ficheiros persistente (ex: S3, Google Cloud Storage) para guardar o ficheiro `.db`.

### 6.3. Segurança

Esta versão de demonstração utiliza palavras-passe em texto simples para simplificar. Para produção, é **essencial** implementar:

-   **Hash de Palavras-passe**: Utilizar bibliotecas como `bcrypt` para armazenar hashes seguros das palavras-passe.
-   **Autenticação Segura**: Considerar JWT ou OAuth para gestão de sessões.
-   **Validação de Inputs**: Implementar validação robusta em todos os inputs do utilizador.

## 7. Roadmap Futuro

-   Implementação completa das funcionalidades de adicionar/editar/remover em todas as páginas.
-   Integração com APIs de pagamento reais.
-   Sistema de notificações (e-mail, SMS).
-   Funcionalidades de gestão de pessoal de apoio.
-   Otimização para grandes volumes de dados e utilizadores.
-   Implementação de testes unitários e de integração.

---

**Desenvolvido por**: Manus AI  
**Data**: Outubro de 2025

