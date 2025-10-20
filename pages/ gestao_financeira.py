import streamlit as st
import pandas as pd
import plotly.express as px
from database.models import get_db, Payment, Student, User

# Verificar se o utilizador está logado e é admin
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.error("Por favor, faça login primeiro.")
    st.stop()

if st.session_state.role != "admin":
    st.error("Acesso negado. Esta página é apenas para administradores.")
    st.stop()

st.title("💰 Gestão Financeira")

# Métricas financeiras
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Receitas do Mês", "€15,240", "+12.5%")

with col2:
    st.metric("Despesas do Mês", "€8,450", "+5.2%")

with col3:
    st.metric("Lucro Líquido", "€6,790", "+23.8%")

with col4:
    st.metric("Pagamentos Pendentes", "€1,200", "-8.3%")

st.markdown("---")

# Pagamentos recentes
st.subheader("💳 Pagamentos Recentes")

db = get_db()
payments = db.query(Payment).join(Student).join(User).order_by(Payment.payment_date.desc()).limit(10).all()

data = []
for payment in payments:
    data.append({
        "Data": payment.payment_date.strftime("%d/%m/%Y"),
        "Aluno": f"{payment.student.user.first_name} {payment.student.user.last_name}",
        "Descrição": payment.description,
        "Método": payment.payment_method,
        "Valor": f"€{payment.amount:.2f}",
        "Estado": payment.status.capitalize()
    })

df = pd.DataFrame(data)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# Gráfico de distribuição de despesas
st.subheader("📊 Distribuição de Despesas")

despesas_data = pd.DataFrame({
    "Categoria": ["Salários", "Renda", "Equipamento", "Marketing", "Outros"],
    "Valor": [5150, 1950, 750, 350, 250]
})

fig = px.pie(
    despesas_data,
    values="Valor",
    names="Categoria",
    title="Distribuição de Despesas por Categoria",
    hole=0.4
)

st.plotly_chart(fig, use_container_width=True)

db.close()

