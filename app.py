import streamlit as st
from streamlit_option_menu import option_menu

def main():
    st.set_page_config(page_title="ACS Micro Área", page_icon="🏥", layout="centered")
    
    # Estilização CSS para ajuste no celular
    st.markdown(
        """
        <style>
            .css-18e3th9 {
                padding-top: 0rem;
            }
            .css-1d391kg {
                padding-top: 0rem;
            }
            .css-1v3fvcr {
                padding-top: 0rem;
            }
            header {
                display: none;
            }
            .block-container {
                padding-top: 0rem;
            }
            .stApp {
                overflow: hidden;
            }
            .header {
                background-color: #0056b3;
                color: white;
                text-align: center;
                padding: 10px;
                font-size: 22px;
                font-weight: bold;
                position: fixed;
                width: 100%;
                top: 0;
                z-index: 1000;
            }
            .footer {
                background-color: #0056b3;
                color: white;
                text-align: center;
                padding: 10px;
                font-size: 16px;
                position: fixed;
                width: 100%;
                bottom: 0;
                z-index: 1000;
            }
            .main-content {
                margin-top: 60px;
                margin-bottom: 40px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    # Cabeçalho fixo
    st.markdown('<div class="header">ACS Micro Área</div>', unsafe_allow_html=True)
    
    # Menu lateral
    with st.sidebar:
        selected = option_menu("Menu", ["Início", "Laudos e Receitas", "Cartões Espelho"],
                               icons=["house", "file-medical", "id-card"],
                               menu_icon="list", default_index=0)
    
    # Conteúdo principal
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    st.title(f"Bem-vindo, Ataide!")
    
    st.subheader("Cadastros")
    st.button("🏠 Domicílios")
    st.button("👨‍👩‍👧 Famílias")
    st.button("👦 Cidadãos")
    
    st.subheader("Análises e Relatórios")
    st.button("📊 Relatórios")
    st.button("📈 Resumo de Produção")
    st.button("👶⚰️ Nascimentos e Óbitos")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Rodapé fixo
    st.markdown('<div class="footer">Desenvolvido para ACS</div>', unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()
