import streamlit as st
from database.models import get_db, Product

# Verificar se o utilizador está logado e é aluno
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.error("Por favor, faça login primeiro.")
    st.stop()

if st.session_state.role != "student":
    st.error("Acesso negado. Esta página é apenas para alunos.")
    st.stop()

st.title("🛒 Loja do Estúdio")

# Inicializar carrinho na sessão
if 'cart' not in st.session_state:
    st.session_state.cart = []

# Obter produtos
db = get_db()
products = db.query(Product).filter(Product.is_active == True).all()

# Exibir produtos em grade
cols = st.columns(3)

for idx, product in enumerate(products):
    with cols[idx % 3]:
        st.markdown(f"### {product.name}")
        st.markdown(f"**Categoria:** {product.category}")
        st.markdown(f"**Preço:** €{product.price:.2f}")
        
        if product.stock > 0:
            st.success(f"Em Stock ({product.stock} unidades)")
            if st.button(f"🛒 Adicionar ao Carrinho", key=f"add_{product.id}"):
                st.session_state.cart.append({
                    "id": product.id,
                    "name": product.name,
                    "price": product.price
                })
                st.success(f"{product.name} adicionado ao carrinho!")
                st.rerun()
        else:
            st.error("Esgotado")
        
        st.markdown("---")

# Exibir carrinho
if st.session_state.cart:
    st.markdown("---")
    st.subheader(f"🛒 Carrinho ({len(st.session_state.cart)} item(ns))")
    
    total = sum(item['price'] for item in st.session_state.cart)
    
    for item in st.session_state.cart:
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.write(item['name'])
        with col2:
            st.write(f"€{item['price']:.2f}")
        with col3:
            if st.button("🗑️", key=f"remove_{item['id']}_{st.session_state.cart.index(item)}"):
                st.session_state.cart.remove(item)
                st.rerun()
    
    st.markdown(f"**Total:** €{total:.2f}")
    
    if st.button("✅ Finalizar Compra", type="primary", use_container_width=True):
        st.success("Compra finalizada com sucesso!")
        st.session_state.cart = []
        st.rerun()

db.close()

