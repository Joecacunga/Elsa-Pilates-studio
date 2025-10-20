import streamlit as st
import pandas as pd
from database.models import get_db, Product

# Verificar se o utilizador está logado e é admin
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.error("Por favor, faça login primeiro.")
    st.stop()

if st.session_state.role != "admin":
    st.error("Acesso negado. Esta página é apenas para administradores.")
    st.stop()

st.title("🛒 Gestão de Produtos")

# Métricas de produtos
db = get_db()
products = db.query(Product).all()

total_revenue = sum(p.price * p.sold for p in products)
total_stock = sum(p.stock for p in products)
total_products = len(products)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Receita Total", f"€{total_revenue:.2f}")

with col2:
    st.metric("Stock Total", f"{total_stock} unidades")

with col3:
    st.metric("Produtos Cadastrados", total_products)

st.markdown("---")

# Tabela de produtos
st.subheader("📦 Produtos")

data = []
for product in products:
    stock_status = "Bom" if product.stock > 20 else ("Médio" if product.stock > 10 else "Baixo")
    data.append({
        "ID": product.id,
        "Nome": product.name,
        "Categoria": product.category,
        "Preço": f"€{product.price:.2f}",
        "Stock": product.stock,
        "Vendidos": product.sold,
        "Estado Stock": stock_status
    })

df = pd.DataFrame(data)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "ID": st.column_config.NumberColumn("ID", width="small"),
        "Nome": st.column_config.TextColumn("Nome", width="medium"),
        "Categoria": st.column_config.TextColumn("Categoria", width="small"),
        "Preço": st.column_config.TextColumn("Preço", width="small"),
        "Stock": st.column_config.NumberColumn("Stock", width="small"),
        "Vendidos": st.column_config.NumberColumn("Vendidos", width="small"),
        "Estado Stock": st.column_config.TextColumn("Estado Stock", width="small")
    }
)

col1, col2 = st.columns([3, 1])

with col2:
    if st.button("➕ Novo Produto", use_container_width=True, type="primary"):
        st.info("Funcionalidade de adicionar novo produto em desenvolvimento.")

db.close()

