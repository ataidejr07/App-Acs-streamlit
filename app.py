import streamlit as st
from streamlit_extras.let_it_rain import rain

def main():
    # Configuração da página
    st.set_page_config(page_title="ACS Micro Área", layout="wide")
    
    # CSS para o cabeçalho fixo
    st.markdown(
        """
        <style>
        .header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #007bff;
            color: white;
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            padding: 15px;
            z-index: 1000;
        }
        .main-content {
            padding-top: 70px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Cabeçalho fixo
    st.markdown('<div class="header">ACS Micro Área</div>', unsafe_allow_html=True)
    
    # Conteúdo principal
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    st.subheader("Bem-vindo, Ataide!")
    
    # Seção de Cadastros
    st.subheader("Cadastros")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🏠 Domicílios"):
            st.info("Gerencie os endereços cadastrados e veja quem mora em cada residência.")
    with col2:
        if st.button("👤 Pacientes"):
            st.info("Visualize e gerencie os dados dos pacientes cadastrados.")
    with col3:
        if st.button("📂 Prontuários"):
            st.info("Acesse prontuários detalhados dos pacientes.")
    
    col4, col5, col6 = st.columns(3)
    with col4:
        if st.button("📑 Cartões Espelho"):
            st.info("Acesse e gerencie os Cartões Espelho dos pacientes.")
    with col5:
        if st.button("📄 Laudos e Receitas"):
            st.info("Gerencie laudos e receitas médicas dos pacientes.")
    with col6:
        if st.button("📊 Nascimentos e Óbitos"):
            st.info("Registre e acompanhe nascimentos e óbitos na comunidade.")
    
    st.sidebar.title("Menu")
    st.sidebar.button("🏠 Domicílios")
    st.sidebar.button("👤 Pacientes")
    st.sidebar.button("📂 Prontuários")
    st.sidebar.button("📑 Cartões Espelho")
    st.sidebar.button("📄 Laudos e Receitas")
    st.sidebar.button("📊 Nascimentos e Óbitos")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()
