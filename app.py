import streamlit as st
from database.models import init_db, populate_sample_data, get_db, User
from sqlalchemy.orm import Session

# Configuração da página
st.set_page_config(
    page_title="ESTÚDIO ELSA PILATES",
    page_icon="🧘‍♀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicializar a base de dados
init_db()
populate_sample_data()

# Inicializar o estado da sessão
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user' not in st.session_state:
    st.session_state.user = None
if 'role' not in st.session_state:
    st.session_state.role = None

# Função de login
def login(username, password):
    db = get_db()
    user = db.query(User).filter(User.username == username).first()
    
    if user and user.password_hash == password:  # Em produção, verificar hash
        st.session_state.logged_in = True
        st.session_state.user = user
        st.session_state.role = user.role
        db.close()
        return True
    
    db.close()
    return False

# Função de logout
def logout():
    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.role = None
    st.rerun()

# Página de Login
if not st.session_state.logged_in:
    st.title("🧘‍♀️ ESTÚDIO ELSA PILATES")
    st.subheader("Sistema de Gestão")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("---")
        st.markdown("### 🔐 Login")
        
        username = st.text_input("Utilizador", placeholder="Digite o seu nome de utilizador")
        password = st.text_input("Palavra-passe", type="password", placeholder="Digite a sua palavra-passe")
        
        if st.button("Entrar", use_container_width=True, type="primary"):
            if login(username, password):
                st.success("Login realizado com sucesso!")
                st.rerun()
            else:
                st.error("Utilizador ou palavra-passe incorretos.")
        
        st.markdown("---")
        st.info("""
        **Credenciais de Teste:**
        - Administrador: `admin` / `password`
        - Instrutor: `instructor` / `password`
        - Aluno: `student` / `password`
        """)

# Página Principal (após login)
else:
    # Sidebar com informações do utilizador
    with st.sidebar:
        st.title("🧘‍♀️ ESTÚDIO ELSA PILATES")
        st.markdown("---")
        
        st.markdown(f"**Utilizador:** {st.session_state.user.first_name} {st.session_state.user.last_name}")
        st.markdown(f"**Perfil:** {st.session_state.role.capitalize()}")
        st.markdown("---")
        
        # Navegação baseada no perfil
        if st.session_state.role == "admin":
            st.page_link("app.py", label="📊 Visão Geral", icon="📊")
            st.page_link("pages/1_👥_Gestão_de_Alunos.py", label="👥 Gestão de Alunos", icon="👥")
            st.page_link("pages/2_📅_Gestão_de_Aulas.py", label="📅 Gestão de Aulas", icon="📅")
            st.page_link("pages/3_💰_Gestão_Financeira.py", label="💰 Gestão Financeira", icon="💰")
            st.page_link("pages/4_🛒_Gestão_de_Produtos.py", label="🛒 Gestão de Produtos", icon="🛒")
            st.page_link("pages/5_📈_Relatórios.py", label="📈 Relatórios", icon="📈")
        
        elif st.session_state.role == "instructor":
            st.page_link("app.py", label="📊 Meu Horário", icon="📊")
            st.page_link("pages/6_👥_Meus_Alunos.py", label="👥 Meus Alunos", icon="👥")
        
        elif st.session_state.role == "student":
            st.page_link("app.py", label="📊 Minhas Aulas", icon="📊")
            st.page_link("pages/7_🛒_Loja.py", label="🛒 Loja", icon="🛒")
            st.page_link("pages/8_💳_Pagamentos.py", label="💳 Pagamentos", icon="💳")
            st.page_link("pages/9_👤_Meu_Perfil.py", label="👤 Meu Perfil", icon="👤")
        
        st.markdown("---")
        
        if st.button("🚪 Sair", use_container_width=True):
            logout()
    
    # Conteúdo principal baseado no perfil
    if st.session_state.role == "admin":
        st.title("📊 Visão Geral do Estúdio")
        
        # Métricas principais
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total de Alunos", "156", "+12")
        
        with col2:
            st.metric("Aulas Hoje", "24", "+2")
        
        with col3:
            st.metric("Receita Mensal", "€12,450", "+8.5%")
        
        with col4:
            st.metric("Taxa de Ocupação", "87%", "+3%")
        
        st.markdown("---")
        
        # Aulas de Hoje
        st.subheader("📅 Aulas de Hoje")
        
        import pandas as pd
        
        aulas_hoje = pd.DataFrame({
            "Horário": ["08:00", "09:30", "11:00", "14:00", "16:00", "18:00"],
            "Aula": ["Pilates Mat", "Pilates Reformer", "Pilates Mat", "Pilates Cadillac", "Pilates Mat", "Pilates Reformer"],
            "Instrutor": ["Maria Silva", "Ana Costa", "Maria Silva", "Ana Costa", "Maria Silva", "Ana Costa"],
            "Ocupação": ["8/10", "10/10", "7/10", "9/10", "10/10", "8/10"],
            "Taxa": ["80%", "100%", "70%", "90%", "100%", "80%"]
        })
        
        st.dataframe(aulas_hoje, use_container_width=True, hide_index=True)
    
    elif st.session_state.role == "instructor":
        st.title("📅 Meu Horário")
        st.info("Funcionalidade em desenvolvimento para instrutores.")
    
    elif st.session_state.role == "student":
        st.title("📊 Minhas Aulas")
        
        # Informações do plano
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.info(f"""
            **Plano Atual:** Premium
            
            **Créditos Disponíveis:** 8/12
            
            **Próxima Renovação:** 01/02/2025
            """)
        
        with col2:
            st.subheader("🎯 Aulas Reservadas")
            
            import pandas as pd
            
            aulas_reservadas = pd.DataFrame({
                "Data": ["10/10/2025", "12/10/2025", "15/10/2025"],
                "Horário": ["08:00", "09:30", "18:00"],
                "Aula": ["Pilates Mat", "Pilates Reformer", "Pilates Mat"],
                "Instrutor": ["Maria Silva", "Ana Costa", "Maria Silva"]
            })
            
            st.dataframe(aulas_reservadas, use_container_width=True, hide_index=True)

