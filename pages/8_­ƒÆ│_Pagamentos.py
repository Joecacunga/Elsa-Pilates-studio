import streamlit as st
import pandas as pd
from database.models import get_db, Payment, Student, User

# Verificar se o utilizador está logado e é aluno
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.error("Por favor, faça login primeiro.")
    st.stop()

if st.session_state.role != "student":
    st.error("Acesso negado. Esta página é apenas para alunos.")
    st.stop()

st.title("💳 Pagamentos e Planos")

# Obter dados do aluno
db = get_db()
student = db.query(Student).join(User).filter(User.id == st.session_state.user.id).first()

# Informações do plano atual
col1, col2 = st.columns([1, 2])

with col1:
    st.info(f"""
    **Plano Atual:** {student.plan}
    
    **Valor Mensal:** €80.00
    
    **Próximo Pagamento:** 01/11/2025
    
    **Estado:** Ativo
    """)

with col2:
    st.subheader("📋 Planos Disponíveis")
    
    planos = pd.DataFrame({
        "Plano": ["Básico", "Premium", "Livre-Trânsito"],
        "Aulas/Mês": ["4 aulas", "12 aulas", "Ilimitado"],
        "Preço": ["€50", "€80", "€120"]
    })
    
    st.dataframe(planos, use_container_width=True, hide_index=True)
    
    if st.button("🔄 Mudar de Plano", use_container_width=True):
        st.info("Funcionalidade de mudança de plano em desenvolvimento.")

st.markdown("---")

# Método de pagamento
st.subheader("💳 Método de Pagamento")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📱 MB Way", use_container_width=True):
        st.success("MB Way selecionado")

with col2:
    if st.button("💳 Cartão", use_container_width=True):
        st.success("Cartão selecionado")

with col3:
    if st.button("🏦 Transferência", use_container_width=True):
        st.success("Transferência selecionada")

st.markdown("---")

# Histórico de pagamentos
st.subheader("📜 Histórico de Pagamentos")

payments = db.query(Payment).filter(Payment.student_id == student.id).order_by(Payment.payment_date.desc()).all()

data = []
for payment in payments:
    data.append({
        "Data": payment.payment_date.strftime("%d/%m/%Y"),
        "Descrição": payment.description,
        "Método": payment.payment_method,
        "Valor": f"€{payment.amount:.2f}",
        "Estado": payment.status.capitalize()
    })

df = pd.DataFrame(data)

st.dataframe(df, use_container_width=True, hide_index=True)

db.close()

