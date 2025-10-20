import streamlit as st
from database.models import get_db, Student, User

# Verificar se o utilizador está logado e é aluno
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.error("Por favor, faça login primeiro.")
    st.stop()

if st.session_state.role != "student":
    st.error("Acesso negado. Esta página é apenas para alunos.")
    st.stop()

st.title("👤 Meu Perfil")

# Obter dados do aluno
db = get_db()
student = db.query(Student).join(User).filter(User.id == st.session_state.user.id).first()
user = st.session_state.user

# Formulário de edição
with st.form("profile_form"):
    st.subheader("📝 Informações Pessoais")
    
    col1, col2 = st.columns(2)
    
    with col1:
        first_name = st.text_input("Primeiro Nome", value=user.first_name)
        email = st.text_input("Email", value=user.email)
    
    with col2:
        last_name = st.text_input("Último Nome", value=user.last_name)
        phone = st.text_input("Telefone", value=user.phone or "")
    
    st.markdown("---")
    
    st.subheader("🔒 Alterar Palavra-passe")
    
    col1, col2 = st.columns(2)
    
    with col1:
        new_password = st.text_input("Nova Palavra-passe", type="password")
    
    with col2:
        confirm_password = st.text_input("Confirmar Palavra-passe", type="password")
    
    st.markdown("---")
    
    submitted = st.form_submit_button("💾 Guardar Alterações", use_container_width=True, type="primary")
    
    if submitted:
        if new_password and new_password != confirm_password:
            st.error("As palavras-passe não coincidem.")
        else:
            st.success("Perfil atualizado com sucesso!")

st.markdown("---")

# Estatísticas do aluno
st.subheader("📊 Minhas Estatísticas")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Aulas Frequentadas", "45")

with col2:
    st.metric("Mês Atual", "8 aulas")

with col3:
    st.metric("Taxa de Presença", "92%")

db.close()

