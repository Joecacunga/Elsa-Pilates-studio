import streamlit as st
from database.models import init_db, populate_sample_data, get_db, User
import time

# Configuração da página
st.set_page_config(
    page_title="Estúdio Elsa Pilates",
    page_icon="🧘‍♀️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Inicializar a base de dados e popular com dados de exemplo
init_db()
populate_sample_data()

# Funções de autenticação
def check_password(username, password):
    db_session = get_db()
    user = db_session.query(User).filter_by(username=username).first()
    db_session.close()
    if user and user.password_hash == password:  # Em um ambiente real, use bcrypt para hash de senhas
        return user
    return None

def login_form():
    st.title("Login - Estúdio Elsa Pilates")

    with st.form("login_form"):
        username = st.text_input("Utilizador")
        password = st.text_input("Palavra-passe", type="password")
        submitted = st.form_submit_button("Entrar")

        if submitted:
            user = check_password(username, password)
            if user:
                st.session_state["logged_in"] = True
                st.session_state["user"] = user.username
                st.session_state["role"] = user.role
                st.success(f"Bem-vindo(a), {user.first_name}!")
                time.sleep(1) # Pequena pausa para a mensagem ser visível
                st.rerun()
            else:
                st.error("Utilizador ou palavra-passe incorretos.")

def logout():
    st.session_state["logged_in"] = False
    st.session_state["user"] = None
    st.session_state["role"] = None
    st.info("Sessão terminada com sucesso.")
    time.sleep(1)
    st.rerun()

# Lógica principal da aplicação
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login_form()
else:
    st.sidebar.title(f"Olá, {st.session_state['user']}!")
    st.sidebar.write(f"**Perfil:** {st.session_state['role'].capitalize()}")

    if st.session_state["role"] == "admin":
        st.sidebar.header("Administração")
        st.sidebar.page_link("app.py", label="📊 Visão Geral", icon="📊")
        st.sidebar.page_link("pages/gestao_alunos.py", label="👥 Gestão de Alunos", icon="👥")
        st.sidebar.page_link("pages/gestao_aulas.py", label="📅 Gestão de Aulas", icon="📅")
        st.sidebar.page_link("pages/gestao_financeira.py", label="💰 Gestão Financeira", icon="💰")
        st.sidebar.page_link("pages/gestao_produtos.py", label="🛒 Gestão de Produtos", icon="🛒")
        st.sidebar.page_link("pages/relatorios.py", label="📈 Relatórios", icon="📈")

        st.title("📊 Dashboard do Administrador")
        st.write("Bem-vindo ao dashboard de administração do Estúdio Elsa Pilates.")
        # Aqui você adicionaria os componentes do dashboard, como métricas e gráficos
        st.subheader("Métricas Rápidas")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric(label="Total de Alunos", value="156", delta="+5 desde o mês passado")
        with col2:
            st.metric(label="Aulas Hoje", value="24", delta="+2 em relação a ontem")
        with col3:
            st.metric(label="Receita Mensal", value="€12.450", delta="+10% em relação ao mês passado")
        with col4:
            st.metric(label="Taxa de Ocupação", value="87%", delta="+3% em relação ao mês passado")

        st.subheader("Aulas de Hoje")
        st.write("Conteúdo das aulas de hoje...")

    elif st.session_state["role"] == "instructor":
        st.sidebar.header("Instrutor")
        st.sidebar.page_link("app.py", label="🗓️ Meu Horário", icon="🗓️")
        st.sidebar.page_link("pages/meus_alunos.py", label="👥 Meus Alunos", icon="👥") # Supondo que você crie esta página

        st.title("🗓️ Meu Horário")
        st.write("Bem-vindo ao seu horário de instrutor.")
        # Conteúdo do horário do instrutor

    elif st.session_state["role"] == "student":
        st.sidebar.header("Aluno")
        st.sidebar.page_link("app.py", label="🧘‍♀️ Minhas Aulas", icon="🧘‍♀️")
        st.sidebar.page_link("pages/loja.py", label="🛒 Loja", icon="🛒")
        st.sidebar.page_link("pages/pagamentos.py", label="💳 Pagamentos", icon="💳")
        st.sidebar.page_link("pages/meu_perfil.py", label="👤 Meu Perfil", icon="👤")

        st.title("🧘‍♀️ Minhas Aulas")
        st.write("Bem-vindo à sua área de aluno.")
        # Conteúdo das aulas do aluno

    st.sidebar.markdown("--- ")
    st.sidebar.button("Sair", on_click=logout)

