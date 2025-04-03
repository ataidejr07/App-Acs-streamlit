import streamlit as st
from streamlit_option_menu import option_menu

# Configuração da página
st.set_page_config(page_title="ACS Micro Área", layout="wide")

# Estilo personalizado
st.markdown(
    """
    <style>
        .header {
            background-color: #0d6efd;
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 24px;
            font-weight: bold;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
        }
        .footer {
            background-color: #0d6efd;
            color: white;
            text-align: center;
            padding: 10px;
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
        }
        .main-content {
            padding-top: 60px;
            padding-bottom: 40px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Barra de Cabeçalho
st.markdown('<div class="header">ACS Micro Área</div>', unsafe_allow_html=True)

# Conteúdo principal
st.markdown('<div class="main-content">', unsafe_allow_html=True)

st.write("## Bem-vindo, Ataide!")

# Menu lateral
with st.sidebar:
    selected = option_menu("Menu", ["Início", "Domicílios", "Famílias", "Cidadãos", "Relatórios", "Resumo de Produção", "Nascimentos e Óbitos", "Cartões Espelho", "Laudos e Receitas"],
                           icons=["house", "building", "people", "person", "bar-chart", "clipboard-data", "activity", "clipboard", "file-text"],
                           menu_icon="list", default_index=0)

# Seções principais
st.write("### Cadastros")
st.button("🏠 Domicílios")
st.button("👨‍👩‍👧 Famílias")
st.button("🧑 Cidadãos")

st.write("### Análises e Relatórios")
st.button("📊 Relatórios")
st.button("📈 Resumo de Produção")
st.button("👶⚰️ Nascimentos e Óbitos")

st.write("### Funcionalidades Extras")
st.button("📋 Cartões Espelho")
st.button("📄 Laudos e Receitas")

# Rodapé
st.markdown('<div class="footer">Desenvolvido para ACS</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
