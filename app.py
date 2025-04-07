import streamlit as st
import streamlit.components.v1 as components

# Configuração da página
st.set_page_config(page_title="ACS Micro Área", page_icon="🏥", layout="centered")

# Estilos CSS
st.markdown("""
    <style>
        /* Cabeçalho ocupando toda a largura */
        .custom-header {
            background-color: #0d6efd;
            color: white;
            padding: 14px 16px;
            font-size: 24px;
            font-weight: bold;
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin: -3.5rem -1rem 2rem -1rem;
            z-index: 99;
        }

        .menu-icon {
            font-size: 26px;
            cursor: pointer;
            margin-right: 12px;
        }

        /* Rodapé fixo */
        .custom-footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #0d6efd;
            color: white;
            text-align: center;
            padding: 8px;
            font-size: 14px;
            z-index: 100;
        }

        /* Botões de menu com bordas arredondadas */
        .menu-button {
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 8px 16px;
            margin-bottom: 10px;
            font-size: 16px;
            display: inline-block;
        }

        /* Ícones com espaçamento */
        .menu-button span {
            margin-right: 6px;
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho com ícone de menu lateral
st.markdown('''
    <div class="custom-header">
        <div class="menu-icon" onclick="document.querySelector('details[open] summary').click();">&#9776;</div>
        ACS Micro Área
    </div>
''', unsafe_allow_html=True)

# Conteúdo da tela
st.markdown("## Bem-vindo, Ataide!")
st.markdown("### Cadastros")

st.markdown('<div class="menu-button">🏠 <b>Domicílios</b></div>', unsafe_allow_html=True)
st.markdown('<div class="menu-button">👨‍👩‍👧‍👦 <b>Famílias</b></div>', unsafe_allow_html=True)
st.markdown('<div class="menu-button">🧑 <b>Cidadãos</b></div>', unsafe_allow_html=True)

st.markdown("### Análises e Relatórios")
st.markdown('<div class="menu-button">📊 <b>Relatórios</b></div>', unsafe_allow_html=True)
st.markdown('<div class="menu-button">📈 <b>Resumo de Produção</b></div>', unsafe_allow_html=True)
st.markdown('<div class="menu-button">👶⚰️ <b>Nascimentos e Óbitos</b></div>', unsafe_allow_html=True)

# Espaço extra para o rodapé
st.markdown("<br><br><br><br>", unsafe_allow_html=True)

# Rodapé
st.markdown('<div class="custom-footer">Desenvolvido para ACS</div>', unsafe_allow_html=True)
