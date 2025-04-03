import streamlit as st

# Configuração da página
st.set_page_config(page_title="ACS Micro Área", layout="wide")

# Estilos CSS para o cabeçalho fixo e o rodapé fixo
st.markdown(
    """
    <style>
        /* Cabeçalho fixo */
        .header {
            background-color: #0056b3;
            color: white;
            padding: 10px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
        }

        /* Rodapé fixo */
        .footer {
            background-color: #0056b3;
            color: white;
            padding: 10px;
            text-align: center;
            font-size: 14px;
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
        }

        /* Espaço extra para evitar sobreposição */
        .content {
            margin-top: 60px;
            margin-bottom: 50px;
        }

        /* Botões estilizados */
        .custom-button {
            display: block;
            width: 100%;
            padding: 15px;
            text-align: left;
            border: 2px solid #ccc;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
            background-color: white;
            transition: 0.3s;
        }

        .custom-button:hover {
            background-color: #f0f0f0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Cabeçalho fixo
st.markdown('<div class="header">ACS Micro Área</div>', unsafe_allow_html=True)

# Conteúdo principal
st.markdown('<div class="content">', unsafe_allow_html=True)

st.title("Bem-vindo, Ataide!")

st.subheader("Cadastros")
st.markdown('<button class="custom-button">🏡 Domicílios</button>', unsafe_allow_html=True)
st.markdown('<button class="custom-button">👨‍👩‍👧‍👦 Famílias</button>', unsafe_allow_html=True)
st.markdown('<button class="custom-button">🧑 Cidadãos</button>', unsafe_allow_html=True)

st.subheader("Análises e Relatórios")
st.markdown('<button class="custom-button">📊 Relatórios</button>', unsafe_allow_html=True)
st.markdown('<button class="custom-button">📈 Resumo de Produção</button>', unsafe_allow_html=True)
st.markdown('<button class="custom-button">👶⚰️ Nascimentos e Óbitos</button>', unsafe_allow_html=True)

# Menu lateral com todas as funcionalidades
st.sidebar.title("Menu")
st.sidebar.button("🏡 Domicílios")
st.sidebar.button("👨‍👩‍👧‍👦 Famílias")
st.sidebar.button("🧑 Cidadãos")
st.sidebar.button("📄 Laudos e Receitas")
st.sidebar.button("🪪 Cartões Espelho")

# Rodapé fixo
st.markdown('<div class="footer">Desenvolvido para ACS</div>', unsafe_allow_html=True)

# Fechando o conteúdo principal
st.markdown('</div>', unsafe_allow_html=True)
