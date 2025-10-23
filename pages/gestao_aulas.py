import streamlit as st
import pandas as pd

# Verificar se o utilizador está logado e é admin
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.error("Por favor, faça login primeiro.")
    st.stop()

if st.session_state.role != "admin":
    st.error("Acesso negado. Esta página é apenas para administradores.")
    st.stop()

st.title("📅 Gestão de Aulas")

# Calendário semanal
st.subheader("📆 Calendário Semanal")

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
aulas_por_dia = [8, 7, 8, 6, 7, 4, 0]

for col, dia, aulas in zip([col1, col2, col3, col4, col5, col6, col7], dias_semana, aulas_por_dia):
    with col:
        st.metric(dia, f"{aulas} aulas")

st.markdown("---")

# Aulas de Segunda-feira
st.subheader("📋 Aulas de Segunda-feira")

aulas_segunda = pd.DataFrame({
    "Horário": ["08:00", "09:30", "11:00", "14:00", "16:00", "18:00", "19:30", "21:00"],
    "Aula": ["Pilates Mat", "Pilates Reformer", "Pilates Mat", "Pilates Cadillac", "Pilates Mat", "Pilates Reformer", "Pilates Mat", "Pilates Reformer"],
    "Instrutor": ["Maria Silva", "Ana Costa", "Maria Silva", "Ana Costa", "Maria Silva", "Ana Costa", "Maria Silva", "Ana Costa"],
    "Ocupação": ["8/10", "10/10", "7/10", "9/10", "10/10", "8/10", "6/10", "9/10"],
    "Taxa": ["80%", "100%", "70%", "90%", "100%", "80%", "60%", "90%"]
})

st.dataframe(
    aulas_segunda,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Horário": st.column_config.TextColumn("Horário", width="small"),
        "Aula": st.column_config.TextColumn("Aula", width="medium"),
        "Instrutor": st.column_config.TextColumn("Instrutor", width="medium"),
        "Ocupação": st.column_config.TextColumn("Ocupação", width="small"),
        "Taxa": st.column_config.TextColumn("Taxa", width="small")
    }
)

col1, col2 = st.columns([3, 1])

with col2:
    if st.button("➕ Nova Aula", use_container_width=True, type="primary"):
        st.info("Funcionalidade de adicionar nova aula em desenvolvimento.")


