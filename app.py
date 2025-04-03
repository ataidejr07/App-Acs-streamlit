import streamlit as st

# Configuração da página
st.set_page_config(page_title="ACS Micro Área", layout="wide")

# Estilização
st.markdown("""
    <style>
        .header {
            background-color: #007bff;
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 22px;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
        }
        .container {
            padding-top: 60px;
        }
        .menu-lateral {
            position: fixed;
            left: 0;
            top: 50px;
            background: #f8f9fa;
            padding: 10px;
            width: 200px;
            height: 100%;
        }
        .content {
            margin-left: 220px;
        }
        .button {
            width: 100%;
            text-align: left;
            padding: 10px;
            border-radius: 10px;
            margin: 5px 0;
            background: white;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown('<div class="header">ACS Micro Área</div>', unsafe_allow_html=True)

# Layout principal
st.markdown('<div class="container">', unsafe_allow_html=True)

# Menu lateral
with st.sidebar:
    st.markdown("## Menu")
    st.button("🏠 Página Inicial")
    st.button("📋 Laudos e Receitas")
    st.button("🃏 Cartões Espelho")

# Conteúdo principal
st.markdown('<div class="content">', unsafe_allow_html=True)
st.markdown("### Bem-vindo, Ataide!")

st.subheader("Cadastros")
st.button("🏠 Domicílios", key="domicilios", help="Acessar cadastros de domicílios")
st.button("👨‍👩‍👧‍👦 Famílias", key="familias", help="Acessar cadastros de famílias")
st.button("🧑 Cidadãos", key="cidadãos", help="Acessar cadastros de cidadãos")

st.subheader("Análises e Relatórios")
st.button("📊 Relatórios", key="relatorios")
st.button("📈 Resumo de Produção", key="resumo_producao")
st.button("👶⚰️ Nascimentos e Óbitos", key="nascimentos_obitos")

st.markdown("</div>", unsafe_allow_html=True)
