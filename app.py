import streamlit as st

# Estilo CSS para cabeçalho fixo, botão e menu lateral
st.markdown("""
    <style>
        /* Cabeçalho fixo */
        .header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #0066ff;
            color: white;
            padding: 15px 10px;
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
            padding: 10px;
            font-size: 20px;
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

# Cabeçalho com botão e título
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

# Menu lateral simulado ao clicar no botão
menu = st.sidebar.radio("Menu", ["Cartões Espelho", "Laudos e Receitas"])

# Rodapé fixo
st.markdown("""
    <div class="footer">
        Desenvolvido para ACS
    </div>
""", unsafe_allow_html=True)
