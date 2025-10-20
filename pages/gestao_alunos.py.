import streamlit as st
import pandas as pd
from database.models import get_db, User, Student

# Verificar se o utilizador está logado e é admin
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.error("Por favor, faça login primeiro.")
    st.stop()

if st.session_state.role != "admin":
    st.error("Acesso negado. Esta página é apenas para administradores.")
    st.stop()

st.title("👥 Gestão de Alunos")

# Obter dados dos alunos
db = get_db()
students = db.query(Student).join(User).all()

# Criar DataFrame
data = []
for student in students:
    data.append({
        "ID": student.id,
        "Nome": f"{student.user.first_name} {student.user.last_name}",
        "Email": student.user.email,
        "Telefone": student.user.phone or "N/A",
        "Plano": student.plan or "Sem plano",
        "Créditos": student.credits,
        "Estado": "Ativo" if student.is_active else "Inativo"
    })

df = pd.DataFrame(data)

# Barra de pesquisa
col1, col2 = st.columns([3, 1])

with col1:
    search = st.text_input("🔍 Pesquisar aluno (nome ou email)", placeholder="Digite o nome ou email do aluno")

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("➕ Novo Aluno", use_container_width=True, type="primary"):
        st.info("Funcionalidade de adicionar novo aluno em desenvolvimento.")

# Filtrar dados se houver pesquisa
if search:
    df = df[df['Nome'].str.contains(search, case=False) | df['Email'].str.contains(search, case=False)]

# Exibir tabela
st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "ID": st.column_config.NumberColumn("ID", width="small"),
        "Nome": st.column_config.TextColumn("Nome", width="medium"),
        "Email": st.column_config.TextColumn("Email", width="medium"),
        "Telefone": st.column_config.TextColumn("Telefone", width="small"),
        "Plano": st.column_config.TextColumn("Plano", width="small"),
        "Créditos": st.column_config.NumberColumn("Créditos", width="small"),
        "Estado": st.column_config.TextColumn("Estado", width="small")
    }
)

st.markdown(f"**Total de alunos:** {len(df)}")

db.close()

