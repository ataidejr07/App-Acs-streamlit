import streamlit as st
from PIL import Image

# Configuração da página
st.set_page_config(page_title="ACS Micro Área", layout="wide")

# Estilo CSS para ajustes visuais
st.markdown(
    """
    <style>
        .main .block-container {padding-top: 0rem;}
        .stApp {background-color: #f8f9fa;}
        .title-bar {background-color: #007bff; color: white; padding: 10px; text-align: center; font-size: 24px; font-weight: bold; position: fixed; width: 100%; top: 0; z-index: 1000;}
        .footer {background-color: #007bff; color: white; padding: 10px; text-align: center; position: fixed; bottom: 0; width: 100%; z-index: 1000;}
        .section {margin-top: 20px;}
        .stButton>button {border-radius: 10px; padding: 10px; width: 100%; font-size: 18px;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Barra de título fixa
st.markdown('<div class="title-bar">ACS Micro Área</div>', unsafe_allow_html=True)

# Espaço para evitar sobreposição com a barra fixa
st.write("\n\n\n")

# Mensagem de boas-vindas
st.markdown("### Bem-vindo, Ataide!")

# Seção de Cadastros
st.markdown("## Cadastros")
st.button("🏠 Domicílios")
st.button("👨‍👩‍👧 Famílias")
st.button("🧑 Cidadãos")

# Seção de Análises e Relatórios
st.markdown("## Análises e Relatórios")
st.button("📊 Relatórios")
st.button("📈 Resumo de Produção")
st.button("👶⚰️ Nascimentos e Óbitos")

# Seção de Funcionalidades Extras
st.markdown("## Funcionalidades Extras")
st.button("📝 Cartões Espelho")
st.button("📄 Laudos e Receitas")

# Rodapé fixo
st.markdown('<div class="footer">Desenvolvido para ACS | Versão 1.0</div>', unsafe_allow_html=True)
