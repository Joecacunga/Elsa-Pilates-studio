# Guia Rápido de Utilização - ESTÚDIO ELSA PILATES (Streamlit)

Bem-vindo(a) ao seu novo sistema de gestão para estúdios de Pilates! Este guia rápido irá ajudá-lo(a) a começar a usar a aplicação "ESTÚDIO ELSA PILATES" desenvolvida com Streamlit.

## 🚀 Aceder à Aplicação

Após o deploy no Streamlit Cloud, a aplicação estará disponível num URL público (ex: `https://seu-nome.streamlit.app`).

## 🔑 Login

Ao aceder à aplicação, será apresentada a página de login. Utilize as seguintes credenciais de teste:

| Perfil        | Utilizador   | Palavra-passe |
|---------------|--------------|---------------|
| Administrador | `admin`      | `password`    |
| Instrutor     | `instructor` | `password`    |
| Aluno         | `student`    | `password`    |

## 👤 Perfis de Utilizador

A aplicação possui três perfis de utilizador, cada um com acesso a funcionalidades específicas:

### 1. Administrador

O perfil de Administrador tem acesso total a todas as funcionalidades do sistema. Após o login, verá um dashboard com métricas gerais e uma sidebar com as seguintes opções:

-   **📊 Visão Geral**: Dashboard principal com estatísticas do estúdio (alunos, aulas, receita, ocupação).
-   **👥 Gestão de Alunos**: Gerir o registo de alunos, ver detalhes, pesquisar e adicionar novos alunos.
-   **📅 Gestão de Aulas**: Visualizar o calendário semanal de aulas, ocupação e adicionar novas aulas.
-   **💰 Gestão Financeira**: Acompanhar receitas, despesas, lucro e pagamentos recentes. Ver gráficos de distribuição de despesas.
-   **🛒 Gestão de Produtos**: Gerir o inventário de produtos, preços, stock e vendas. Adicionar novos produtos.
-   **📈 Relatórios**: Aceder a relatórios gráficos sobre finanças, frequência de aulas e distribuição de planos.

### 2. Instrutor

O perfil de Instrutor tem acesso a funcionalidades relacionadas com as suas aulas e alunos. Após o login, terá acesso a:

-   **📊 Meu Horário**: Visualizar o seu horário de aulas.
-   **👥 Meus Alunos**: Acompanhar os alunos sob a sua responsabilidade.

### 3. Aluno

O perfil de Aluno permite gerir as suas aulas, pagamentos e compras. Após o login, terá acesso a:

-   **📊 Minhas Aulas**: Ver o seu plano atual, créditos disponíveis e aulas reservadas.
-   **🛒 Loja**: Navegar e comprar produtos do estúdio.
-   **💳 Pagamentos**: Consultar o seu plano, métodos de pagamento e histórico de pagamentos.
-   **👤 Meu Perfil**: Visualizar e editar as suas informações pessoais e alterar a palavra-passe.

## 💡 Dicas de Utilização

-   **Navegação**: Utilize a sidebar à esquerda para navegar entre as diferentes secções da aplicação.
-   **Dados de Exemplo**: A base de dados é populada com dados de exemplo na primeira execução. Pode adicionar os seus próprios dados através das funcionalidades de gestão.
-   **Atualizações**: Se a aplicação for atualizada no GitHub, o Streamlit Cloud fará o redeploy automaticamente, e as alterações estarão visíveis após alguns minutos.

## 🔒 Segurança (Importante)

Esta versão é para demonstração. Para uso em produção, é crucial implementar medidas de segurança adicionais, como o hash de palavras-passe e a utilização de uma base de dados persistente externa.

---

**Desenvolvido por**: Manus AI  
**Data**: Outubro de 2025

