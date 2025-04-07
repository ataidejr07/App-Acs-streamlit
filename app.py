import streamlit as st

st.set_page_config(page_title="ACS Micro Área", layout="wide")

# CSS personalizado
st.markdown("""
    <style>
        .header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #0066ff;
            color: white;
            padding: 14px 10px;
            z-index: 1000;
            display: flex;
            align-items: center;
            box-shadow: 0 2px 6px rgba(0,0,0,0.2);
        }

        .menu-button {
            background-color: #0047b3;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 10px 14px;
            font-size: 22px;
            cursor: pointer;
            margin-right: 15px;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
        }

        .header-title {
            font-size: 22px;
            font-weight: bold;
        }

        .main-content {
            padding-top: 80px;
        }

        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #0066ff;
            color: white;
            text-align: center;
            padding: 10px;
            z-index: 1000;
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho HTML
st.markdown("""
    <div class="header">
        <form action="#menu">
            <button class="menu-button" type="submit">☰</button>
        </form>
        <div class="header-title">ACS Micro Área</div>
    </div>
""", unsafe_allow_html=True)

# Conteúdo principal
st.markdown('<div class="main-content">', unsafe_allow_html=True)

st.markdown("## Bem-vindo, Ataide!")

st.markdown("### Cadastros")
st.button("🏠 Domicílios")
st.button("👨‍👩‍👧 Famílias")
st.button("🧑 Cidadãos")

st.markdown("### Análises e Relatórios")
st.button("📊 Relatórios")
st.button("📈 Resumo de Produção")
st.button("👶⚰️ Nascimentos e Óbitos")

st.markdown('</div>', unsafe_allow_html=True)

# Menu lateral
with st.sidebar:
    st.markdown("### Menu")
    st.page_link("app.py", label="Cartões Espelho", icon="🗂️")
    st.page_link("app.py", label="Laudos e Receitas", icon="📝")

# Rodapé
st.markdown("""
    <div class="footer">
        Desenvolvido para ACS
    </div>
""", unsafe_allow_html=True)
