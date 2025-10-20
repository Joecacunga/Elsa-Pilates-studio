import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Verificar se o utilizador está logado e é admin
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.error("Por favor, faça login primeiro.")
    st.stop()

if st.session_state.role != "admin":
    st.error("Acesso negado. Esta página é apenas para administradores.")
    st.stop()

st.title("📈 Relatórios e Análise")

# Gráfico de Receitas vs Despesas
st.subheader("💰 Receitas vs Despesas (Últimos 6 Meses)")

financeiro_data = pd.DataFrame({
    "Mês": ["Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro"],
    "Receitas": [12500, 13200, 14100, 13800, 14500, 15240],
    "Despesas": [7800, 8100, 8300, 8200, 8400, 8450]
})

fig1 = go.Figure()
fig1.add_trace(go.Bar(x=financeiro_data["Mês"], y=financeiro_data["Receitas"], name="Receitas", marker_color='#2ecc71'))
fig1.add_trace(go.Bar(x=financeiro_data["Mês"], y=financeiro_data["Despesas"], name="Despesas", marker_color='#e74c3c'))
fig1.update_layout(barmode='group', xaxis_title="Mês", yaxis_title="Valor (€)")

st.plotly_chart(fig1, use_container_width=True)

st.markdown("---")

# Gráfico de Taxa de Frequência Semanal
st.subheader("📊 Taxa de Frequência Semanal")

frequencia_data = pd.DataFrame({
    "Dia": ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"],
    "Taxa": [92, 88, 90, 85, 87, 75, 0]
})

fig2 = px.line(
    frequencia_data,
    x="Dia",
    y="Taxa",
    title="Taxa de Ocupação por Dia da Semana (%)",
    markers=True
)
fig2.update_traces(line_color='#3498db', line_width=3)

st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# Gráfico de Distribuição de Planos
st.subheader("🎯 Distribuição de Planos")

planos_data = pd.DataFrame({
    "Plano": ["Premium", "Básico", "Livre-Trânsito"],
    "Alunos": [70, 55, 31]
})

fig3 = px.pie(
    planos_data,
    values="Alunos",
    names="Plano",
    title="Distribuição de Alunos por Plano",
    hole=0.4,
    color_discrete_sequence=['#3498db', '#2ecc71', '#f39c12']
)

st.plotly_chart(fig3, use_container_width=True)

